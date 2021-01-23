#!/bin/bash

if [ $# -ne 1 ]; then echo 'wrong arguments, exit'; exit -1; fi

para=$1
find . -name ultimate | while read line; do grep -rn ^"$para " $line; done | awk '{print $NF}' | sort | uniq -c
