#!/bin/bash

if [ $# -ne 1 ]; then echo 'ERROR: ./dispatcher.sh [project]'; exit -1; fi

the_project=$1
vm_num=$(( $(cat /proc/cpuinfo | grep 'processor' | wc -l) / 2 ))
if [ $vm_num -gt 20 ]; then vm_num=20; fi
vm_num=10
vm_num=$(( vm_num -1 ))
busy_file=/tmp/reconf_busy
dst='/root/reconf_test_gen/target/'
IFS=$'\n' 
entry_list=( $(cat /root/reconf_test_gen/task.txt) )
entry_list_length=${#entry_list[@]}
entry_cursor=0
echo entry_list_length = $entry_list_length
cmd='echo /root/reconf_test_gen/run_mvn_test.sh $the_project ${entry_list[$entry_cursor]} $dst'

function is_busy {
    i=$1
    jps_num=$(docker exec hadoop-$i bash -c "jps" | wc -l)
    #sh_num=$(docker exec hadoop-$i bash -c "ps aux | grep run_mvn_test.sh" | wc -l)
    if [ $jps_num -gt 1 ] ; then
	echo "true"
    else
	echo "false"
    fi
}

while [ $entry_cursor -lt $entry_list_length ]
do
    for i in $(seq 0 $vm_num)
    do
        if [ "$(is_busy $i)" == "true" ]; then
	     echo hadoop-$i is busy
	else
	    echo hadoop-$i is not busy, assign entry $entry_cursor to it
	    docker exec -d hadoop-$i bash -c "$(eval $cmd)"
	    entry_cursor=$(( entry_cursor + 1 ))
	    if [ $entry_cursor -ge $entry_list_length ]; then echo finish all tasks; break; fi
	fi
    done
    sleep 1
done

for i in $(seq 0 $vm_num)
do
    while [ "$(is_busy $i)" == "true" ]; do sleep 10; done
done

echo all nodes are unbusy now
