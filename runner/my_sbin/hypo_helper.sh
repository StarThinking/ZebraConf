#!/bin/bash

source ~/.profile

if [ $# -ne 1 ]; then
    echo "./hypo_helper.sh [hypo_log_dir]"
    exit -1
fi

hypo_log_dir=$1
result_dir=./with_confidence
confidence=0.999
clean_flag=1

rm -rf $result_dir
mkdir $result_dir

for i in $hypo_log_dir/*.txt
do
    $ZEBRACONF_HOME/runner/my_sbin/hypo_analysis.sh $i $confidence $clean_flag
done | while read j; do cp $j $result_dir; done

extract=$ZEBRACONF_HOME/runner/my_sbin/extract_utility.sh

cd $result_dir
for i in *
do 
    p_and_c="$($extract $i 'para')@@@$($extract $i 'comp')"
    if [ ! -d $p_and_c ]; then 
	mkdir $p_and_c
    fi
    mv $i $p_and_c
done
