#!/bin/bash

IFS=$'\n'

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
