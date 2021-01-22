#!/bin/bash

if [ $# -ne 2 ]; then echo wrong; exit -1; fi
num=$1
tag=$2

for i in $(seq 0 $num); do docker run -d -it --name hadoop-$i sixiangma/reconf_parameter:$tag ; done
