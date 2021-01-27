#!/bin/bash

killall -9 dispatcher_hypo.sh
pkill dispatcher_hypo.sh
killall -9 dispatcher.sh
pkill dispatcher.sh

pids=()
for con in $(docker container list -a | awk '{print $NF}' | grep -v NAMES)
do 
    docker exec $con bash -c "pkill -9 java; cd /root/ZebraConf; git clean -df; git checkout -- *; git pull; cd runner; ./build.sh" &
    pids[$i]=$!
done

for i in $(seq 0 $num)
do
    wait ${pids[$i]}
done

echo 'runner is built'
