#!/bin/bash

if [ $# -ne 2 ]; then echo wrong; exit -1; fi
tag=$1
vms=$2

for i in $(seq 0 $vms); do docker run -d -it --name hadoop-$i sixiangma/reconf_parameter:$tag ; done
