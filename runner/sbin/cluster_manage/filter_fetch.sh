#!/bin/bash

if [ $# -ne 1 ]; then echo 'wrong'; exit 1; fi

key=$1
pids=()
rm -rf ~/parameter_test_controller/target/*
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do ssh node-$i "find ~/parameter_test_controller/target/ -type f -maxdepth 1 -name '*' | xargs rm; ~/parameter_test_controller/container_utility_sh/docker_fetch_result_by_key.sh $key /root/parameter_test_controller/target/ /root/parameter_test_controller/target/; cd /root/parameter_test_controller/; rm -rf target.$i; cp -r target target.$i; tar zcvf $i.tar.gz target.$i; rm -rf target.$i" & pids+=($!); done; for id in ${pids[@]}; do wait $id; echo "pid $id finished"; done; for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do scp node-$i:~/parameter_test_controller/$i.tar.gz ~/parameter_test_controller/target/; ssh node-$i "rm ~/parameter_test_controller/$i.tar.gz"; done; find ~/parameter_test_controller/target/ -maxdepth 1 -name '*txt*' | xargs rm ; find ~/parameter_test_controller/target/ -maxdepth 1 -name '*.class' | xargs rm
