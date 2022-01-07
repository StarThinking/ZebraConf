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
02:19:42,427 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:19:42,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:19:42,581 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  8%]
topology_test.py::TestTopology::test_size_estimates_multidc 
-------------------------------- live log call ---------------------------------
02:20:32,212 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:32,320 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:20:32,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:20:32,484 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:32,569 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:20:32,638 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:20:32,730 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:32,816 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:20:32,884 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:20:32,939 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:33,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:20:33,75 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:33,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:20:33,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:33,302 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:20:33,355 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:33,441 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:20:33,493 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:33,580 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:20:33,631 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:33,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 16%]
topology_test.py::TestTopology::test_simple_removenode 
-------------------------------- live log call ---------------------------------
02:21:04,796 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:21:04,881 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:21:04,949 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:21:05,42 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:21:05,126 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:21:05,194 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:21:05,286 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:21:05,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:21:05,437 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 25%]
topology_test.py::TestTopology::test_simple_decommission 
-------------------------------- live log call ---------------------------------
02:22:29,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:29,520 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:22:29,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:22:29,692 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:29,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:22:29,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:22:29,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:30,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:22:30,90 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
topology_test.py::TestTopology::test_concurrent_decommission_not_allowed SKIPPED [ 41%]
topology_test.py::TestTopology::test_resumable_decommission 
-------------------------------- live log call ---------------------------------
02:24:17,395 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:24:17,481 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:24:17,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:24:17,645 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:24:17,729 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:24:17,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:24:17,892 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:24:17,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:24:18,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:26:29,761 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
02:26:30,785 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:26:32,616 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:26:36,258 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:26:45,60 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:26:59,338 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:27:05,998 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
02:27:05,999 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:07,59 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:08,966 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:13,476 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:18,131 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:19,137 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:21,346 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:21,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:25,960 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:28,516 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:27:34,485 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:39,787 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:48,137 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:49,228 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:51,356 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:27:54,890 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:28:02,383 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
------------------------------ live log teardown -------------------------------
02:28:07,742 conftest ERROR Unexpected error in node1 log, error: 
ERROR [Stream-Deserializer-/127.0.0.2:7000-bab5ddd6] 2022-01-03 01:25:13,623 StreamSession.java:888 - [Stream #ac3687e0-6c6e-11ec-896a-8d15ee1ebd21] Remote peer /127.0.0.2:7000 failed stream session.

topology_test.py::TestTopology::test_movement 
-------------------------------- live log call ---------------------------------
02:28:08,510 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:28:08,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:28:08,699 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:28:08,811 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:28:08,912 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:28:08,994 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:28:09,106 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:28:09,205 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:28:09,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 58%]
topology_test.py::TestTopology::test_decommission 
-------------------------------- live log call ---------------------------------
02:32:44,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:44,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:32:44,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:32:45,13 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:45,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:32:45,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:32:45,256 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:45,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:32:45,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:32:45,498 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:45,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:32:45,649 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 66%]
topology_test.py::TestTopology::test_move_single_node 
-------------------------------- live log call ---------------------------------
02:36:45,421 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:36:45,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:36:45,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 75%]
topology_test.py::TestTopology::test_decommissioned_node_cant_rejoin 
-------------------------------- live log call ---------------------------------
02:38:01,125 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:01,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:38:01,276 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:38:01,368 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:01,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:38:01,519 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:38:01,611 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:01,695 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:38:01,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 83%]
topology_test.py::TestTopology::test_crash_during_decommission 
-------------------------------- live log call ---------------------------------
02:39:31,523 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:39:31,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:39:31,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:39:31,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:39:31,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:39:31,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:39:32,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:39:32,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:39:32,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 91%]
topology_test.py::TestTopology::test_stop_decommission_too_few_replicas_multi_dc 
-------------------------------- live log call ---------------------------------
02:40:25,131 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:25,215 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:40:25,282 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:40:25,378 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:25,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:40:25,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:40:25,623 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:25,707 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:40:25,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:40:25,868 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:25,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:40:26,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
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

=================== 11 passed, 1 skipped in 1335.71 seconds ====================
[msx] rc = 0
