#!/bin/bash

for i in $(seq 0 4); do docker exec -d container-$i bash -c '/root/vm_images/ZebraConf/app_meta/run_all_cassandra_pytest.sh &> /root/vm_images/ZebraConf/app_meta/nohup.txt'; done
