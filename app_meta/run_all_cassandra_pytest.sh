#!/bin/bash

source ~/.profile

rm -rf "$ZEBRACONF_HOME"/app_meta/tmp_pytest_logs 
mkdir "$ZEBRACONF_HOME"/app_meta/tmp_pytest_logs 
echo none > "$ZEBRACONF_HOME"/runner/shared/reconf_vvmode

for test in $(cat "$ZEBRACONF_HOME"/runner/task.txt)
do
    echo $test
    time "$ZEBRACONF_HOME"/app_meta/run_pytest.sh cassandra $test false true &> "$ZEBRACONF_HOME"/app_meta/tmp_pytest_logs/$test
done
