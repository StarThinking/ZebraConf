#!/bin/bash

if [ $# -ne 1 ]; then echo 'ERROR: ./dispatcher.sh [project]'; exit -1; fi

the_project=$1
busy_file=/tmp/reconf_busy
IFS=$'\n' 
entry_list=( $(cat /root/vm_images/ZebraConf/app_meta/task.txt) )
entry_list_length=${#entry_list[@]}
entry_cursor=0
echo "task size = $entry_list_length"
cmd='echo /root/ZebraConf/app_meta/run_mvn_test.sh $the_project ${entry_list[$entry_cursor]}'

function is_busy {
    my_con=$1
    jps_num=$(docker exec $my_con bash -c "jps" | wc -l)
    if [ $jps_num -gt 1 ]; then
	echo "true"
    else
	echo "false"
    fi
}

while [ $entry_cursor -lt $entry_list_length ]
do
    for my_container in $(docker container list -a | awk '{print $NF}' | grep -v NAMES)
    do
        if [ "$(is_busy $my_container)" == "true" ]; then
	     echo "$my_container is busy"
	else
            # double check
            for dc in 1 2 3 4 5; do
                if [ "$(is_busy $my_container)" == "true" ]; then
                    continue
                fi
            done
	    echo "$my_container is not busy, assign entry $entry_cursor to it"
	    docker exec -d $my_container bash -c "$(eval $cmd)"
	    entry_cursor=$(( entry_cursor + 1 ))
	    if [ $entry_cursor -ge $entry_list_length ]; then echo finish all tasks; break; fi
	fi
    done
    sleep 1
done

# wait until all containers are not busy
for my_container in $(docker container list -a | awk '{print $NF}' | grep -v NAMES)
do
    while [ "$(is_busy $my_container)" == "true" ]
    do 
        sleep 10
    done
done

echo "all nodes are unbusy now"
