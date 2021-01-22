#!/bin/bash

if [ $# -ne 2 ]; then echo wrong: pm vm; exit -1; fi

pm=$1
vm=$2

for j in $(seq 0 $pm)
do 
    ssh node-$j 'nums=$(for i in $(seq 0 '$vm'); do docker exec hadoop-$i bash -c "ls /root/parameter_test_controller | grep dfs. | wc -l" ; done); for i in ${nums[@]}; do echo $i; done | awk '\''{s+=$1} END {print s}'\''' &
    pids[$j]=$!
done | tee >(awk '{s+=$1} END {print s}')

for i in $(seq 0 $pm)
do
    wait ${pids[$i]}
done
