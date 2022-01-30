#!/bin/bash

for i in $(seq 0 4)
do 
    last="$(docker exec container-$i bash -c 'cat /root/vm_images/ZebraConf/runner/nohup.txt' | grep 'assign entry' | tail -n 1 | awk '{print $(NF - 2)}')"
    task_num=$(docker exec container-$i bash -c 'cat /root/vm_images/ZebraConf/runner/task.txt | wc -l')
    echo "container-$i: $last / $task_num"
    docker exec container-$i bash -c 'find /root/vm_images/ZebraConf/runner/log -name *single_hypo*'
done
