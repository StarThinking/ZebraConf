#!/bin/bash

if [ $# -ne 2 ]; then
    echo "./hypo_analysis.sh [file_prefix] [cf]..."
    exit -1
fi

classpath=/root/parameter_test_controller/target/:/root/parameter_test_controller/src/lib/commons-math3-3.6.1.jar

prefix=$1
hypo_files=$(find /root/parameter_test_controller/target/ -name *"_hypothesis_"* | grep -F "$prefix")

sum_v1v2_num=0
sum_v1v2_failed=0
sum_v1v1v2v2_num=0
sum_v1v1v2v2_failed=0

for hypo_file in ${hypo_files[@]} 
do 
    v1v2_num=$(grep 'v1v2 failed with probability' $hypo_file | awk -F ' ' '{print $8}')
    v1v2_failed=$(grep 'v1v2 failed with probability' $hypo_file | awk -F ' ' '{print $5}')
    v1v1v2v2_num=$(grep 'v1v1v2v2 failed with probability' $hypo_file | awk -F ' ' '{print $8}')
    v1v1v2v2_failed=$(grep 'v1v1v2v2 failed with probability' $hypo_file | awk -F ' ' '{print $5}')
    sum_v1v2_num=$(( sum_v1v2_num + v1v2_num )) 
    sum_v1v2_failed=$(( sum_v1v2_failed + v1v2_failed ))
    sum_v1v1v2v2_num=$(( sum_v1v1v2v2_num + v1v1v2v2_num ))
    sum_v1v1v2v2_failed=$(( sum_v1v1v2v2_failed + v1v1v2v2_failed ))
done

echo "sum_v1v2_num: $sum_v1v2_num"
echo "sum_v1v2_failed: $sum_v1v2_failed"
echo "sum_v1v1v2v2_num: $sum_v1v1v2v2_num"
echo "sum_v1v1v2v2_failed: $sum_v1v1v2v2_failed"

if [ $sum_v1v1v2v2_failed -gt $sum_v1v2_failed ]; then
    echo 'v1v1v2v2 failed more';
    exit 0;
fi

cf=$2
output=$(java -cp $classpath HypoAnalysis $sum_v1v2_num $sum_v1v2_failed $sum_v1v1v2v2_num $sum_v1v1v2v2_failed $cf)
echo $output
#if [ "$output" == "null_hypothesis is false" ]; then
#    echo "$hypo_file"    
#    print_data
#fi

