#!/bin/bash

if [ $# -ne 2 ]; then
    echo "./hypo_analysis_wrapper.sh [hypo.txt] [confidence]"
    exit -1
fi

hypo_file=$1
confidence=$2
clean_sheet_enable=$3

v1v2_failed=$(grep 'v1v2 failed with probability' $hypo_file | awk -F ' ' '{print $5}')
v1v2_num=$(grep 'v1v2 failed with probability' $hypo_file | awk -F ' ' '{print $8}')
v1v1v2v2_failed=$(grep 'v1v1v2v2 failed with probability' $hypo_file | awk -F ' ' '{print $5}')
v1v1v2v2_num=$(grep 'v1v1v2v2 failed with probability' $hypo_file | awk -F ' ' '{print $8}')

function print_data {
    echo "v1v2_num: $v1v2_num"
    echo "v1v2_failed: $v1v2_failed"
    echo "v1v1v2v2_num: $v1v1v2v2_num"
    echo "v1v1v2v2_failed: $v1v1v2v2_failed"
}

if [ $v1v1v2v2_failed -gt $v1v2_failed ]; then
    #echo 'v1v1v2v2 failed more';
    exit 0; 
fi

classpath=~/ZebraConf/runner/target/:~/ZebraConf/runner/lib/commons-math3-3.6.1.jar
output=$(java -cp $classpath HypoAnalysis $v1v2_num $v1v2_failed $v1v1v2v2_num $v1v1v2v2_failed $confidence)
if [ "$output" == "null_hypothesis is false" ]; then
    echo "might be a real problem!"
else
    echo "not a real problem."
fi

