#!/bin/bash

while read i
do
    echo $i | grep -v "\.port"$
done
