#!/bin/bash

if [ $# -ne 2 ]; then echo 'wrong args: [parameter_list_file] [dst_dir]'; exit -1; fi

parameter_list_file=$1
dst_dir=$2

pids=()
for p in $(cat $parameter_list_file)
do 
    ./generate_tuples.sh $p > $dst_dir/"$p".txt & pids+=($!)
done

for id in ${pids[@]}
do 
    wait $id
    echo "thread $id job is done"
done
