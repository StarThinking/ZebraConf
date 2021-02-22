#!/bin/bash
echo $@
if [ $# -ne 3 ]; then echo 'ERROR: ./run_mvn_test.sh [project] [test_name] [verbose_enable]'; exit -1; fi

the_project=$1
project_root_dir=$(cat /root/ZebraConf/app_meta/"$the_project"/project_root_dir.txt)
if [ $? -ne 0 ]; then echo 'ERROR: project name is wrong'; exit -1; fi
the_test=$2
classname=$(echo $the_test | awk -F '#' '{print $1}')
testname=$(echo $the_test | awk -F '#' '{print $2}')
log_dts_dir='/root/ZebraConf/app_meta/log'
echo "the_test is $the_test"
verbose_enable=$3
echo "$verbose_enable" > /root/ZebraConf/app_meta/lib/enable

# find the innerest sub project path
sub_project_path=$(grep "$classname " /root/ZebraConf/app_meta/"$the_project"/about_test/mapping.txt | awk '{print $2}')
if [ "$sub_project_path" == "" ]; then
    echo "WARN: cannot find sub project path for $the_test"
    sub_project_path="$project_root_dir"
    #exit -1
fi
echo "run test under sub_project_path $sub_project_path"

# run mvn test
rc=1
cd $sub_project_path; mvn test -Dtest=$the_test
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
mv $output_log $log_dts_dir/"$the_test"-output.txt
# append output_log path and return code to our log
echo "msx-output-log $output_log" >> $log_dts_dir/"$the_test"-output_"$LOG_TIME"_"$RANDOM$RANDOM".txt
echo "msx-rc $rc" >> $log_dts_dir/"$the_test"-output_"$LOG_TIME"_"$RANDOM$RANDOM".txt

# return exit code of mvn test
exit $rc
