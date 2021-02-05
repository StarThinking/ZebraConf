#!/bin/bash

if [ $# -ne 1 ]; then echo '[while_list.txt]'; exit -1; fi

new_file=$1

# first, transfer to local node
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    scp $new_file node-$i:/root/vm_images/ZebraConf/runner/
done

# second, run cp_from_local_2_cont.sh asynchronizedly
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    ssh node-$i "/root/vm_images/ZebraConf/container_sbin/local/cp_from_local_2_cont.sh /root/vm_images/ZebraConf/runner/white_list.txt /root/ZebraConf/runner/white_list.txt &" & pids+=($!)
done

for p in ${pids[@]}
do 
    wait $p
    echo "$p is done"
done
