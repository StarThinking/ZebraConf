#!/bin/bash

if [ $# -ne 2 ]; then echo 'wrong: num key '; exit -1; fi

num=$1
key=$2

for i in $(seq 0 $num)
do
    docker exec hadoop-$i bash -c "/root/parameter_test_controller/container_utility_sh/list_files_key_stub.sh $num '$key'" &
    pids[$i]=$!
done

for i in $(seq 0 $num)
do
    wait ${pids[$i]}
done
