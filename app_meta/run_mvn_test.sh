#!/bin/bash
echo $@
#if [ $# -lt 3 ]; then echo 'ERROR: ./run_mvn_test.sh [project] [test_name] [log_dts_dir|none]'; exit -1; fi
if [ $# -ne 2 ]; then echo 'ERROR: ./run_mvn_test.sh [project] [test_name]'; exit -1; fi

the_project=$1
project_root_dir=$(cat /root/ZebraConf/app_meta/"$the_project"/project_root_dir.txt)
if [ $? -ne 0 ]; then echo 'ERROR: project name is wrong'; exit -1; fi
the_test=$2
classname=$(echo $the_test | awk -F '#' '{print $1}')
testname=$(echo $the_test | awk -F '#' '{print $2}')
log_dts_dir='/root/ZebraConf/app_meta/log'
echo "the_test is $the_test"

#sub_project_classes_dir="/root/ZebraConf/app_meta/"$the_project"/all_classes"
#suffix='all_classes.txt'
#raw_sub_project=$(cd $sub_project_classes_dir; grep ^"$classname"$ *.txt | awk -F 'all_classes.txt' '{print $1}' | sed 's#%#/#g')
#if [ "$raw_sub_project" == "" ]; then
#    echo "ERROR: cannot find sub_project for $the_test"; exit -1;
#fi
#sub_project="$project_root_dir""$raw_sub_project"
#echo "sub_project for $the_test is $sub_project"

# run mvn test
rc=1
cd $project_root_dir; mvn test -Dtest=$the_test
rc=$?

# find output log
output_log=$(find $project_root_dir -name "$classname"-output.txt)
echo "output_log is $output_log"
if [ "$output_log" == "" ]; then
     echo 'ERROR: cannot find output_log for test $the_test'
     exit -1;
fi

# move output log to dst directory
if [ ! -d $log_dts_dir ]; then 
    mkdir $log_dts_dir
fi
mv $output_log $log_dts_dir/"$the_test"-output.txt
# append output_log path and return code to our log
echo "msx-output-log $output_log" >> $log_dts_dir/"$the_test"-output.txt
echo "msx-rc $rc" >> $log_dts_dir/"$the_test"-output.txt

# return exit code of mvn test
exit $rc
