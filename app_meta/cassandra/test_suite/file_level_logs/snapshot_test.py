cassandra snapshot_test.py true true
the_test is snapshot_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 10 items

snapshot_test.py::TestSnapshot::test_basic_snapshot_and_restore 
-------------------------------- live log call ---------------------------------
01:25:04,890 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:25:04,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:25:05,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:25:16,623 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:25:17,174 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:25:39,532 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 10%]
snapshot_test.py::TestSnapshot::test_snapshot_and_restore_drop_table_remove_dropped_column 
-------------------------------- live log call ---------------------------------
01:25:39,935 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:25:40,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:25:40,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 20%]
snapshot_test.py::TestSnapshot::test_snapshot_and_restore_dropping_a_column 
-------------------------------- live log call ---------------------------------
01:26:07,464 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:26:07,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:26:07,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 30%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog 
-------------------------------- live log call ---------------------------------
01:26:34,977 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:26:35,63 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:26:35,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:28:04,922 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:28:11,221 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:28:11,224 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:28:12,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:28:14,637 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:28:16,816 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:28:16,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:28:16,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:28:25,402 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:28:45,690 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 40%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_with_active_commitlog 
-------------------------------- live log call ---------------------------------
01:28:45,981 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:28:46,71 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:28:46,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:30:15,936 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:30:22,212 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:30:22,215 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:30:23,222 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:30:25,26 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:30:27,859 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:30:27,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:30:28,13 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:30:36,458 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:30:56,489 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 50%]
snapshot_test.py::TestArchiveCommitlog::test_dont_archive_commitlog 
-------------------------------- live log call ---------------------------------
01:30:56,760 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:30:56,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:30:56,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:32:30,594 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:32:42,337 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:32:42,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:32:42,488 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:32:50,890 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:33:09,490 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 60%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_point_in_time 
-------------------------------- live log call ---------------------------------
01:33:09,759 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:33:09,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:33:09,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:40,192 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:34:52,157 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:34:52,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:52,309 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:00,687 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:35:21,89 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 70%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_point_in_time_with_active_commitlog 
-------------------------------- live log call ---------------------------------
01:35:21,354 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:35:21,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:21,508 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:53,71 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:37:04,896 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:37:04,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:05,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:13,504 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:37:34,573 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 80%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_point_in_time_with_active_commitlog_ln 
-------------------------------- live log call ---------------------------------
01:37:34,845 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:37:34,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:34,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:06,911 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:39:18,742 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:39:18,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:18,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:27,281 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:39:47,120 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 90%]
snapshot_test.py::TestArchiveCommitlog::test_archive_and_restore_commitlog_repeatedly 
-------------------------------- live log call ---------------------------------
01:39:47,416 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:39:47,504 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:47,571 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:23,656 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:40:23,660 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:40:24,666 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:40:26,671 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:40:30,80 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:40:38,806 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:40:42,436 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [100%]
===Flaky Test Report===

test_basic_snapshot_and_restore passed 1 out of the required 1 times. Success!
test_snapshot_and_restore_drop_table_remove_dropped_column passed 1 out of the required 1 times. Success!
test_snapshot_and_restore_dropping_a_column passed 1 out of the required 1 times. Success!
test_archive_commitlog passed 1 out of the required 1 times. Success!
test_archive_commitlog_with_active_commitlog passed 1 out of the required 1 times. Success!
test_dont_archive_commitlog passed 1 out of the required 1 times. Success!
test_archive_commitlog_point_in_time passed 1 out of the required 1 times. Success!
test_archive_commitlog_point_in_time_with_active_commitlog passed 1 out of the required 1 times. Success!
test_archive_commitlog_point_in_time_with_active_commitlog_ln passed 1 out of the required 1 times. Success!
test_archive_and_restore_commitlog_repeatedly passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 10 passed in 938.65 seconds ==========================
[msx] rc = 0
