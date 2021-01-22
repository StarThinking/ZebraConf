#!/bin/bash

IFS=$'\n'

function per_override_task {
    task_file=$1
    for line in $(cat $task_file)
    do 
        jar_name="$(echo $line | awk '{print $1}')"
        jar_path="$(echo $line | awk '{print $2}')"
        mvn_jar_path_num=$(find /root/.m2/ -name $jar_name | wc -l)
        mvn_jar_path=$(find /root/.m2/ -name $jar_name)
        if [ $mvn_jar_path_num -eq 0 ]; then
    	echo "$jar_name not used in mvn"
        elif [ $mvn_jar_path_num -eq 1 ]; then 
    	echo "USE $jar_path to override $mvn_jar_path"
           	cp $jar_path $mvn_jar_path
        else 
            echo "ERROR: $jar_name"; exit -1; 
        fi
    done
}

# hadoop common: Configuration, ReconfAgent, Listener (for all hadoop applications)
hadoop_version='3.2.1'
echo "perform jar override for hadoop common $hadoop_version"
cp /root/hadoop-"$hadoop_version"-src/hadoop-common-project/hadoop-common/target/*.jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop_version"/
# double override
#cp /root/reconf_test_gen/javassist_study/conf_return/hadoop-common-3.2.1.jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop_version"/

# hadoop common: Configuration, ReconfAgent
hadoop_version='2.8.5'
echo "perform jar override for hadoop common $hadoop_version"
cp /root/hadoop-"$hadoop_version"-src/hadoop-common-project/hadoop-common/target/*.jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop_version"/
# double override
#cp /root/reconf_test_gen/javassist_study/conf_return/hadoop-common-2.8.5.jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop_version"/

# hbase common: Listener, HBaseConfiguration
echo "perform jar override for hbase common 2.2.4"
cp /root/hbase-2.2.4/hbase-common/target/*.jar /root/.m2/repository/org/apache/hbase/hbase-common/2.2.4/

# system component modification
for i in $(find ~/reconf_test_gen -name 'override_jar_store.txt')
do
    echo ''
    echo "perform jar override for $i"
    per_override_task $i
done
