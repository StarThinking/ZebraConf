#!/bin/bash

file_name=$1
proj=$2

for i in $(cat $file_name); do /root/reconf_test_gen/run_mvn_test.sh $proj $i /root/reconf_test_gen/target/; done
