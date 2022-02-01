#!/bin/bash

for i in $(seq 0 4)
do 
    last="$(docker exec container-$i bash -c 'cat /root/vm_images/ZebraConf/runner/nohup.txt' | grep --text 'assign entry' | tail -n 1 | awk '{print $(NF - 2)}')"
    task_num=$(docker exec container-$i bash -c 'cat /root/vm_images/ZebraConf/runner/task.txt | wc -l')
    last=$(( last + 1 ))
    echo "container-$i: $(( $last * 2 )) / $(( $task_num * 2 ))"
    docker exec container-$i bash -c 'find /root/vm_images/ZebraConf/runner/log -name *single_hypo* | while read i; do cat $i | head -n 4 | tail -n 1; cat $i | tail -n 4 | head -n 2; done'
    echo ''
done
