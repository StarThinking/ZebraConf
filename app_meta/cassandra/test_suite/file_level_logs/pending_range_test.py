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
22:29:39,80 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:29:39,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:29:39,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:29:39,327 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:29:39,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:29:39,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:29:39,568 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:29:39,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:29:39,718 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:29:39,809 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:29:39,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
22:29:39,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
22:29:40,50 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:29:40,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
22:29:40,200 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
22:30:29,615 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
22:30:30,630 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
22:30:32,941 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
22:30:37,160 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_pending_range passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 65.01 seconds ===========================
[msx] rc = 0
