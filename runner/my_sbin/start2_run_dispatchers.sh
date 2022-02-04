#!/bin/bash

for i in $(seq 0 4); do docker exec -d container-$i bash -c '/root/vm_images/ZebraConf/runner/my_sbin/dispatcher.sh &> /root/vm_images/ZebraConf/runner/nohup.txt'; done
