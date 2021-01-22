#!/bin/bash

if [ $# -ne 2 ]; then echo 'wrong args'; exit -1; fi

IFS=$'\n'
log=$1
output=$2

rm total.txt can.txt cannot.txt conf_cannot_identify.txt conf_later_identify.txt conf_real_cannot_identify.txt 2> /dev/null
rm total_tmp.txt cannot_tmp.txt 2> /dev/null
#rm later.txt raw_cannot.txt raw_can.txt 2> /dev/null
#rm cannot.txt raw_can_with_later.txt can.txt 2> /dev/null
#rm total.txt 2> /dev/null

cat $log | grep 'cannot be identified when reading from' | awk '{print $NF}' | sort -u > conf_cannot_identify.txt
cat $log | grep 'later identified' | awk '{print $2}' | sort -u > conf_later_identify.txt

comm -23 conf_cannot_identify.txt conf_later_identify.txt > conf_real_cannot_identify.txt

cat $log | grep 'reading from' | awk '{print $2}' | sort -u > total_tmp.txt
# common
comm -12 total_tmp.txt ~/reconf_test_gen/all_xml_parameters.txt > total.txt

cat conf_real_cannot_identify.txt | while read line; do grep $line $log | grep 'reading from' | awk '{print $2}'; done | sort -u > cannot_tmp.txt
# common
comm -12 cannot_tmp.txt ~/reconf_test_gen/all_xml_parameters.txt > cannot.txt

comm -23 total.txt cannot.txt > can.txt

echo "$log can = $(cat can.txt | wc -l)"
echo "$log cannot = $(cat cannot.txt | wc -l)"
if [ $(cat total.txt | wc -l) -gt 0 ]; then
    echo "$log % can = $(echo "scale=2; $(cat can.txt | wc -l) * 100 / $(cat total.txt | wc -l)" | bc)"
fi

log_prefix=$(echo $log | awk -F '-component-meta.txt' '{print $1}')
if [ $output -eq 1 ]; then
    cat can.txt > "$log_prefix"-identify-can.txt
    cat cannot.txt > "$log_prefix"-identify-cannot.txt
fi

rm total.txt can.txt cannot.txt conf_cannot_identify.txt conf_later_identify.txt conf_real_cannot_identify.txt 2> /dev/null
