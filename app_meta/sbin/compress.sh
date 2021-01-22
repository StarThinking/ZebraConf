#!/bin/bash

log=$1

# we do not generate meta files if a test doesn't contain msx-reconfagent
#if [ "$(cat $log | grep "msx-reconfagent" | grep "performReconf")" == "" ]; then echo 'no init'; exit 0; fi

prefix=$(echo $log | awk -F '-output.txt' '{print $1}')
grep msx $log | grep -v 'msx-get' | sort -u > "$prefix"-component-meta.txt

grep msx $log | grep 'msx-get' | awk -F 'msx-get ' '{print $2}' | sort -u > "$prefix"-parameter-meta.txt

cat "$prefix"-parameter-meta.txt | awk '{print $1" "$2" "$3}' | sort -u > "$prefix"-ultimate-meta.txt
