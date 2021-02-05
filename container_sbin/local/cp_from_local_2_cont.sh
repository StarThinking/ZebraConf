#!/bin/bash

if [ $# -ne 2 ]; then echo 'wrong: [local_src] [container_dst]'; exit -1; fi

local_src=$1
container_dst=$2

for my_container in $(docker ps -aq)
do
    docker cp $local_src $my_container:$container_dst
done
