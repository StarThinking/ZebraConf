#!/bin/bash

for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n)
do 
    finished=$(ssh node-$i "cat ~/nohup.txt | grep assign | wc -l")
    all=$(ssh node-$i "cat nohup.txt | head -n 1" | awk '{print $NF}')
    ratio=$(echo "scale=2; $finished / $all" | bc)
    echo "$finished out of $all are finished $ratio"
done
