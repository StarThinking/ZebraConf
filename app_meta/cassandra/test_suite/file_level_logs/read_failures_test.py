cassandra read_failures_test.py true true
the_test is read_failures_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

read_failures_test.py::TestReadFailures::test_tombstone_failure_v3 
-------------------------------- live log call ---------------------------------
22:46:17,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:46:17,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:46:17,585 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:46:17,677 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:46:17,763 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:46:17,848 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:46:17,940 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:46:18,26 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:46:18,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
read_failures_test.py::TestReadFailures::test_tombstone_failure_v4 
-------------------------------- live log call ---------------------------------
22:46:40,191 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:46:40,279 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:46:40,347 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:46:40,439 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:46:40,524 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:46:40,591 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:46:40,683 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:46:40,768 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:46:40,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 66%]
read_failures_test.py::TestReadFailures::test_tombstone_failure_v5 
-------------------------------- live log call ---------------------------------
22:47:01,941 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:47:02,26 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:47:02,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:47:02,184 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:47:02,269 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:47:02,336 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:47:02,427 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:47:02,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:47:02,578 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_tombstone_failure_v3 passed 1 out of the required 1 times. Success!
test_tombstone_failure_v4 passed 1 out of the required 1 times. Success!
test_tombstone_failure_v5 passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 68.37 seconds ===========================
[msx] rc = 0
