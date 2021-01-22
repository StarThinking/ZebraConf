#!/bin/bash

proj=$1
type=$2 # run or total
if [ "$type" == "run" ]; then
    cat "$proj".txt | awk '{print $1}' | awk '{s+=$1} END {printf "%.0f\n", s}'
else
    cat "$proj".txt | awk '{print $2}' | awk '{s+=$1} END {printf "%.0f\n", s}'
fi
