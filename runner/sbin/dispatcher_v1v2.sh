#!/bin/bash

if [ $# -ne 0 ]; then echo 'ERROR: ./dispatcher_v1v2.sh'; exit -1; fi

the_project=''
the_h_list=''
the_test=''
busy_file=/tmp/reconf_busy
IFS=$'\n' 
entry_list=( $(cat /root/vm_images/ZebraConf/runner/task.txt) )
entry_list_length=${#entry_list[@]}
entry_cursor=0
echo "task size = $entry_list_length"
cmd='echo /root/ZebraConf/app_meta/run_mvn_test.sh $the_project $the_test false true'

function is_busy {
    con_id=$1
    jps_num=$(docker exec hadoop-$con_id bash -c "jps" | wc -l)
    if [ $jps_num -gt 1 ]; then
	echo "true"
    else
	echo "false"
    fi
}

max_id=$(( $(docker container list -a | awk '{print $NF}' | grep -v NAMES | wc -l) - 1 ))
while [ $entry_cursor -lt $entry_list_length ]
do
    for container_id in $(seq 0 $max_id)
    do
        if [ "$(is_busy $container_id)" == "true" ]; then
	     echo "$container_id is busy"
	else
            # double check
	    quit_busy=0
            for dc in 1 2 3 4 5; do
                if [ "$(is_busy $container_id)" == "true" ]; then
		    quit_busy=1
                    break
		else
	            sleep 0.1
                fi
            done
	    if [ $quit_busy -eq 1 ]; then 
		continue
	    fi
	    echo "$container_id is not busy, assign entry $entry_cursor to it"
            the_project=$(echo ${entry_list[$entry_cursor]} | awk '{print $1}')
            the_test=$(echo ${entry_list[$entry_cursor]} | awk '{print $2}')
            the_h_list=$(echo ${entry_list[$entry_cursor]} | awk '{print $3}')
	    docker exec -d hadoop-$container_id bash -c "echo v1v2 > /root/ZebraConf/runner/shared/reconf_vvmode"
	    docker exec -d hadoop-$container_id bash -c "echo $the_h_list > /root/ZebraConf/runner/shared/reconf_h_list"
	    docker exec -d hadoop-$container_id bash -c "$(eval $cmd)"
	    entry_cursor=$(( entry_cursor + 1 ))
	    if [ $entry_cursor -ge $entry_list_length ]; then 
		echo finish all tasks
		break
	    fi
	fi
    done
    sleep 1
done

# wait until all containers are not busy
for container_id in $(seq 0 $max_id)
do
    while [ "$(is_busy $container_id)" == "true" ]
    do 
        sleep 10
    done
done

echo "all nodes are unbusy now"
