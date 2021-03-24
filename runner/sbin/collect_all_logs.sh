#!/bin/bash

if [ $# -ne 1 ]; then echo '[new_dir]'; exit -1; fi

# kill auto_update_white_list.sh before collect all
ps aux | grep auto_update_white_list.sh | awk '{print $2}' | xargs kill -9

~/vm_images/ZebraConf/runner/sbin/collect_combine_run.sh
rm mv ~/vm_images/ZebraConf/runner/log/*txt
mv ~/vm_images/ZebraConf/runner/log ~/vm_images/ZebraConf/runner/log_combine

~/vm_images/ZebraConf/runner/sbin/collect_hypothesis.sh
rm mv ~/vm_images/ZebraConf/runner/log/*txt
mv ~/vm_images/ZebraConf/runner/log ~/vm_images/ZebraConf/runner/log_hypothesis

~/vm_images/ZebraConf/runner/sbin/collect_single_run.sh
rm mv ~/vm_images/ZebraConf/runner/log/*txt
mv ~/vm_images/ZebraConf/runner/log ~/vm_images/ZebraConf/runner/log_collect_combine

mkdir ~/vm_images/ZebraConf/runner/"$1"
mv ~/vm_images/ZebraConf/runner/log_* ~/vm_images/ZebraConf/runner/"$1" 


