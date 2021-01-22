#!/bin/bash

if [ $# -ne 8 ]; then
    echo "./procedure.sh [repeat_times] [parameter] [component] [v1] [v2] [testProject] [unitTest] [reconfPoint]"
    exit -1
fi

# disable conf tracking
echo 'false' > ~/reconf_test_gen/lib/enable

parameter=$1
component=$4
v1=$6
v2=$7
testProject=$2
unitTest=$3
reconfPoint=$5
repeat_times=$8

java -cp /root/parameter_test_controller/target/ Hypothesis "$repeat_times" "$parameter" "$component" "$v1" "$v2" "$testProject" "$unitTest" "$reconfPoint"
