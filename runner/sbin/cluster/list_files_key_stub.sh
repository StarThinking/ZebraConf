#!/bin/bash

if [ $# -ne 2 ]; then echo 'wrong: num key '; exit -1; fi

num=$1
key=$2

cd ~/parameter_test_controller
for i in dfs*.txt
do
    if [ "$(grep "$key" $i)" != "" ]; then
        echo $i
    fi
done
