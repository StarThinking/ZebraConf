#!/bin/bash

if [ $# -ne 1 ]; then echo '[proj]'; exit -1; fi

proj=$1
pids=()

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    ssh node-$i "rm ~/nohup.txt; ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9; nohup ~/vm_images/ZebraConf/app_meta/sbin/dispatcher.sh $proj > nohup.txt &" & pids+=$!
done

for p in ${pids[@]}
do 
    wait $p
    echo "$p is done"
done
