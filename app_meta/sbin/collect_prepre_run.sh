#!/bin/bash

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    ssh node-$i '/root/vm_images/ZebraConf/container_sbin/local/cp_from_cont_2_local_by_key.sh txt /root/ZebraConf/app_meta/log/ /root/vm_images/ZebraConf/app_meta/log/' &
    pids[$i]=$!
done

for p in ${pids[@]}
do
    wait $p; echo "node $p copy finished"
done
    
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do
    ssh node-$i "cd /root/vm_images/ZebraConf/app_meta/log/; tar zcvf $i.tar.gz *"
    scp node-$i:/root/vm_images/ZebraConf/app_meta/log/$i.tar.gz /root/vm_images/ZebraConf/app_meta/log/
done
