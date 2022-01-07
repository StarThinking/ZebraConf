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
00:58:13,671 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:58:13,757 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:58:13,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 16%]
schema_test.py::TestSchema::test_drop_column_compact SKIPPED             [ 33%]
schema_test.py::TestSchema::test_drop_column_compaction 
-------------------------------- live log call ---------------------------------
00:58:37,507 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:58:37,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:58:37,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
schema_test.py::TestSchema::test_drop_column_queries 
-------------------------------- live log call ---------------------------------
00:58:48,743 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:58:48,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:58:48,897 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 66%]
schema_test.py::TestSchema::test_drop_column_and_restart 
-------------------------------- live log call ---------------------------------
00:58:56,452 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:58:56,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:58:56,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:59:04,157 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:59:05,165 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:59:06,969 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:59:10,681 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 83%]
schema_test.py::TestSchema::test_drop_static_column_and_restart 
-------------------------------- live log call ---------------------------------
00:59:17,444 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:59:17,532 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:59:17,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:59:26,773 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:59:27,880 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:59:29,886 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:59:33,698 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_table_alteration passed 1 out of the required 1 times. Success!
test_drop_column_compaction passed 1 out of the required 1 times. Success!
test_drop_column_queries passed 1 out of the required 1 times. Success!
test_drop_column_and_restart passed 1 out of the required 1 times. Success!
test_drop_static_column_and_restart passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

===================== 5 passed, 1 skipped in 87.12 seconds =====================
[msx] rc = 0
