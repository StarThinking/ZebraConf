#!/bin/bash

if [ $# -ne 1 ]; then echo wrong: num; exit -1; fi
num=$1

for i in $(seq 0 $num)
do 
    docker container stop hadoop-$i &
    pids[$i]=$!
done

for i in $(seq 0 $num)
do
    wait ${pids[$i]}
done
echo 'all containers are stopped'

pids=()

for i in $(seq 0 $num)
do 
    docker container rm hadoop-$i &
    pids[$i]=$!
done
    

for i in $(seq 0 $num)
do
    wait ${pids[$i]}
done
echo 'all containers are removed'
