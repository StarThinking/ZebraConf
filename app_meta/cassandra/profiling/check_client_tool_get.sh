#!/bin/bash

log=$1

daemon_pids=( $(cat $log | grep $'init daemon ' | awk '{print $NF}') )
client_pids=( $(cat $log | grep $'init client ' | awk '{print $NF}') )
tool_pids=( $(cat $log | grep $'init tool ' | awk '{print $NF}') )
get_pids=( $(cat $log | grep $'zbGet' | awk '{print $2}' | sort -u) )

for get_pid in ${get_pids[@]}
do
    found=0
    for pid in ${daemon_pids[@]}
    do
        if [ $pid -eq $get_pid ]; then
            found=1
        fi
    done
    
    for pid in ${client_pids[@]}
    do
        if [ $pid -eq $get_pid ]; then
            found=2
        fi
    done
    
    for pid in ${tool_pids[@]}
    do
        if [ $pid -eq $get_pid ]; then
            found=3
        fi
    done
    
    if [ $found -eq 1 ]; then
        echo "$get_pid called from daemon process"
    elif [ $found -eq 2 ]; then
        echo "$get_pid called from client process"
    elif [ $found -eq 3 ]; then
        echo "$get_pid called from tool process"
    else
        echo "$get_pid called from unknown process"
    fi
done
