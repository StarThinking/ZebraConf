#!/bin/bash

for test in $(cat cassandra/test_suite/all_test_func_level.txt); do echo $test; time ./run_pytest.sh cassandra $test false true &> tmp_pytest_logs/$test; done
