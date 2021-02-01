#!/bin/bash

log=$1

# we do not generate meta files if a test doesn't contain msx-reconfagent
#if [ "$(cat $log | grep "msx-reconfagent" | grep "performReconf")" == "" ]; then echo 'no init'; exit 0; fi

test_name=$(echo $log | awk -F '-output.txt' '{print $1}')
grep msx $log | grep -v 'msx-get' | sort -u > "$test_name"-component-meta.txt

grep msx $log | grep 'msx-get' | awk -F 'msx-get ' '{print $2}' | sort -u > "$test_name"-parameter-meta.txt

cat "$test_name"-parameter-meta.txt | awk '{print $1" "$2" "$3}' | sort -u > "$test_name"-ultimate-meta.txt
