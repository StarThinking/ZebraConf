#!/bin/bash
echo $@
if [ $# -lt 3 ]; then echo 'ERROR: ./run_mvn_test.sh [project] [test_name] [log_dts_dir|none]'; exit -1; fi

# yarn mapreduce hdfs hbase
the_project=$1
project_root_dir=$(cat /root/ZebraConf/app_meta/"$the_project"/project_root_dir.txt)
if [ $? -ne 0 ]; then echo 'ERROR: project name is wrong'; exit -1; fi

the_test=$2
classname=$(echo $the_test | awk -F '#' '{print $1}')
testname=$(echo $the_test | awk -F '#' '{print $2}')
sub_project_classes_dir="/root/ZebraConf/app_meta/"$the_project"/all_classes"

log_dts_dir="$3"

suffix='all_classes.txt'
raw_sub_project=$(cd $sub_project_classes_dir; grep ^"$classname"$ *.txt | awk -F 'all_classes.txt' '{print $1}' | sed 's#%#/#g')
if [ "$raw_sub_project" == "" ]; then
    echo "ERROR: cannot find sub_project for $the_test"; exit -1;
fi
sub_project="$project_root_dir""$raw_sub_project"
echo "sub_project for $the_test is $sub_project"

# run mvn test
echo "the_test is $the_test"
#cd $project_root_dir; mvn test -Dtest=$the_test
rc=1
rm ~/mvn_tmp_log.txt &> /dev/null
cd $sub_project; mvn test -Dtest=$the_test &> ~/mvn_tmp_log.txt
rc=$?

# log
test_log="$sub_project"/target/surefire-reports/"$classname"-output.txt
if [ ! -f $test_log ]; then echo 'ERROR: cannot find test_log for test $the_test'; exit -1; fi
#echo "test_log is $test_log"
if [ "$log_dts_dir" != "none" ]; then 
    mv $test_log $log_dts_dir/"$the_test"-output.txt
    mv ~/mvn_tmp_log.txt $log_dts_dir/"$the_test"-mvnlog.txt
    
    echo "msx-rc $rc" >> $log_dts_dir/"$the_test"-output.txt
    echo "msx-rc $rc" >> $log_dts_dir/"$the_test"-mvnlog.txt
fi

# return exit code of mvn test
exit $rc
