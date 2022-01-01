cassandra pending_range_test.py true true
the_test is pending_range_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

pending_range_test.py::TestPendingRangeMovements::test_pending_range 
-------------------------------- live log call ---------------------------------
08:25:28,149 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:25:28,236 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:25:28,237 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:28,304 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:25:28,304 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:28,395 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:25:28,480 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:25:28,480 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:28,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:25:28,545 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:28,636 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:25:28,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:25:28,721 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:28,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:25:28,786 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:28,876 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:25:28,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
08:25:28,961 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:29,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
08:25:29,27 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:29,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:25:29,202 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
08:25:29,202 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:25:29,267 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
08:25:29,267 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:26:17,574 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
08:26:18,686 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:26:20,593 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:26:24,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:26:31,360 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_pending_range passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 64.77 seconds ===========================
[msx] rc = 0
