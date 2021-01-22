#!/bin/bash

if [ $# -ne 1 ]; then echo "wrong [tag]"; exit -1; fi
pm=( $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n) )
vm=$(( $(cat /proc/cpuinfo | grep 'processor' | wc -l) / 2 ))
if [ $vm -gt 20 ]; then vm=10; fi
vm=10
vm=$(( vm -1 ))
tag=$1

for i in ${pm[@]}; do ssh node-$i "ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9; killall -9 dispatcher_hypo.sh; pkill dispatcher_hypo.sh; killall -9 dispatcher.sh; pkill dispatcher.sh; "; done;

for i in ${pm[@]}; do ssh node-$i "cd ~/parameter_test_controller; git pull; cd ~/reconf_test_gen; git pull" & ppids[$i]=$!; done; for p in ${ppids[@]}; do wait $p; echo git update finished; done

for i in ${pm[@]}; do ssh node-$i "~/parameter_test_controller/container_utility_sh/rm_all_containers.sh $vm" & rmpids[$i]=$!; done; for p in ${rmpids[@]}; do wait $p; echo rm container finished; done

for i in ${pm[@]}; do ssh node-$i "~/parameter_test_controller/container_utility_sh/create_containers.sh $vm $tag" & vmpids[$i]=$!; done; for p in ${vmpids[@]}; do wait $p; echo creation finished; done

for i in ${pm[@]}; do ssh node-$i "~/parameter_test_controller/container_utility_sh/clean_update_all_container.sh $vm" & pids[$i]=$!; done; for p in ${pids[@]}; do wait $p; echo container git update finished; done
