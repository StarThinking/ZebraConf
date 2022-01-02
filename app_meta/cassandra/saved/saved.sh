# under all_pytest_files_logs, print the smallest level pytest
grep '.py::' * | grep -v SKIPPED | awk -F ':' '{print $2"::"$4"::"$6}'

# run tests
for test in $(cat cassandra/all_pytest.txt); do echo $test; time ./run_pytest.sh cassandra $test true true &> pytest_logs/$test; ps aux | grep -ie CassandraDaemon | grep java | awk '{print $2}' | xargs kill; sleep 60; done
