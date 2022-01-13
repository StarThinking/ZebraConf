#!/bin/bash

for test in $(cat cassandra/test_suite/all_test_func_level.txt); do echo $test; time ./run_pytest.sh cassandra $test true true &> tmp_pytest_log/$test; ps aux | grep -ie CassandraDaemon | grep java | awk '{print $2}' | xargs kill; sleep 60; done
