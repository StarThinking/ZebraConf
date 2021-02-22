#!/bin/bash

if [ $# -ne 0 ]; then echo 'no arguments'; exit -1; fi

pids=()

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    ssh node-$i "rm ~/nohup.txt; ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9; nohup ~/vm_images/ZebraConf/runner/sbin/dispatcher_v1v2.sh > nohup.txt &" & pids+=($!)
done

for p in ${pids[@]}
do 
    wait $p
    echo "$p is done"
done
