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
11:16:14,268 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:16:14,353 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:16:14,353 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:16:14,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:16:14,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:16:25,313 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:16:25,883 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:16:47,692 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 10%]
snapshot_test.py::TestSnapshot::test_snapshot_and_restore_drop_table_remove_dropped_column 
-------------------------------- live log call ---------------------------------
11:16:48,61 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:16:48,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:16:48,147 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:16:48,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:16:48,214 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
snapshot_test.py::TestSnapshot::test_snapshot_and_restore_dropping_a_column 
-------------------------------- live log call ---------------------------------
11:17:14,331 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:17:14,417 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:17:14,417 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:17:14,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:17:14,484 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 30%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog 
-------------------------------- live log call ---------------------------------
11:17:46,111 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:17:46,197 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:17:46,197 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:17:46,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:17:46,264 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:19:14,598 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:19:22,143 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:19:22,147 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:19:23,153 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:19:25,260 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:19:25,839 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:19:25,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:19:25,925 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:19:25,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:19:25,991 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:19:33,998 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:19:53,633 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 40%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_with_active_commitlog 
-------------------------------- live log call ---------------------------------
11:19:53,903 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:19:53,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:19:53,990 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:19:54,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:19:54,57 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:21:20,960 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:21:30,8 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:21:30,10 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:21:31,18 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:21:32,279 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:21:32,365 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:21:32,365 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:21:32,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:21:32,431 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:21:40,491 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:22:00,250 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 50%]
snapshot_test.py::TestArchiveCommitlog::test_dont_archive_commitlog 
-------------------------------- live log call ---------------------------------
11:22:00,526 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:22:00,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:22:00,616 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:22:00,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:22:00,683 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:23:27,403 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:23:36,579 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:23:36,581 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:23:37,688 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:23:38,897 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:23:38,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:23:38,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:23:39,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:23:39,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:23:47,74 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:24:05,120 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 60%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_point_in_time 
-------------------------------- live log call ---------------------------------
11:24:05,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:24:05,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:24:05,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:24:05,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:24:05,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:25:31,627 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:25:41,474 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:25:41,476 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:25:42,483 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:25:42,826 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:25:42,911 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:25:42,911 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:25:42,978 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:25:42,978 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:25:51,49 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:26:10,474 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 70%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_point_in_time_with_active_commitlog 
-------------------------------- live log call ---------------------------------
11:26:10,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:26:10,836 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:26:10,836 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:26:10,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:26:10,904 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:27:37,517 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:27:46,801 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:27:46,803 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:27:47,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:27:48,843 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:27:48,928 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:27:48,929 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:27:48,995 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:27:48,996 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:27:57,158 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:28:17,1 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 80%]
snapshot_test.py::TestArchiveCommitlog::test_archive_commitlog_point_in_time_with_active_commitlog_ln 
-------------------------------- live log call ---------------------------------
11:28:17,280 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:28:17,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:28:17,375 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:28:17,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:28:17,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:29:44,157 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:29:53,352 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:29:53,354 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:29:54,560 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:29:55,728 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:29:55,818 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:29:55,818 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:29:55,885 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:29:55,886 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:30:03,963 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
11:30:23,729 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 90%]
snapshot_test.py::TestArchiveCommitlog::test_archive_and_restore_commitlog_repeatedly 
-------------------------------- live log call ---------------------------------
11:30:24,17 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:30:24,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:30:24,104 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:30:24,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:30:24,173 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:31:00,85 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:31:00,87 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:31:01,94 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:31:03,400 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:31:08,12 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:31:16,568 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
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

========================= 10 passed in 903.35 seconds ==========================
[msx] rc = 0
