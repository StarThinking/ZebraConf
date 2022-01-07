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
18:04:18,989 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:04:19,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:04:19,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:04:19,232 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:04:19,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:04:19,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:04:19,473 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:04:19,557 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:04:19,623 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:04:40,284 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
18:04:41,291 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:04:43,498 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:04:46,908 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:04:54,235 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
consistent_bootstrap_test.py::TestBootstrapConsistency::test_consistent_reads_after_bootstrap 
-------------------------------- live log call ---------------------------------
18:05:45,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:05:45,857 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:05:45,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:05:46,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:05:46,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:05:46,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:06:06,177 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
18:06:07,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:06:09,191 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:06:13,3 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:06:19,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:06:28,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:06:28,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:06:28,857 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_consistent_reads_after_move passed 1 out of the required 1 times. Success!
test_consistent_reads_after_bootstrap passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 213.75 seconds ==========================
[msx] rc = 0
