cassandra schema_test.py true true
the_test is schema_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 6 items

schema_test.py::TestSchema::test_table_alteration 
-------------------------------- live log call ---------------------------------
10:49:54,224 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:49:54,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:49:54,310 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:49:54,378 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:49:54,378 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
schema_test.py::TestSchema::test_drop_column_compact SKIPPED             [ 33%]
schema_test.py::TestSchema::test_drop_column_compaction 
-------------------------------- live log call ---------------------------------
10:50:16,577 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:50:16,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:16,662 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:50:16,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:16,728 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
schema_test.py::TestSchema::test_drop_column_queries 
-------------------------------- live log call ---------------------------------
10:50:27,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:50:27,647 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:27,647 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:50:27,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:27,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
schema_test.py::TestSchema::test_drop_column_and_restart 
-------------------------------- live log call ---------------------------------
10:50:35,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:50:35,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:35,355 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:50:35,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:35,421 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:50:42,789 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:50:43,796 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:50:45,802 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:50:49,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 83%]
schema_test.py::TestSchema::test_drop_static_column_and_restart 
-------------------------------- live log call ---------------------------------
10:50:56,18 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:50:56,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:56,103 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:50:56,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:50:56,175 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:51:05,423 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:51:06,429 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:51:08,334 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:51:11,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_table_alteration passed 1 out of the required 1 times. Success!
test_drop_column_compaction passed 1 out of the required 1 times. Success!
test_drop_column_queries passed 1 out of the required 1 times. Success!
test_drop_column_and_restart passed 1 out of the required 1 times. Success!
test_drop_static_column_and_restart passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

===================== 5 passed, 1 skipped in 84.63 seconds =====================
[msx] rc = 0
