#!/bin/bash

for test in $(cat $1); do echo $test; time ./run_pytest.sh cassandra $test false true &> tmp_pytest_logs/$test; done
