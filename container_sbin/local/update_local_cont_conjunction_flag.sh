#!/bin/bash

if [ $# -ne 1 ]; then echo '[true|false]'; exit -1; fi

conjunction_enable=$1

for my_cont in $(docker ps -aq)
do
    docker exec $my_cont bash -c "echo $conjunction_enable > /root/ZebraConf/runner/conjunction_enable" 
done
