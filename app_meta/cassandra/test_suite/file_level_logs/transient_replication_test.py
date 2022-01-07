cassandra transient_replication_test.py true true
the_test is transient_replication_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 26 items

transient_replication_test.py::TestTransientReplication::test_transient_noop_write 
-------------------------------- live log setup --------------------------------
03:04:45,631 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:04:45,726 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:04:45,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:04:45,895 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:04:45,980 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:04:46,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:04:46,144 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:04:46,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:04:46,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  3%]
transient_replication_test.py::TestTransientReplication::test_transient_write 
-------------------------------- live log setup --------------------------------
03:05:16,422 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:16,511 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:05:16,585 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:05:16,681 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:16,766 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:05:16,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:05:16,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:17,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:05:17,87 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  7%]
transient_replication_test.py::TestTransientReplication::test_transient_full_merge_read 
-------------------------------- live log setup --------------------------------
03:05:50,488 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:50,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:05:50,648 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:05:50,744 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:50,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:05:50,899 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:05:50,996 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:51,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:05:51,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
03:06:39,601 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:06:39,603 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:06:40,709 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:06:42,300 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:06:42,301 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:06:42,729 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:06:42,730 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:06:42,814 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:06:43,507 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:06:43,836 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 11%]
transient_replication_test.py::TestTransientReplication::test_srp 
-------------------------------- live log setup --------------------------------
03:06:45,34 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:45,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:06:45,190 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:06:45,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:45,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:06:45,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:06:45,536 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:45,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:06:45,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 15%]
transient_replication_test.py::TestTransientReplication::test_transient_full_merge_read_with_delete_transient_coordinator 
-------------------------------- live log setup --------------------------------
03:07:29,514 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:07:29,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:07:29,672 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:07:29,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:07:29,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:07:29,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:07:30,24 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:07:30,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:07:30,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
03:08:18,653 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:08:18,656 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:19,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:21,151 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:08:21,152 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:21,241 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:08:21,242 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:21,631 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:08:21,632 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:21,968 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:22,257 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:22,348 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:08:22,637 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 19%]
transient_replication_test.py::TestTransientReplication::test_transient_full_merge_read_with_delete_full_coordinator 
-------------------------------- live log setup --------------------------------
03:08:23,777 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:08:23,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:08:23,935 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:08:24,34 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:08:24,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:08:24,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:08:24,288 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:08:24,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:08:24,442 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 23%]
transient_replication_test.py::TestTransientReplication::test_cheap_quorums 
-------------------------------- live log setup --------------------------------
03:09:08,267 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:09:08,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:09:08,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:09:08,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:09:08,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:09:08,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:09:08,771 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:09:08,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:09:08,928 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 26%]
transient_replication_test.py::TestTransientReplication::test_speculative_write 
-------------------------------- live log setup --------------------------------
03:09:33,293 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:09:33,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:09:33,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:09:33,548 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:09:33,633 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:09:33,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:09:33,800 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:09:33,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:09:33,956 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 30%]
transient_replication_test.py::TestTransientReplication::test_keyspace_rf_changes SKIPPED [ 34%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_speculative_write_repair_cycle 
-------------------------------- live log setup --------------------------------
03:10:03,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:03,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:03,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:03,349 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:03,434 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:10:03,504 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:10:03,599 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:03,684 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:10:03,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 38%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_primary_range_repair 
-------------------------------- live log setup --------------------------------
03:10:49,956 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:50,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:50,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:50,208 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:50,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:10:50,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:10:50,464 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:50,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:10:50,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 42%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_optimized_primary_range_repair 
-------------------------------- live log setup --------------------------------
03:11:36,605 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:36,691 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:36,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:36,856 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:36,942 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:11:37,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:11:37,106 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:37,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:11:37,260 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 46%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_optimized_primary_range_repair_with_lcs 
-------------------------------- live log setup --------------------------------
03:12:23,722 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:23,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:23,881 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:23,977 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:24,62 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:12:24,132 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:12:24,227 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:24,312 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:12:24,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 50%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_transient_incremental_repair 
-------------------------------- live log setup --------------------------------
03:13:11,369 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:13:11,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:13:11,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:13:11,623 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:13:11,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:13:11,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:13:11,879 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:13:11,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:13:12,34 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 53%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_full_repair_from_full_replica 
-------------------------------- live log setup --------------------------------
03:13:58,4 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:13:58,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:13:58,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:13:58,257 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:13:58,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:13:58,412 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:13:58,507 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:13:58,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:13:58,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 57%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_full_repair_from_transient_replica 
-------------------------------- live log setup --------------------------------
03:14:33,84 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:14:33,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:14:33,239 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:14:33,333 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:14:33,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:14:33,487 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:14:33,582 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:14:33,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:14:33,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 61%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_speculative_write_repair_cycle 
-------------------------------- live log setup --------------------------------
03:15:08,161 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:08,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:08,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:08,411 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:08,497 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:15:08,570 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:15:08,665 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:08,751 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:15:08,820 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 65%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_primary_range_repair 
-------------------------------- live log setup --------------------------------
03:15:54,26 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:54,117 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:54,188 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:54,284 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:54,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:15:54,438 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:15:54,534 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:54,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:15:54,688 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 69%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_optimized_primary_range_repair 
-------------------------------- live log setup --------------------------------
03:16:40,672 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:16:40,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:16:40,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:16:40,926 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:16:41,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:16:41,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:16:41,178 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:16:41,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:16:41,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 73%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_optimized_primary_range_repair_with_lcs 
-------------------------------- live log setup --------------------------------
03:17:27,539 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:17:27,625 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:17:27,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:17:27,793 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:17:27,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:17:27,955 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:17:28,53 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:17:28,138 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:17:28,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 76%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_transient_incremental_repair 
-------------------------------- live log setup --------------------------------
03:18:15,424 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:15,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:15,585 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:15,680 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:15,764 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:18:15,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:18:15,930 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:16,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:18:16,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 80%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_full_repair_from_full_replica 
-------------------------------- live log setup --------------------------------
03:19:02,301 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:02,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:19:02,461 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:19:02,555 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:02,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:19:02,712 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:19:02,806 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:02,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:19:02,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 84%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_full_repair_from_transient_replica 
-------------------------------- live log setup --------------------------------
03:19:36,885 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:36,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:19:37,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:19:37,139 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:37,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:19:37,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:19:37,396 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:19:37,482 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:19:37,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 88%]
transient_replication_test.py::TestTransientReplicationSpeculativeQueries::test_always_speculate 
-------------------------------- live log setup --------------------------------
03:20:10,703 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:10,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:20:10,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:20:10,959 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:11,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:20:11,117 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:20:11,212 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:11,297 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:20:11,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 92%]
transient_replication_test.py::TestTransientReplicationSpeculativeQueries::test_custom_speculate 
-------------------------------- live log setup --------------------------------
03:20:42,515 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:42,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:20:42,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:20:42,771 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:42,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:20:42,948 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:20:43,43 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:20:43,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:20:43,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 96%]
transient_replication_test.py::TestMultipleTransientNodes::test_transient_full_merge_read 
-------------------------------- live log setup --------------------------------
03:21:05,516 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:21:05,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:21:05,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:21:05,770 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:21:05,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:21:05,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:21:06,23 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:21:06,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:21:06,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:21:06,279 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:21:06,365 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:21:06,436 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:21:06,532 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:21:06,617 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:21:06,688 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [100%]
===Flaky Test Report===

test_transient_noop_write passed 1 out of the required 1 times. Success!
test_transient_write passed 1 out of the required 1 times. Success!
test_transient_full_merge_read passed 1 out of the required 1 times. Success!
test_srp passed 1 out of the required 1 times. Success!
test_transient_full_merge_read_with_delete_transient_coordinator passed 1 out of the required 1 times. Success!
test_transient_full_merge_read_with_delete_full_coordinator passed 1 out of the required 1 times. Success!
test_cheap_quorums passed 1 out of the required 1 times. Success!
test_speculative_write passed 1 out of the required 1 times. Success!
test_speculative_write_repair_cycle passed 1 out of the required 1 times. Success!
test_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair_with_lcs passed 1 out of the required 1 times. Success!
test_transient_incremental_repair passed 1 out of the required 1 times. Success!
test_full_repair_from_full_replica passed 1 out of the required 1 times. Success!
test_full_repair_from_transient_replica passed 1 out of the required 1 times. Success!
test_speculative_write_repair_cycle passed 1 out of the required 1 times. Success!
test_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair_with_lcs passed 1 out of the required 1 times. Success!
test_transient_incremental_repair passed 1 out of the required 1 times. Success!
test_full_repair_from_full_replica passed 1 out of the required 1 times. Success!
test_full_repair_from_transient_replica passed 1 out of the required 1 times. Success!
test_always_speculate passed 1 out of the required 1 times. Success!
test_custom_speculate passed 1 out of the required 1 times. Success!
test_transient_full_merge_read passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 25 passed, 1 skipped in 1031.39 seconds ====================
[msx] rc = 0
