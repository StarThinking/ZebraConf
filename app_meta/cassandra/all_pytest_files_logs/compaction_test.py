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
03:19:33,802 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:33,887 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:19:33,887 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:19:33,955 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:19:33,955 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 13%]
compaction_test.py::TestCompaction::test_bloomfilter_size[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:20:03,87 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:03,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:20:03,172 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:20:03,237 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:20:03,237 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
compaction_test.py::TestCompaction::test_bloomfilter_size[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:21:12,997 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:21:13,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:21:13,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:21:13,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:21:13,149 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
compaction_test.py::TestCompaction::test_bloomfilter_size[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:22:23,147 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:22:23,232 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:22:23,232 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:22:23,297 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:22:23,297 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 23%]
compaction_test.py::TestCompaction::test_sstable_deletion[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:23:32,796 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:23:32,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:32,882 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:23:32,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:32,947 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 26%]
compaction_test.py::TestCompaction::test_sstable_deletion[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:23:46,785 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:23:46,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:46,874 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:23:46,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:46,941 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 30%]
compaction_test.py::TestCompaction::test_sstable_deletion[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:24:00,769 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:00,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:00,856 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:24:00,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:00,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
compaction_test.py::TestCompaction::test_dtcs_deletion[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:24:15,9 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:15,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:15,95 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:24:15,161 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:15,161 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
compaction_test.py::TestCompaction::test_compaction_throughput 
-------------------------------- live log call ---------------------------------
03:25:19,116 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:25:19,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:25:19,201 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:25:19,267 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:25:19,267 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
compaction_test.py::TestCompaction::test_compaction_strategy_switching[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:26:20,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:26:20,113 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:26:20,113 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:26:20,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:26:20,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:26:56,25 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:26:56,31 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:57,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:59,247 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:03,258 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 43%]
compaction_test.py::TestCompaction::test_compaction_strategy_switching[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:27:12,132 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:27:12,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:27:12,218 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:27:12,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:27:12,284 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:27:48,128 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:27:48,131 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:49,138 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:51,43 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:55,253 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 46%]
compaction_test.py::TestCompaction::test_compaction_strategy_switching[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:28:04,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:04,328 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:04,328 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:28:04,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:04,395 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:28:40,249 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:28:40,251 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:41,457 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:43,564 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:48,74 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
compaction_test.py::TestCompaction::test_large_compaction_warning 
-------------------------------- live log call ---------------------------------
03:28:56,346 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:56,434 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:56,434 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:28:56,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:56,501 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
compaction_test.py::TestCompaction::test_disable_autocompaction_nodetool[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:29:19,328 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:29:19,413 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:29:19,414 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:29:19,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:29:19,479 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 56%]
compaction_test.py::TestCompaction::test_disable_autocompaction_nodetool[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:29:48,144 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:29:48,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:29:48,229 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:29:48,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:29:48,295 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
compaction_test.py::TestCompaction::test_disable_autocompaction_nodetool[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:30:16,679 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:30:16,764 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:30:16,765 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:30:16,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:30:16,830 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 63%]
compaction_test.py::TestCompaction::test_disable_autocompaction_schema[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:30:44,962 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:30:45,51 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:30:45,52 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:30:45,118 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:30:45,118 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:31:20,984 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 66%]
compaction_test.py::TestCompaction::test_disable_autocompaction_schema[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:31:27,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:31:27,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:31:27,372 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:31:27,437 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:31:27,438 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:32:03,290 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 70%]
compaction_test.py::TestCompaction::test_disable_autocompaction_schema[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:32:10,118 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:32:10,203 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:32:10,203 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:32:10,269 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:32:10,269 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:32:46,106 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 73%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:32:52,470 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:32:52,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:32:52,555 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:32:52,621 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:32:52,622 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 76%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:33:19,757 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:33:19,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:33:19,844 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:33:19,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:33:19,910 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:33:47,38 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:33:47,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:33:47,123 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:33:47,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:33:47,189 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 83%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter_and_nodetool[LeveledCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:34:14,341 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:34:14,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:34:14,428 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:34:14,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:34:14,493 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 86%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter_and_nodetool[SizeTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:34:46,648 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:34:46,734 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:34:46,734 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:34:46,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:34:46,800 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 90%]
compaction_test.py::TestCompaction::test_disable_autocompaction_alter_and_nodetool[DateTieredCompactionStrategy] 
-------------------------------- live log call ---------------------------------
03:35:18,709 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:35:18,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:35:18,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:35:18,861 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:35:18,861 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 93%]
compaction_test.py::TestCompaction::test_user_defined_compaction 
-------------------------------- live log call ---------------------------------
03:35:51,26 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:35:51,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:35:51,112 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:35:51,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:35:51,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

=================== 26 passed, 4 skipped in 1022.43 seconds ====================
[msx] rc = 0
