#!/bin/bash
echo $@
if [ $# -ne 3 ]; then echo 'ERROR: ./run_mvn_test.sh [project] [test_name] [verbose_enable]'; exit -1; fi

the_project=$1
project_root_dir=$(cat /root/ZebraConf/app_meta/"$the_project"/project_root_dir.txt)
zebraconf_class_test_mapping_path=/root/ZebraConf/app_meta/"$the_project"/about_test/CORRECT_ZEBRA_CLASSES.txt
if [ $? -ne 0 ]; then echo 'ERROR: project name is wrong'; exit -1; fi
the_test=$2
classname=$(echo $the_test | awk -F '#' '{print $1}')
short_classname=$(echo $classname | awk -F '.' '{print $NF}')
testname=$(echo $the_test | awk -F '#' '{print $2}')
log_dts_dir='/root/ZebraConf/app_meta/log'
echo "the_test is $the_test"
verbose_enable=$3
echo "$verbose_enable" > /root/ZebraConf/app_meta/lib/enable

# find the innerest sub project path
can_find_sub_dir=0 # 1 means can, 0 means connot
sub_project_path=''

function find_sub_project_dir {
    class_type=$1
    #sub_project_path=$(grep "$classname " /root/ZebraConf/app_meta/"$the_project"/about_test/mapping.txt | awk '{print $2}')
    if [ "$sub_project_path" == "" ]; then
        sub_project_path_count=$(find $project_root_dir -name "$short_classname"".""$class_type" | grep '/src/test/' | wc -l)
        if [ $sub_project_path_count -ge 0 ]; then
            class_path=$(echo $classname | awk -F '.' '{for (i=1; i<NF-1; i++) printf "%s.", $i}';  echo $classname | awk -F '.' '{print $(NF-1)}')
    	    #echo "class_path = $class_path"
    	    candidates=( $(find $project_root_dir -name "$short_classname"".""$class_type" | grep '/src/test/') )
    	    the_matched=""
    	
    	    for cand in ${candidates[@]}
     	    do
    	        # check if the class file contains the package pattern
    	        if [ "$(grep ^"package $class_path" $cand)" != "" ] && [ "$the_matched" == "" ]; then 
    		    the_matched="$cand"
    	        fi
    	    done
    
    	    if [ "$the_matched" != "" ]; then
     	        sub_project_path=$(echo "$the_matched" | awk -F '/src/test/' '{print $1}')
                echo "INFO: find sub project path for $the_test at $sub_project_path by searching $class_type class with package $short_classname"
                can_find_sub_dir=1
            fi
        fi
    else
        echo "find sub project path for $the_test from mapping"
        can_find_sub_dir=1
    fi
}

# search for java class first
find_sub_project_dir 'java'
if [ $can_find_sub_dir -eq 0 ]; then # then scala
    find_sub_project_dir 'scala'
fi

if [ $can_find_sub_dir -eq 0 ]; then
    echo "ERROR: cannot find sub project path for $the_test"
    sub_project_path="$the_project"
fi

echo "run test under sub_project_path $sub_project_path"

# run mvn test
rc=1
cd $sub_project_path

# if unit test uses pattern of unit_test_class#zebraconf_class_test, replace zebraconf_class_test with real correct tests
the_real_test="$the_test"
can_find_zebraconf_test_mapping=1 # 1 means can, 0 means connot
if [ "$testname" == "zebraconf_class_test" ]; then
    if [ "$(grep "$the_test" $zebraconf_class_test_mapping_path)" == "" ]; then
        can_find_zebraconf_test_mapping=0
    else
        the_real_test="$(grep "$the_test" $zebraconf_class_test_mapping_path | awk -F '#zebraconf_class_test ' '{print $2}')"
    fi
fi

if [ "$the_project" == "flink" ]; then
    if [ "$(echo $short_classname | grep 'ITCase'$)" != "" ]; then
	mvn integration-test -Dtest=$the_real_test
    else
	mvn test -Dtest=$the_real_test
    fi
else
    mvn test -Dtest=$the_real_test
fi
rc=$?

# set error rc
if [ $can_find_sub_dir -ne 1 ]; then
    rc=12
fi

if [ $can_find_zebraconf_test_mapping -ne 1 ]; then
    rc=13
fi

# find output log
output_log=$(find $sub_project_path -name "$classname"-output.txt)
if [ "$output_log" == "" ]; then
     echo 'ERROR: cannot find output_log for test $the_test'
     exit -1
else
    echo "output_log $output_log has been found"
fi

# move output log to dst directory
LOG_TIME="$(($(date +%s%N)/1000000))"
if [ ! -d $log_dts_dir ]; then 
    mkdir $log_dts_dir
fi
my_random_name="$the_test"-output_"$LOG_TIME"_"$RANDOM$RANDOM".txt
mv $output_log $log_dts_dir/$my_random_name
# append output_log path and return code to our log
echo "msx-output-log $output_log" >> $log_dts_dir/$my_random_name
echo "msx-rc $rc" >> $log_dts_dir/$my_random_name

# return exit code of mvn test
exit $rc
