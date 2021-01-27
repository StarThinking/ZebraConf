#!/bin/bash

if [ $# -ne 2 ]; then echo "wrong [tag] [vms]"; exit -1; fi
pm=( $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n) )
tag=$1
vms=$2

pids=()

for i in ${pm[@]}
do 
    ssh node-$i "~/vm_images/ZebraConf/runner/sbin/local/rebuild_local_containers.sh $tag $vms" & pids[$i]=$!
done

for p in ${pids[@]}
do 
    wait $p
done

echo "all done"
