#!/bin/bash

if [ $# -ne 1 ]; then echo './check_thread_consistency.sh [log]'; exit -1; fi
log=$1
TMP_OUTPUT=/root/my_check_thread_consistency.tmp.txt
rm $TMP_OUTPUT &> /dev/null
cat $log | grep 'get-return' | grep -v 'thread is 1'$ | sort -u | awk '{print $NF" "$4" "$5}' | sort -u > $TMP_OUTPUT
cat $TMP_OUTPUT | awk '{print $1}' | sort -u | while read tid; do if [ $(grep "$tid " $TMP_OUTPUT | wc -l) -gt 1 ]; then echo "warning! thread $tid has multiple value"; fi; done
