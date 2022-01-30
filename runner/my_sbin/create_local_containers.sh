#!/bin/bash

if [ $# -ne 2 ]; then echo ./create_local_containers.sh tag num; exit -1; fi

tag=$1
num=$(( $2 - 1 ))

for i in $(seq 0 $num)
do 
    docker run -d -it --name container-$i sixiangma/reconf_parameter:$tag
done

docker container list -a
