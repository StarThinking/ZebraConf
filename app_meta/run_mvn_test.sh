#!/bin/bash
echo $@
if [ $# -ne 3 ]; then echo 'ERROR: ./run_mvn_test.sh [project] [test_name] [verbose_enable]'; exit -1; fi

the_project=$1
project_root_dir=$(cat /root/ZebraConf/app_meta/"$the_project"/project_root_dir.txt)
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
sub_project_path=$(grep "$classname " /root/ZebraConf/app_meta/"$the_project"/about_test/mapping.txt | awk '{print $2}')
if [ "$sub_project_path" == "" ]; then
    sub_project_path_count=$(find $project_root_dir -name "$short_classname"".java" | grep 'src/test' | wc -l)

    if [ $sub_project_path_count -eq 0 ]; then
        echo "ERROR: cannot find sub project path for $the_test"
        # just use project root dir
        sub_project_path="$project_root_dir"
    elif [ $sub_project_path_count -eq 1 ]; then
        sub_project_path=$(find $project_root_dir -name "$short_classname"".java" | grep 'src/test' | awk -F 'src/test' '{print $1}')
        echo "WARN: find sub project path for $the_test by finding $short_classname java class at $sub_project_path"
    else
        path_last_dir_name=$(echo $classname | awk -F '.' '{print $(NF-1)}')
        sub_project_path_count_filter=$(find $project_root_dir -name "$short_classname"".java" | grep 'src/test' | grep $path_last_dir_name | grep wc -l)
        if [ $sub_project_path_count_filter -eq 0 ]; then
            echo "ERROR: cannot find sub project path for $the_test"
            # just use project root dir
            sub_project_path="$project_root_dir"
        elif [ $sub_project_path_count_filter -eq 1 ]; then
            echo "WARN: find sub project path for $the_test by finding $short_classname java class at $sub_project_path"
            sub_project_path=$(find $project_root_dir -name "$short_classname"".java" | grep 'src/test' | grep $path_last_dir_name | awk -F 'src/test' '{print $1}')
        else
            echo "ERROR: find multiple sub project path for $the_test"
            # just use the first one
            sub_project_path=$(find $project_root_dir -name "$short_classname"".java" | grep 'src/test' | grep $path_last_dir_name | head -n 1 | awk -F 'src/test' '{print $1}')
        fi
    fi
else
    echo "find sub project path for $the_test from mapping"
fi
echo "run test under sub_project_path $sub_project_path"

# run mvn test
rc=1
cd $sub_project_path
if [ "$the_project" == "flink" ]; then
    if [ "$(echo $short_classname | grep 'ITCase'$)" != "" ]; then
	mvn integration-test -Dtest=$the_test
    else
	mvn test -Dtest=$the_test
    fi
else
    mvn test -Dtest=$the_test
fi
rc=$?

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
