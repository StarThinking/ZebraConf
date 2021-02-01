#!/bin/bash

if [ $# -ne 3 ]; then echo 'wrong: [key] [container_log_dir] [local_log_dir']; exit -1; fi

key=$1
container_log_dir=$2
local_log_dir=$3

function fetch {
    my_cont=$1
    files=$(docker exec $my_cont bash -c "ls $container_log_dir | grep -F $key")
    for f in ${files[@]}
    do
        docker exec $my_cont bash -c "cd $container_log_dir; /root/ZebraConf/app_meta/sbin/compress.sh $f" 
        docker exec $my_cont bash -c "cd $container_log_dir; rm $f" 
    done
    
    compressed_files=$(docker exec $my_cont bash -c "ls $container_log_dir | grep -F $key")
    for f in ${compressed_files[@]}
    do
	docker cp $my_cont:$container_log_dir/$f $local_log_dir
    done
}

# before transfer, re-mkdir local_log_dir
rm -rf $local_log_dir &> /dev/null
mkdir $local_log_dir

pids=()
for my_container in $(docker container list -a | awk '{print $NF}' | grep -v NAMES)
do
    fetch $my_container &
    pids+=($!)
done

for p_id in ${pids[@]}
do
    wait $p_id
done

echo "all files with key $key are fetched"
