cassandra topology_test.py true true
the_test is topology_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 12 items

topology_test.py::TestTopology::test_do_not_join_ring 
-------------------------------- live log call ---------------------------------
12:09:58,883 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:09:58,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:09:58,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:09:59,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:09:59,47 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  8%]
topology_test.py::TestTopology::test_size_estimates_multidc 
-------------------------------- live log call ---------------------------------
12:10:48,17 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:48,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:10:48,103 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,170 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:10:48,170 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,262 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:48,346 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:10:48,346 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,412 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:10:48,412 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:48,586 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:10:48,587 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:10:48,653 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,706 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:48,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:10:48,789 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,842 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:48,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:10:48,926 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:48,976 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:49,61 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:10:49,61 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:49,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:49,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:10:49,201 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:49,251 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:49,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:10:49,335 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:10:49,385 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:10:49,469 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:10:49,469 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
topology_test.py::TestTopology::test_simple_removenode 
-------------------------------- live log call ---------------------------------
12:11:19,179 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:11:19,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:11:19,264 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:11:19,331 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:11:19,331 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:11:19,423 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:11:19,508 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:11:19,508 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:11:19,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:11:19,574 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:11:19,666 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:11:19,750 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:11:19,750 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:11:19,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:11:19,817 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
topology_test.py::TestTopology::test_simple_decommission 
-------------------------------- live log call ---------------------------------
12:12:41,568 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:12:41,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:12:41,654 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:12:41,721 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:12:41,721 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:12:41,813 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:12:41,897 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:12:41,897 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:12:41,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:12:41,964 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:12:42,55 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:12:42,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:12:42,139 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:12:42,206 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:12:42,206 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
topology_test.py::TestTopology::test_concurrent_decommission_not_allowed SKIPPED [ 41%]
topology_test.py::TestTopology::test_resumable_decommission 
-------------------------------- live log call ---------------------------------
12:14:28,5 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:14:28,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:14:28,91 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:14:28,161 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:14:28,161 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:14:28,256 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:14:28,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:14:28,340 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:14:28,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:14:28,410 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:14:28,504 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:14:28,587 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:14:28,588 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:14:28,656 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:14:28,656 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:16:40,6 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
12:16:41,226 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
12:16:43,52 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
12:16:47,705 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
12:16:55,896 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
12:17:13,547 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
12:17:16,25 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
12:17:16,26 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:17,159 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:18,964 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:23,577 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:28,949 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:30,155 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:30,796 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:32,466 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:36,779 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:43,800 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:47,940 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:49,444 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
12:17:58,955 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:17:59,990 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:18:02,119 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:18:06,662 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:18:14,557 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
12:18:19,722 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 56.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
------------------------------ live log teardown -------------------------------
12:18:26,705 conftest ERROR Unexpected error in node1 log, error: 
ERROR [Stream-Deserializer-/127.0.0.2:7000-672d8154] 2021-12-31 11:15:24,624 StreamSession.java:888 - [Stream #9f8c83b0-6a65-11ec-b886-67c3b5ee99cb] Remote peer /127.0.0.2:7000 failed stream session.

topology_test.py::TestTopology::test_movement 
-------------------------------- live log call ---------------------------------
12:18:27,452 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:18:27,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:18:27,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:18:27,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:18:27,605 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:18:27,696 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:18:27,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:18:27,789 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:18:27,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:18:27,856 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:18:27,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:18:28,31 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:18:28,31 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:18:28,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:18:28,97 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 58%]
topology_test.py::TestTopology::test_decommission 
-------------------------------- live log call ---------------------------------
12:23:01,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:23:01,238 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:23:01,238 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:01,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:23:01,305 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:01,397 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:23:01,481 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:23:01,481 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:01,547 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:23:01,547 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:01,638 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:23:01,722 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:23:01,722 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:01,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:23:01,789 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:01,880 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:23:01,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:23:01,963 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:23:02,30 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:23:02,30 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
topology_test.py::TestTopology::test_move_single_node 
-------------------------------- live log call ---------------------------------
12:27:00,84 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:27:00,170 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:27:00,170 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:27:00,238 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:27:00,238 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
topology_test.py::TestTopology::test_decommissioned_node_cant_rejoin 
-------------------------------- live log call ---------------------------------
12:28:16,133 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:28:16,219 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:28:16,219 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:28:16,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:28:16,287 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:28:16,379 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:28:16,464 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:28:16,464 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:28:16,530 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:28:16,531 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:28:16,622 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:28:16,706 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:28:16,706 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:28:16,773 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:28:16,773 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 83%]
topology_test.py::TestTopology::test_crash_during_decommission 
-------------------------------- live log call ---------------------------------
12:29:44,773 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:29:44,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:29:44,858 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:29:44,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:29:44,926 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:29:45,21 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:29:45,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:29:45,106 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:29:45,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:29:45,174 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:29:45,266 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:29:45,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:29:45,351 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:29:45,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:29:45,418 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 91%]
topology_test.py::TestTopology::test_stop_decommission_too_few_replicas_multi_dc 
-------------------------------- live log call ---------------------------------
12:30:37,375 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:30:37,460 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:30:37,460 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:37,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:30:37,532 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:37,624 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:30:37,708 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:30:37,708 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:37,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:30:37,775 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:37,868 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:30:37,953 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:30:37,953 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:38,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:30:38,19 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:38,111 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:30:38,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:30:38,195 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:30:38,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:30:38,262 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_do_not_join_ring passed 1 out of the required 1 times. Success!
test_size_estimates_multidc passed 1 out of the required 1 times. Success!
test_simple_removenode passed 1 out of the required 1 times. Success!
test_simple_decommission passed 1 out of the required 1 times. Success!
test_resumable_decommission passed 1 out of the required 1 times. Success!
test_movement passed 1 out of the required 1 times. Success!
test_decommission passed 1 out of the required 1 times. Success!
test_move_single_node passed 1 out of the required 1 times. Success!
test_decommissioned_node_cant_rejoin passed 1 out of the required 1 times. Success!
test_crash_during_decommission passed 1 out of the required 1 times. Success!
test_stop_decommission_too_few_replicas_multi_dc passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 11 passed, 1 skipped in 1331.01 seconds ====================
[msx] rc = 0
