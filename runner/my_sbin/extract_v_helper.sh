#!/bin/bash

log=$1
if [ "$(cat $log | grep --text 'invalid value v')" == "" ]; then exit 0; fi

v_num=$(cat $log | grep --text 'invalid value v' | awk -F 'invalid value v' '{print $2}')
p=$(cat $log | grep --text 'h_list\[1\]' | awk -F '=' '{print $2}' | awk -F '@@@' '{print $1}')

if [ "$v_num" -eq 1 ]; then
    echo -n "$p "
    cat $log | grep --text 'h_list\[1\]' | awk -F '@@@' '{print $(NF-1)}'
elif [ "$v_num" -eq 2 ]; then
    echo -n "$p "
    cat $log | grep --text 'h_list\[1\]' | awk -F '@@@' '{print $NF}'
fi
