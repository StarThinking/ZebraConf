#!/bin/bash

if [ $# -lt 3 ]; then
    echo "./run_heter_conf_test.sh [suite] [u_test] [[para@@@component@@@point@@@v1@@@v2]%%%[...]]"
    exit -1
fi

# disable conf tracking
echo 'false' > /root/ZebraConf/app_meta/lib/enable

# create log if not existed
#if [ ! -d /root/ZebraConf/runner/log ]; then mkdir /root/ZebraConf/runner/log; fi

proj=$1
u_test=$2
shift 2
hypo_max_repeats=30
LOG_TIME="$(($(date +%s%N)/1000000))"

function filter_with_white_list {
    local str="$@"
    for p_c in $(cat /root/ZebraConf/runner/white_list.txt)
    do
        str=$(echo "$str" | awk -F ' ' '{for(i=1; i<=NF; i++) {print $i}}' | grep -v "$p_c" | tr '\n' ' ')
    done
    echo "$str"
}

# argument $@ is h_list: "para,component,point,v1,v2 para,component,point,v1,v2"
function test_procedure {   
    local conbime_type=""
    #local OLDIFS=$IFS
    #local task_array=()
    #IFS='%%%' read -ra task_array <<< "$@"
    #IFS=$OLDIFS
    local task_array="$(echo "$@" | awk -F '%%%' '{for(i=1; i<=NF; i++) {print $i}}' | tr '\n' ' ')"
    local task_array="$(filter_with_white_list "$task_array")"
    local h_list_size=$(echo "$task_array" | awk '{print NF}')
    echo ""
    echo ">>>>>>>> test_procedure -- $h_list_size parameters -- after filtering white list: $(echo "$task_array" | awk -F '@@@| ' '{for (i=1;i<=NF;i+=5) print $i}' | tr "\n" " ")"
    echo ">>>>>>>> $task_array"

    if [ $h_list_size -eq 1 ]; then
        conbime_type="single"
    elif [ $h_list_size -ge 2 ]; then
        conbime_type="combine"
    elif [ $h_list_size -eq 0 ]; then
        echo "hlist size is 0, bye bye."
        return 0
    fi
   
    echo "";
    echo ">>>>>>>> running $conbime_type run_test for $(echo "$task_array" | awk -F '@@@| ' '{for (i=1;i<=NF;i+=5) print $i}' | tr "\n" " ")"
    java -cp /root/ZebraConf/runner/target/ HConfRunner $h_list_size 'run' $proj $u_test "$(echo "$task_array" | awk  -F ' ' '{for (i=1;i<=NF;i++) if (i != NF) {printf "%s", $i"%%%"} else printf "%s", $i}')" > /root/ZebraConf/runner/log/"$proj.$u_test.$LOG_TIME."$conbime_type"_run_$RANDOM$RANDOM.txt"
    local run_rc=$?
    echo "run_rc is $run_rc"
    if [ $run_rc -eq 0 ]; then
        echo "no issue, bye bye."
        return 0
    else
        if [ $conbime_type == "single" ] ; then
            echo "";
            echo ">>>>>>>> running $conbime_type hypo_test for $(echo "$task_array" | awk -F '@@@| ' '{for (i=1;i<=NF;i+=5) print $i}' | tr "\n" " ")"
            java -cp /root/ZebraConf/runner/target/ HConfRunner $h_list_size 'hypothesis' $proj $u_test "$(echo "$task_array" | awk  -F ' ' '{for (i=1;i<=NF;i++) if (i != NF) {printf "%s", $i"%%%"} else printf "%s", $i}')" > /root/ZebraConf/runner/log/"$proj.$u_test.$LOG_TIME."$conbime_type"_hypothesis_$RANDOM$RANDOM.txt"
            return 0
        else
            local half_index=$(( h_list_size / 2))
            echo "half_index = $half_index"
            local first_tasks=$(echo "$task_array" | awk -v first_end="$half_index" -F ' ' '{for (i=1;i<=first_end;i++) if (i != first_end) {printf "%s", $i"%%%"} else printf "%s", $i}')
            local second_tasks=$(echo "$task_array" | awk -v first_end="$half_index" -v second_end="$h_list_size" -F ' ' '{for (i=first_end+1;i<=second_end;i++) if (i != second_end) {printf "%s", $i"%%%"} else printf "%s", $i}')
            echo "first_half = $first_tasks"
            echo "second_half = $second_tasks"
            #| awk '{for(i=0;i<2;i++) print $i}'
            
            test_procedure $first_tasks
            test_procedure $second_tasks
        fi
    fi
}

test_procedure $@
#echo "test_procedure returns $?"
