#!/bin/bash

ut_time=$(cat $1 | grep 'Time elapsed' | head -n 1 | awk -F 'Time elapsed: ' '{print $2}' | awk '{print $1}')
total_time_raw=$(cat $1 | grep 'Total time' | head -n 1  | awk '{print $(NF-1)}')

if [ "$ut_time" == "" ] || [ "$total_time_raw" == "" ]; then
    #echo "invalid input: ut_time = $ut_time, total_time_raw = $total_time_raw"
    exit 0
fi

# convert min:sec
if [ "$(echo $total_time_raw | grep ':')" != "" ]; then
    total_time=$(echo "$(echo $total_time_raw | awk -F ':' '{print $1}') * 60 + $(echo $total_time_raw | awk -F ':' '{print $2}')" | bc)
    #echo "total_time_raw = $total_time_raw"
    #echo "total_time 1 = $total_time"
else
    #echo "total_time 2 = $total_time_raw"
    total_time=$total_time_raw
fi
echo "$ut_time $total_time"
