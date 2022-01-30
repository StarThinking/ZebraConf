#!/bin/bash

for i in $(seq 0 4); do last="$(docker exec container-$i bash -c 'cat /root/vm_images/ZebraConf/runner/nohup.txt' | grep 'assign entry' | tail -n 1 | awk '{print $(NF - 2)}')"; echo "$i: $last"; done
