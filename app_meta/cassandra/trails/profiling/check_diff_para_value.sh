#!/bin/bash

log=$1

num1=$(~/vm_images/ZebraConf/app_meta/cassandra/trails/profiling/convert.sh $log | sort -k 1,2 | sort -u | awk '{print $1" "$2}' | sort -u | wc -l)

num2=$(~/vm_images/ZebraConf/app_meta/cassandra/trails/profiling/convert.sh $log | sort -k 1,2 | sort -u | wc -l)

if [ $num1 -eq $num2 ]; then
    echo "$num1 $num2"
else
    echo "$num1 $num2 not same"
fi
