#!/bin/bash

pm=( $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n) )
vm=$(( $(cat /proc/cpuinfo | grep 'processor' | wc -l) / 2 ))
if [ $vm -gt 20 ]; then vm=10; fi
vm=10
vm=$(( vm -1 ))

for i in ${pm[@]}; do ssh node-$i "~/parameter_test_controller/container_utility_sh/update_white_list_all_containers.sh $vm" & pids[$i]=$!; done; for p in ${pids[@]}; do wait $p; echo container git update finished; done
