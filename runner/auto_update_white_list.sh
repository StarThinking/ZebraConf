#!/bin/bash

~/vm_images/ZebraConf/runner/sbin/build_local.sh 
rm nohup.out

while true
do
    ~/vm_images/ZebraConf/runner/sbin/collect_hypothesis.sh
    sleep 2
    cd ~/vm_images/ZebraConf/runner/log
    rm *txt; for i in *; do tar zxvf $i; rm $i; done; mkdir no_need_hypo/; cf=0.9999; for hlog in *_hypothesis_*; do ~/vm_images/ZebraConf/runner/sbin/hypo_analysis.sh $hlog $cf 1; done | while read line; do mv $line no_need_hypo/; done; cd no_need_hypo; for i in *; do p_and_c="$(~/vm_images/ZebraConf/runner/sbin/extract_utility.sh $i 'para')@@@$(~/vm_images/ZebraConf/runner/sbin/extract_utility.sh $i 'comp')"; if [ ! -d $p_and_c ]; then mkdir $p_and_c; fi; mv $i $p_and_c; done

    mv ~/vm_images/ZebraConf/runner/white_list.txt ~/vm_images/ZebraConf/runner/white_list.txt.old
    for i in *; do if [ $(ls $i | wc -l) -gt 1 ]; then echo $i; fi; done > ~/vm_images/ZebraConf/runner/white_list.txt.increm
    cat ~/vm_images/ZebraConf/runner/white_list.txt.old ~/vm_images/ZebraConf/runner/white_list.txt.increm | sort -u > ~/vm_images/ZebraConf/runner/white_list.txt
    ~/vm_images/ZebraConf/runner/sbin/update_cluster_white_list.sh ~/vm_images/ZebraConf/runner/white_list.txt
    sleep 600
done
