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
08:42:02,818 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:02,905 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:42:02,905 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:02,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:42:02,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:03,62 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:03,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:42:03,148 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:03,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:42:03,214 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:03,304 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:03,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:42:03,389 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:03,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:42:03,455 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
read_failures_test.py::TestReadFailures::test_tombstone_failure_v4 
-------------------------------- live log call ---------------------------------
08:42:24,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:24,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:42:24,909 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:24,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:42:24,975 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:25,77 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:25,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:42:25,163 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:25,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:42:25,229 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:25,319 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:25,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:42:25,405 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:25,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:42:25,471 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
read_failures_test.py::TestReadFailures::test_tombstone_failure_v5 
-------------------------------- live log call ---------------------------------
08:42:46,571 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:46,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:42:46,662 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:46,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:42:46,731 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:46,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:46,911 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:42:46,911 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:46,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:42:46,979 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:47,72 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:42:47,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:42:47,158 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:42:47,227 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:42:47,227 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_tombstone_failure_v3 passed 1 out of the required 1 times. Success!
test_tombstone_failure_v4 passed 1 out of the required 1 times. Success!
test_tombstone_failure_v5 passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 66.35 seconds ===========================
[msx] rc = 0
