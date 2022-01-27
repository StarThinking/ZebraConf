#!/bin/bash

#set -x
IFS=$'\n'
log=$1

daemon_pids=( $(cat $log | grep $'init daemon ' | awk '{print $NF}') )
client_pids=( $(cat $log | grep $'init client ' | awk '{print $NF}') )
tool_pids=( $(cat $log | grep $'init tool ' | awk '{print $NF}') )
gets=( "$(cat $log | grep $'zbGet')" )

for get in ${gets[@]}
do
    get_pid=$(echo "$get" | awk '{print $2}')
    get_compoenet_id=$(echo "$get" | awk '{print $3}')
    get_parameter=$(echo "$get" | awk '{print $4}')
    get_value=$(echo "$get" | awk '{print $5}')
    component_type=0
    daemon_id=0
    client_id=0
    tool_id=0
#    echo "get_pid = $get_pid, get_parameter = $get_parameter, get_value = $get_value"
    for mypid in ${daemon_pids[@]}
    do
        daemon_id=$(( daemon_id + 1 ))
        if [ $mypid -eq $get_pid ]; then
            component_type=1
            break
        fi
    done
    
    for mypid in ${client_pids[@]}
    do
        client_id=$(( client_id + 1 ))
        if [ $mypid -eq $get_pid ]; then
            component_type=2
            break
        fi
    done
    
    for mypid in ${tool_pids[@]}
    do
        tool_id=$(( tool_id + 1 ))
        if [ $mypid -eq $get_pid ]; then
            component_type=3
            break
        fi
    done
    
    if [ $component_type -eq 1 ]; then
        echo "$get_parameter CassandraDaemon.$daemon_id $get_compoenet_id $get_value"
        #echo "$get_parameter Daemon.$daemon_id $get_value"
    elif [ $component_type -eq 2 ]; then
        echo "$get_parameter Client.$client_id $get_compoenet_id $get_value"
        #echo "$get_parameter Client.$client_id $get_value"
    elif [ $component_type -eq 3 ]; then
        echo "$get_parameter Tool.$tool_id $get_compoenet_id $get_value"
        #echo "$get_parameter Tool.$tool_id $get_value"
    else
        echo "ERROR: cannot identify $get_pid"
    fi
done
