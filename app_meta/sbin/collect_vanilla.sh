#!/bin/bash

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    ssh node-$i 'rm ~/reconf_test_gen/target/*; ~/parameter_test_controller/container_utility_sh/docker_fetch_result_by_key.sh .txt ~/reconf_test_gen/target/ ~/reconf_test_gen/target/' &
    pids[$i]=$!
done

for p in ${pids[@]}
do
    wait $p; echo "$p finished compressing and tranferring"
done
    
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do
    ssh node-$i "cd ~/reconf_test_gen/target/; tar zcvf $i.tar.gz *"
    scp node-$i:~/reconf_test_gen/target/$i.tar.gz ~/reconf_test_gen/target/
done
