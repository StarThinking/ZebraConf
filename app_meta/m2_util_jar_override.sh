#!/bin/bash

IFS=$'\n'

# hadoop common: Configuration, ReconfAgent, Listener (for all hadoop applications)
hadoop3_version='3.2.1'
echo "perform jar override for hadoop common $hadoop3_version"
cp /root/hadoop-"$hadoop3_version"-src/hadoop-common-project/hadoop-common/target/*.jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop3_version"/
# override again with hacked hadoop common to retrieve get return value
cp /root/ZebraConf/app_meta/hack_conf_return/hadoop-common-"$hadoop3_version".jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop3_version"/

# hadoop common: Configuration, ReconfAgent
hadoop2_version='2.8.5'
echo "perform jar override for hadoop common $hadoop2_version"
cp /root/hadoop-"$hadoop2_version"-src/hadoop-common-project/hadoop-common/target/*.jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop2_version"/
# override again with hacked hadoop common to retrieve get return value
cp /root/ZebraConf/app_meta/hack_conf_return/hadoop-common-"$hadoop2_version".jar /root/.m2/repository/org/apache/hadoop/hadoop-common/"$hadoop2_version"/

# hbase common: Listener, HBaseConfiguration
echo "perform jar override for hbase common 2.2.4"
cp /root/hbase-2.2.4/hbase-common/target/*.jar /root/.m2/repository/org/apache/hbase/hbase-common/2.2.4/
