#!/bin/bash

if [ $# -ne 3 ]; then echo 'wrong: [key] [src_dir] [dst_dir']; exit -1; fi

vm=$(( $(cat /proc/cpuinfo | grep 'processor' | wc -l) / 2 ))
if [ $vm -gt 20 ]; then vm=10; fi
vm=10
vm=$(( vm -1 ))
key=$1
src_dir=$2
dst_dir=$3

function fetch {
    d=$1
    #files=$(docker exec hadoop-$d bash -c "ls $src_dir | grep -F $key")
    #for f in ${files[@]}
    #do
	rm -rf ~/my_tmp 
	docker cp hadoop-$d:/"$src_dir" ~/my_tmp
        find ~/my_tmp/ -name "*$key*" | xargs mv -t "$dst_dir"
    #done
}

for i in $(seq 0 $vm)
do
    fetch $i
    #pids[$i]=$!
done

#for i in $(seq 0 $vm)
#do
#    wait ${pids[$i]}
#done

echo "all files with key $key are fetched"
