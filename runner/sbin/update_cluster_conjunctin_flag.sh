#!/bin/bash

if [ $# -ne 1 ]; then echo '[true|false]'; exit -1; fi

conjunction_enable=$1

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    ssh node-$i "/root/vm_images/ZebraConf/container_sbin/local/update_local_cont_conjunction_flag.sh $conjunction_enable &" & pids+=($!)
done

for p in ${pids[@]}
do 
    wait $p
    echo "$p is done"
done
