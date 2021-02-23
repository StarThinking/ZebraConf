#!/bin/bash

# filtering
cat tuples_per_para/* | grep -v 'unidentifiable' | grep -v 'unit_test' > tuples_per_para.txt

# convert into per test view
mkdir tuples_per_test
cat tuples_per_para.txt | awk '{print $2" "$3}' | sort -u | while read line; do grep -F " $line " tuples_per_para.txt | awk '{print $2" "$3" "$1" "$4" "$5" "$6" "$7}' > tuples_per_test/"$line".txt ; done

# grouping
cd tuples_per_test
mkdir ../grouped
IFS=$'\n'
for i in *
do 
    echo "grouping for test $i"
    java -cp ~/ZebraConf/test_gen GroupTuple "$i" 100 > ../grouped/"$i"
done
