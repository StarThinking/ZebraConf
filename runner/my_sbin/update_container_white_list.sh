#!/bin/bash

if [ $# -ne 1 ]; then echo './update_container_white_list.sh: [my_white_list]'; exit -1; fi

my_white_list=$1
container_prefix='container-'
container_names=( $(docker container list -a | awk '{print $NF}' | grep -v NAMES) )
container_num=${#container_names[@]}
container_task_path='/root/vm_images/ZebraConf/runner/white_list.txt'

# copy file to container task path
for container in ${container_names[@]}
do
    id=$(echo $container | awk -F "$container_prefix" '{print $2}')
    echo docker cp $my_white_list "$container_prefix""$id":"$container_task_path"
    docker cp $my_white_list "$container_prefix""$id":"$container_task_path"
done
