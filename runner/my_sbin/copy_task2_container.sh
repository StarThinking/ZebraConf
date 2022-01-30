#!/bin/bash

if [ $# -ne 1 ]; then echo './split_task2_local_container.sh: [my_task]'; exit -1; fi

my_task=$1
container_prefix='container-'
container_names=( $(docker container list -a | awk '{print $NF}' | grep -v NAMES) )
container_num=${#container_names[@]}
container_task_path='/root/vm_images/ZebraConf/runner/task.txt'
tmp_prefix='my_tmp_prefix'

# split task file
split -d -n l/$container_num $my_task $tmp_prefix
for i in $(seq 0 9)
do 
    mv "$tmp_prefix"0"$i" "$tmp_prefix""$i"
done

# copy file to container task path
for container in ${container_names[@]}
do
    id=$(echo $container | awk -F "$container_prefix" '{print $2}')
    echo docker cp "$tmp_prefix""$id" "$container_prefix""$id":"$container_task_path"
    docker cp "$tmp_prefix""$id" "$container_prefix""$id":"$container_task_path"
done

# remove tmp files
rm "$tmp_prefix"*
