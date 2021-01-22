#!/bin/bash

~/parameter_test_controller/container_utility_sh/filter_fetch.sh single_hypothesis

cd ~/parameter_test_controller/target/
for i in *.tar.gz; do tar zxvf $i; rm $i; done; mkdir single_hypothesis; find -maxdepth 2 -name '*single_hypothesis_*' | xargs mv -t single_hypothesis; cd single_hypothesis; ~/parameter_test_controller/just_compile.sh; mkdir no_need_hypo/; cf=0.9999; for hlog in *_hypothesis_*; do ~/parameter_test_controller/hypo_analysis.sh $hlog $cf 1; done | while read line; do mv $line no_need_hypo/; done

cd no_need_hypo/
for i in *_hypothesis_*; do cat $i | head -n 3 | tail -n 1; done | sort | awk -F ' |@@@' '{print $2"@@@"$3}' > ~/my_white_list.txt
