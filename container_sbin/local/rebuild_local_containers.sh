#!/bin/bash

if [ $# -ne 2 ]; then echo "wrong [tag] [vms]"; exit -1; fi
tag=$1
vms=$(( $2 - 1 )) # minus one here

# kill dispatcher
ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9
killall -9 dispatcher_hypo.sh
pkill dispatcher_hypo.sh
killall -9 dispatcher.sh
pkill dispatcher.sh
echo "dispatcher is killed"

# update ZebraConf
cd ~/vm_images/ZebraConf; git pull
echo "ZebraConf is updated"

# delete containers
~/vm_images/ZebraConf/container_sbin/local/delete_local_containers.sh
echo "containers are deleted"

# create containers
~/vm_images/ZebraConf/container_sbin/local/create_local_containers.sh $tag $vms
echo "containers are created"

# clean and build runners
~/vm_images/ZebraConf/container_sbin/local/clean_and_build.sh
echo "runner is built"
