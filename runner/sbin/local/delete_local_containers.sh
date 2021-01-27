#!/bin/bash

docker container list -a | awk '{print $NF}' | grep -v NAMES | while read i; do docker container stop $i; docker container rm $i; done
