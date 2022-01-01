#!/bin/bash
for test in $(cat cassandra/all_pytest.txt); do echo $test; time ./run_pytest.sh cassandra $test true true &> pytest_logs/$test; ps aux | grep -ie CassandraDaemon | grep java | awk '{print $2}' | xargs kill; sleep 60; done
