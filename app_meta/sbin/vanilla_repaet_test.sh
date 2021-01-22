#!/bin/bash

app='hadoop-tools'
running_time_expected=1800

function procedure {
    index=$1
    ~/parameter_test_controller/container_utility_sh/whole_cluster_clean.sh x0.0
    sleep 60
    ~/parameter_test_controller/container_utility_sh/whole_cluster_clean.sh x0.0
    sleep 60
    
    rm -fr ~/reconf_test_gen/target/*
    
    proj="$app"; for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do ssh node-$i "rm ~/nohup.txt; ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9; nohup ~/reconf_test_gen/dispatcher.sh $proj > nohup.txt &" & pids[$i]=$!; done; for p in ${pids[@]}; do wait $p; echo "$p is done"; done
    
    sleep $running_time_expected
    ~/reconf_test_gen/collect_vanilla.sh
    
    rm ~/reconf_test_gen/target/*.txt
    
    mkdir ~/reconf_test_gen/vanilla_error/tar_store/"$app""$index" 
    mv ~/reconf_test_gen/target/*.tar.gz  ~/reconf_test_gen/vanilla_error/tar_store/"$app""$index"
}

# remember to distribute tasks first here

for i in 1 2 3 4 5
do
    procedure $i
done
