#!/bin/bash

if [ $# -ne 3 ]; then echo 'wrong: [key] [container_log_dir] [local_log_dir']; exit -1; fi

key=$1
container_log_dir=$2
local_log_dir=$3

function fetch {
    my_cont=$1
    rm -rf ~/my_tmp 
    docker cp $my_cont:$container_log_dir ~/my_tmp
    find ~/my_tmp/ -name "*$key*" | xargs mv -t $local_log_dir
}

# before transfer, re-mkdir local_log_dir
rm -rf $local_log_dir &> /dev/null
mkdir $local_log_dir

for my_container in $(docker container list -a | awk '{print $NF}' | grep -v NAMES)
do
    fetch $my_container
done

echo "all files with key $key are fetched"
