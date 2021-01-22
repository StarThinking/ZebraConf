#!/bin/bash

dir=$1

#mkdir invalid_$dir
for i in $dir/*
do
    if [ "$(grep 'invalid value' $i)" != "" ]; then
	identifier=$(cat $i | grep 'invalid value' | awk '{print $NF}')
        proj=$(cat $i | head -n 1 | tail -n 1 | awk '{print $2}')
        u_test=$(cat $i | head -n 2 | tail -n 1 | awk '{print $2}')
        h_list="$(cat $i | head -n 3 | tail -n 1 | awk '{print $2}')"
	para="$(echo $h_list | awk -F '@@@' '{print $1}')"
	v1="$(echo $h_list | awk -F '@@@' '{print $4}')"
	v2="$(echo $h_list | awk -F '@@@' '{print $5}')"
	#echo "$proj $u_test $v1 $v2 $identifier"
        if [ "$identifier" == "v1" ]; then
	    echo "$proj $u_test $para $v1"
	fi
        if [ "$identifier" == "v2" ]; then
	    echo "$proj $u_test $para $v2"
	fi
    fi
done
