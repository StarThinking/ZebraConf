#!/bin/bash
date 
vm_num=$(( $(cat /proc/cpuinfo | grep 'processor' | wc -l) / 2 ))
if [ $vm_num -gt 20 ]; then vm_num=10; fi
vm_num=10
vm_num=$(( vm_num -1 ))
IFS=$'\n' 
entry_list=( $(cat /root/parameter_test_controller/task.txt) )
entry_list_length=${#entry_list[@]}
entry_cursor=0
echo entry_list_length = $entry_list_length
cmd='echo /root/parameter_test_controller/procedure.sh ${entry_list[$entry_cursor]}'

function is_busy {
    i=$1
    jps_num=$(docker exec hadoop-$i bash -c "jps" | wc -l)
    disp_num=$(docker exec hadoop-$i bash -c "ps -ef | grep procedure.sh" | wc -l)
    #sh_num=$(docker exec hadoop-$i bash -c "ps aux | grep run_mvn_test.sh" | wc -l)
    if [ $disp_num -gt 2 ] || [ $jps_num -gt 1 ] ; then
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
	    # double check
	    for dc in 1 2 3 4 5; do
	        if [ "$(is_busy $i)" == "true" ]; then
		    continue
		fi
	    	sleep 0.1
            done
	    echo hadoop-$i is not busy, assign entry $entry_cursor to it
	    docker exec -d hadoop-$i bash -c "$(eval $cmd)"
	    entry_cursor=$(( entry_cursor + 1 ))
	    if [ $entry_cursor -ge $entry_list_length ]; then echo finish all tasks; break; fi
	fi
    done
done

for i in $(seq 0 $vm_num)
do
    while [ "$(is_busy $i)" == "true" ]; do sleep 10; done
done

echo all nodes are unbusy now
date
