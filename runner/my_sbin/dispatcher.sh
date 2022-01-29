#!/bin/bash

source ~/.profile

if [ $# -ne 0 ]; then echo 'ERROR: ./dispatcher.sh'; exit -1; fi

IFS=$'\n' 
entry_list=( $(cat "$ZEBRACONF_HOME"/runner/task.txt) )
entry_list_length=${#entry_list[@]}
entry_cursor=0
echo "task size = $entry_list_length"

function is_busy {
    daemon_num=$(ps aux | grep -ie CassandraDaemon | grep java | wc -l)
    jps_num=$(jps | wc -l)
    if [ $daemon_num -gt 0 ] || [ $jps_num -gt 1 ] ; then
	echo "true"
    else
	echo "false"
    fi
}

function force_fill {
    ps aux | grep -ie CassandraDaemon | grep java | awk '{print $2}' | xargs kill -9 &> /dev/null
    jps | grep -v 'Jps' | awk '{print $1}' | xargs kill -9 &> /dev/null
}

force_fill
sleep 5
last_idle_time=$(date +%s)

while [ $entry_cursor -lt $entry_list_length ]
do
    if [ $(is_busy) == "true" ]; then
        echo "$container_id is busy"
        sleep 5
        # perform kill if busy for too long
        time_now=$(date +%s)
        time_waiting=$(( time_now - last_idle_time ))
        echo "WARN: time_waiting is $time_waiting seconds"
        if [ $time_waiting -gt 1500 ]; then
            force_fill
            echo "WARN: time_waiting is $time_waiting seconds > 2000s threshold. Perform force killing."
            sleep 10
        fi
    else
        # double check five times
        for dc in $(seq 1 5); do
            if [ $(is_busy) == "true" ]; then
                continue
    	    else
                sleep 0.1
            fi
        done

	echo "the host is not busy, assign entry $entry_cursor to it"
        last_idle_time=$(date +%s)

        echo ${entry_list[$entry_cursor]}
        force_fill
        sleep 2
        
        IFS=$' '
        "$ZEBRACONF_HOME"/runner/run_heter_conf_test.sh ${entry_list[$entry_cursor]}
	IFS=$'\n'

        force_fill
        sleep 2
        entry_cursor=$(( entry_cursor + 1 ))
    fi
done

# wait until the host is not busy
while [ "$(is_busy)" == "true" ]
do 
    sleep 10
done

echo "all tasks are finished now and the machine is idle"
