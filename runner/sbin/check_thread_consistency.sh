#!/bin/bash

if [ $# -ne 1 ]; then echo './check_thread_consistency.sh [log]'; exit -1; fi
log=$1
TMP_OUTPUT=/root/my_check_thread_consistency.tmp.txt
rm $TMP_OUTPUT &> /dev/null
cat $log | grep 'msx-confcontroller get-return' | sort -u | awk '{print $NF" "$(NF-3)" "$4" "$5}' | sort -u > $TMP_OUTPUT
cat $TMP_OUTPUT
cat $TMP_OUTPUT | awk -F ',' '{print $1}' | sort -u | while read tid; do if [ $(grep "$tid " $TMP_OUTPUT | wc -l) -gt 1 ]; then echo "warning! thread $tid has multiple value"; fi; done
