#!/bin/bash

if [ $# -ne 0 ]; then 
    echo './collect_single_run.sh'
    exit -1
fi

compress=0
pids=()

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    if [ $compress -eq 1 ]; then
        ssh node-$i '/root/vm_images/ZebraConf/container_sbin/local/cp_from_cont_2_local_by_key_w_compress.sh hypothesis /root/ZebraConf/runner/log/ /root/vm_images/ZebraConf/runner/log/' &
    else
        ssh node-$i '/root/vm_images/ZebraConf/container_sbin/local/cp_from_cont_2_local_by_key.sh single_run /root/ZebraConf/runner/log/ /root/vm_images/ZebraConf/runner/log/' &
    fi
    pids+=($!)
done

for p in ${pids[@]}
do
    wait $p
    echo "node $p copy finished"
done
    
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do
    ssh node-$i "cd /root/vm_images/ZebraConf/runner/log/; tar zcvf $i.tar.gz *"
    scp node-$i:/root/vm_images/ZebraConf/runner/log/$i.tar.gz /root/vm_images/ZebraConf/runner/log/
done
