#!/bin/bash

if [ $# -ne 2 ]; then echo 'wrong: [proj] [xml]'; exit -1; fi

proj=$1
xml=$2
get_store_dir='/root/reconf_test_gen/soot_study/component_parameter_analysis'

for p in $(java -cp /root/reconf_test_gen/ ReadXMLFile "$xml" getNoDefaultValueParameters)
do 
    if [ "$(grep -r ^"$p"$ "$get_store_dir"/"$proj"/get/)" == "" ]; then 
	echo $p
    fi
done
