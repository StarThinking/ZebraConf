cassandra compaction_test.py true true
the_test is compaction_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 30 items

compaction_test.py::TestCompaction::test_compaction_delete[LeveledCompactionStrategy] SKIPPED [  3%]
compaction_test.py::TestCompaction::test_compaction_delete[SizeTieredCompactionStrategy] SKIPPED [  6%]
compaction_test.py::TestCompaction::test_compaction_delete[DateTieredCompactionStrategy] SKIPPED [ 10%]
compaction_test.py::TestCompaction::test_data_size 
-------------------------------- live log call ---------------------------------
17:18:27,986 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:18:28,72 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:18:28,140 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 13%]
compaction_test.py::TestCompaction::test_bloomfilter_size[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:18:58,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:18:58,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:18:58,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 16%]
compaction_test.py::TestCompaction::test_bloomfilter_size[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:20:10,196 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:20:10,282 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:20:10,349 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 20%]
compaction_test.py::TestCompaction::test_bloomfilter_size[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:21:22,99 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:21:22,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:21:22,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 23%]
compaction_test.py::TestCompaction::test_sstable_deletion[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:22:34,28 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:22:34,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:22:34,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 26%]
compaction_test.py::TestCompaction::test_sstable_deletion[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:22:49,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:22:49,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:22:49,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 30%]
compaction_test.py::TestCompaction::test_sstable_deletion[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:23:04,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:23:04,87 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:23:04,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
compaction_test.py::TestCompaction::test_dtcs_deletion[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:23:18,985 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:23:19,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:23:19,140 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 36%]
compaction_test.py::TestCompaction::test_compaction_throughput 
-------------------------------- live log call ---------------------------------
17:24:23,585 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:24:23,671 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:24:23,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
compaction_test.py::TestCompaction::test_compaction_strategy_switching[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:25:25,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:25:25,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:25:25,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:26:01,429 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:26:01,432 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:26:02,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:26:04,644 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:26:09,256 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:26:17,512 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'ks' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'ks\' does not exist"',)
PASSED                                                                   [ 43%]
compaction_test.py::TestCompaction::test_compaction_strategy_switching[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:26:18,605 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:26:18,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:26:18,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:26:54,787 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:26:54,789 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:26:55,796 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:26:57,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:27:01,812 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:27:10,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 46%]
compaction_test.py::TestCompaction::test_compaction_strategy_switching[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:27:11,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:27:11,776 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:27:11,843 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:27:47,885 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:27:47,888 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:27:48,898 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:27:51,104 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:27:54,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:28:02,537 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
compaction_test.py::TestCompaction::test_large_compaction_warning 
-------------------------------- live log call ---------------------------------
17:28:05,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:28:05,125 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:28:05,192 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 53%]
compaction_test.py::TestCompaction::test_disable_autocompaction_nodetool[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:28:28,729 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:28:28,814 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:28:28,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 56%]
compaction_test.py::TestCompaction::test_disable_autocompaction_nodetool[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:28:59,527 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:28:59,613 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:28:59,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
compaction_test.py::TestCompaction::test_disable_autocompaction_nodetool[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:29:30,375 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:29:30,462 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:29:30,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 63%]
compaction_test.py::TestCompaction::test_disable_autocompaction_schema[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:30:01,173 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:30:01,260 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:30:01,328 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:30:37,380 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:30:37,383 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:30:38,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 66%]
compaction_test.py::TestCompaction::test_disable_autocompaction_schema[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:30:46,9 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:30:46,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:30:46,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:31:22,212 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:31:22,214 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:31:23,221 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 70%]
compaction_test.py::TestCompaction::test_disable_autocompaction_schema[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:31:31,108 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:31:31,194 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:31:31,263 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:32:07,329 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:32:07,331 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:32:08,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 73%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:32:15,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:32:15,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:32:15,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 76%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:32:45,251 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:32:45,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:32:45,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 80%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:33:14,544 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:33:14,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:33:14,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 83%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter_and_nodetool[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:33:44,81 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:33:44,167 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:33:44,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 86%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter_and_nodetool[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:34:18,409 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:34:18,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:34:18,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 90%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter_and_nodetool[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
17:34:52,731 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:34:52,818 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:34:52,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 93%]
compaction_test.py::TestCompaction::test_user_defined_compaction 
-------------------------------- live log call ---------------------------------
17:35:27,51 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:35:27,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:35:27,207 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 96%]
compaction_test.py::TestCompaction::test_fanout_size[LeveledCompactionStrategy] SKIPPED [100%]
===Flaky Test Report===

test_data_size passed 1 out of the required 1 times. Success!
test_bloomfilter_size[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_bloomfilter_size[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_bloomfilter_size[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_sstable_deletion[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_sstable_deletion[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_sstable_deletion[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_dtcs_deletion[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_compaction_throughput passed 1 out of the required 1 times. Success!
test_compaction_strategy_switching[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_compaction_strategy_switching[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_compaction_strategy_switching[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_large_compaction_warning passed 1 out of the required 1 times. Success!
test_disable_autocompaction_nodetool[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_nodetool[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_nodetool[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_schema[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_schema[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_schema[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_alter[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_alter[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_alter[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_alter_and_nodetool[LeveledCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_alter_and_nodetool[SizeTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_disable_autocompaction_alter_and_nodetool[DateTieredCompactionStrategy] passed 1 out of the required 1 times. Success!
test_user_defined_compaction passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 26 passed, 4 skipped in 1064.54 seconds ====================
[msx] rc = 0
