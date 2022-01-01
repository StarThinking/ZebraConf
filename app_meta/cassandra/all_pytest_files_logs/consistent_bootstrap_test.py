cassandra consistent_bootstrap_test.py true true
the_test is consistent_bootstrap_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

consistent_bootstrap_test.py::TestBootstrapConsistency::test_consistent_reads_after_move 
-------------------------------- live log call ---------------------------------
04:04:26,722 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:04:26,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:04:26,808 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:04:26,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:04:26,877 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:04:26,966 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:04:27,51 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:04:27,51 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:04:27,117 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:04:27,117 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:04:27,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:04:27,290 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:04:27,291 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:04:27,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:04:27,356 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:04:47,465 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
04:04:48,472 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:04:50,479 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:04:54,391 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:05:01,524 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
consistent_bootstrap_test.py::TestBootstrapConsistency::test_consistent_reads_after_bootstrap 
-------------------------------- live log call ---------------------------------
04:05:52,737 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:05:52,823 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:05:52,823 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:05:52,889 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:05:52,889 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:05:52,979 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:05:53,64 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:05:53,64 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:05:53,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:05:53,130 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:06:11,624 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
04:06:12,731 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:06:14,537 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:06:19,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:06:26,284 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:06:33,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:06:33,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:06:33,844 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:06:33,921 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:06:33,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_consistent_reads_after_move passed 1 out of the required 1 times. Success!
test_consistent_reads_after_bootstrap passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 210.71 seconds ==========================
[msx] rc = 0
