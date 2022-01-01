cassandra consistency_test.py true true
the_test is consistency_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 27 items

consistency_test.py::TestAvailability::test_simple_strategy 
-------------------------------- live log call ---------------------------------
03:42:16,410 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:16,497 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:42:16,497 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:42:16,565 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:42:16,566 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:42:16,656 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:16,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:42:16,742 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:42:16,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:42:16,808 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:42:16,898 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:16,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:42:16,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:42:17,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:42:17,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:43:03,369 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:43:03,371 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:04,489 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:06,508 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:07,19 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:43:07,23 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:08,137 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:10,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:10,249 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:14,72 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:18,470 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:21,491 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:29,910 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
03:43:29,912 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:43:31,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:43:33,27 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:43:35,634 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:43:37,539 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:43:37,543 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [  3%]
consistency_test.py::TestAvailability::test_simple_strategy_each_quorum 
-------------------------------- live log call ---------------------------------
03:43:45,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:45,561 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:45,561 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:43:45,627 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:45,628 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:43:45,719 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:45,804 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:43:45,804 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:43:45,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:43:45,870 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:43:45,961 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:46,46 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:43:46,46 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:43:46,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:43:46,113 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  7%]
consistency_test.py::TestAvailability::test_network_topology_strategy 
-------------------------------- live log call ---------------------------------
03:44:31,814 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:31,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:44:31,901 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:31,968 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:44:31,968 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:32,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:44:32,146 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,212 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:44:32,212 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:32,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:44:32,390 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,456 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:44:32,457 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:32,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:44:32,632 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,698 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:44:32,699 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,790 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:32,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:44:32,875 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:32,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:44:32,942 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:33,33 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:33,118 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:44:33,118 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:44:33,185 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:44:33,185 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:44:33,276 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:33,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
03:44:33,362 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:33,429 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
03:44:33,429 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:33,520 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:33,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
03:44:33,606 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:33,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
03:44:33,674 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:33,766 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:33,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
03:44:33,852 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:44:33,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
03:44:33,920 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:45:27,55 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:45:27,57 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:28,266 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:30,580 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:33,312 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:45:33,317 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:34,100 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:34,431 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:36,444 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:40,473 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:41,448 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:49,4 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:58,446 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:45:58,504 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
03:45:58,506 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:45:59,512 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:46:01,718 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:46:04,84 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:46:06,29 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:46:14,581 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:46:20,72 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
03:46:20,75 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:46:21,79 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:46:22,884 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:46:26,991 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:46:27,497 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:46:32,273 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:46:32,328 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 71.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:46:36,150 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:46:37,279 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
03:46:37,280 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:46:38,293 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:46:40,607 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:46:45,18 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:46:52,569 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:46:53,453 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:46:57,592 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
03:46:57,593 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:46:58,600 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:47:00,605 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:47:04,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:47:05,937 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 72.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:47:07,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:47:11,670 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:47:17,720 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
03:47:17,722 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.6:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:47:18,837 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:47:20,952 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:47:24,578 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:47:27,134 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:47:27,859 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:47:31,58 cassandra.cluster WARNING Host 127.0.0.7:9042 has been marked down
03:47:31,60 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.7:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
03:47:32,65 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
03:47:33,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:47:33,873 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
03:47:34,868 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 133.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:47:37,995 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
PASSED                                                                   [ 11%]
consistency_test.py::TestAvailability::test_network_topology_strategy_each_quorum 
-------------------------------- live log call ---------------------------------
03:47:44,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:44,376 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:47:44,376 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:44,444 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:47:44,444 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:44,535 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:44,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:47:44,621 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:44,687 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:47:44,688 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:44,779 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:44,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:47:44,864 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:44,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:47:44,932 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:45,23 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:45,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:47:45,108 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:45,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:47:45,176 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:45,267 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:45,353 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:47:45,353 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:45,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:47:45,421 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:45,512 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:45,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:47:45,598 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:47:45,665 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:47:45,665 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:47:45,757 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:45,842 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
03:47:45,842 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:45,910 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
03:47:45,910 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:46,1 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:46,86 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
03:47:46,86 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:46,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
03:47:46,154 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:46,245 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:47:46,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
03:47:46,333 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:47:46,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
03:47:46,401 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:48:39,582 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:48:39,583 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:40,589 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:42,494 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:46,204 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:47,285 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:48:47,286 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:48,392 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:50,599 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:53,726 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:55,111 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:48:58,280 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
03:48:58,282 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:48:59,387 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:49:01,293 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:49:03,233 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:49:05,2 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:49:09,131 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
03:49:09,132 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:49:09,667 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:49:10,137 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:49:12,444 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:49:12,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:49:16,455 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:49:17,456 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
03:49:17,458 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:49:18,564 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:49:20,670 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:49:20,676 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:49:25,82 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:49:25,280 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:49:26,252 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
03:49:26,254 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:49:27,259 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:49:29,265 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:49:29,366 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:49:33,175 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:49:34,304 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:49:34,998 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
03:49:34,999 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.6:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:49:36,105 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:49:36,938 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 72.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:49:38,411 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:49:41,322 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
03:49:41,497 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
03:49:42,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
03:49:43,309 cassandra.cluster WARNING Host 127.0.0.7:9042 has been marked down
03:49:43,310 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.7:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
03:49:44,316 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
PASSED                                                                   [ 14%]
consistency_test.py::TestAccuracy::test_simple_strategy_users 
-------------------------------- live log call ---------------------------------
03:49:46,797 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:46,884 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:49:46,884 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:46,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:49:46,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,43 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:47,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:49:47,128 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:49:47,196 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:47,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:49:47,372 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:49:47,439 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,530 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:47,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:49:47,616 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:49:47,683 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,775 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:47,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:49:47,860 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:49:47,928 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:47,983 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:48,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:49:48,69 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:48,119 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:48,205 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:49:48,205 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:48,254 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:48,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:49:48,341 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:48,390 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:48,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:49:48,475 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:49:48,525 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:48,611 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:49:48,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 18%]
consistency_test.py::TestAccuracy::test_simple_strategy_each_quorum_users 
-------------------------------- live log call ---------------------------------
03:52:05,742 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:05,828 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:52:05,828 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:05,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:52:05,895 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:05,985 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:06,70 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:52:06,70 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,136 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:52:06,136 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,226 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:06,312 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:52:06,312 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,378 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:52:06,378 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,469 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:06,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:52:06,554 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:52:06,620 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,710 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:06,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:52:06,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:06,861 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:52:06,861 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_users 
-------------------------------- live log call ---------------------------------
03:52:55,315 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:55,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:52:55,404 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:55,471 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:52:55,472 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:55,563 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:55,649 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:52:55,649 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:55,740 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:52:55,741 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:55,832 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:55,918 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:52:55,918 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:55,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:52:55,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:56,76 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:56,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:52:56,162 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:56,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:52:56,229 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:56,321 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:56,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:52:56,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:56,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:52:56,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:52:56,565 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:56,651 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:52:56,651 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:52:56,718 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:52:56,718 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
PASSED                                                                   [ 25%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_each_quorum_users 
-------------------------------- live log call ---------------------------------
03:56:25,200 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:25,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:56:25,286 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:25,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:56:25,354 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:25,446 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:25,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:56:25,531 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:25,599 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:56:25,599 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:25,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:25,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:56:25,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:25,881 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:56:25,881 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:25,973 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:26,58 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:56:26,59 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:26,126 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:56:26,126 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:26,217 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:26,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:56:26,303 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:26,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:56:26,370 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:56:26,461 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:26,546 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:56:26,547 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:56:26,614 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:56:26,614 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
PASSED                                                                   [ 29%]
consistency_test.py::TestAccuracy::test_simple_strategy_counters 
-------------------------------- live log call ---------------------------------
03:57:25,551 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:25,638 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:57:25,638 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:25,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:57:25,706 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:25,798 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:25,884 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:57:25,884 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:25,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:57:25,952 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:26,44 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:26,129 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:57:26,129 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:26,196 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:57:26,197 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:26,252 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:26,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:57:26,338 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:26,388 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:26,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:57:26,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:57:26,525 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:26,615 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:57:26,615 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
consistency_test.py::TestAccuracy::test_simple_strategy_each_quorum_counters 
-------------------------------- live log call ---------------------------------
03:58:06,777 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:06,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:58:06,864 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:06,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:58:06,932 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:07,24 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:07,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:58:07,110 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:07,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:58:07,177 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:07,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:07,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:58:07,355 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:07,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:58:07,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 37%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_counters 
-------------------------------- live log call ---------------------------------
03:58:34,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:34,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:58:34,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:58:34,247 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:34,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:58:34,426 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:58:34,494 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:34,672 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:58:34,672 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:58:34,739 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,832 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:34,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:58:34,920 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:34,987 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:58:34,987 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:35,79 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:35,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:58:35,164 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:35,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
03:58:35,231 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:58:35,323 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:58:35,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:58:35,409 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
03:58:35,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
03:58:35,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
PASSED                                                                   [ 40%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_each_quorum_counters 
-------------------------------- live log call ---------------------------------
04:00:18,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:18,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:00:18,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:18,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:00:18,606 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:18,697 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:18,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:00:18,783 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:18,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:00:18,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:18,942 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:19,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:00:19,28 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:19,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:00:19,95 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:19,187 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:19,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:00:19,272 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:19,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:00:19,340 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:19,431 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:19,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:00:19,517 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:19,584 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:00:19,584 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:00:19,677 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:19,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
04:00:19,770 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
04:00:19,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
04:00:19,838 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
PASSED                                                                   [ 44%]
consistency_test.py::TestConsistency::test_14513_transient 
-------------------------------- live log call ---------------------------------
04:01:04,213 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:01:04,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:01:04,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:01:04,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:01:04,368 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 48%]
consistency_test.py::TestConsistency::test_14513_permanent 
-------------------------------- live log call ---------------------------------
04:01:18,208 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:01:18,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:01:18,295 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:01:18,361 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:01:18,362 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:01:18,453 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:01:18,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:01:18,540 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:01:18,612 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:01:18,613 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:01:18,705 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:01:18,792 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:01:18,792 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:01:18,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:01:18,858 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 51%]
consistency_test.py::TestConsistency::test_14330 
-------------------------------- live log call ---------------------------------
04:02:15,267 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:02:15,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:02:15,356 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:15,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:02:15,423 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:15,516 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:02:15,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:02:15,602 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:15,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:02:15,669 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:32,267 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
04:02:33,345 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:02:35,552 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:02:39,966 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:02:48,693 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 55%]
consistency_test.py::TestConsistency::test_13911 SKIPPED                 [ 59%]
consistency_test.py::TestConsistency::test_13911_rows_srp SKIPPED        [ 62%]
consistency_test.py::TestConsistency::test_13911_partitions_srp SKIPPED  [ 66%]
consistency_test.py::TestConsistency::test_13880 SKIPPED                 [ 70%]
consistency_test.py::TestConsistency::test_13747 SKIPPED                 [ 74%]
consistency_test.py::TestConsistency::test_13595 SKIPPED                 [ 77%]
consistency_test.py::TestConsistency::test_12872 SKIPPED                 [ 81%]
consistency_test.py::TestConsistency::test_short_read SKIPPED            [ 85%]
consistency_test.py::TestConsistency::test_short_read_delete SKIPPED     [ 88%]
consistency_test.py::TestConsistency::test_short_read_quorum_delete SKIPPED [ 92%]
consistency_test.py::TestConsistency::test_readrepair SKIPPED            [ 96%]
consistency_test.py::TestConsistency::test_quorum_available_during_failure 
-------------------------------- live log call ---------------------------------
04:02:56,204 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:02:56,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:02:56,290 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:56,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:02:56,356 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:56,446 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:02:56,533 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:02:56,534 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:56,600 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:02:56,600 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:56,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:02:56,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:02:56,775 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:02:56,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:02:56,842 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:03:15,605 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
04:03:16,640 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:03:18,647 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
04:03:22,859 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_simple_strategy passed 1 out of the required 1 times. Success!
test_simple_strategy_each_quorum passed 1 out of the required 1 times. Success!
test_network_topology_strategy passed 1 out of the required 1 times. Success!
test_network_topology_strategy_each_quorum passed 1 out of the required 1 times. Success!
test_simple_strategy_users passed 1 out of the required 1 times. Success!
test_simple_strategy_each_quorum_users passed 1 out of the required 1 times. Success!
test_network_topology_strategy_users passed 1 out of the required 1 times. Success!
test_network_topology_strategy_each_quorum_users passed 1 out of the required 1 times. Success!
test_simple_strategy_counters passed 1 out of the required 1 times. Success!
test_simple_strategy_each_quorum_counters passed 1 out of the required 1 times. Success!
test_network_topology_strategy_counters passed 1 out of the required 1 times. Success!
test_network_topology_strategy_each_quorum_counters passed 1 out of the required 1 times. Success!
test_14513_transient passed 1 out of the required 1 times. Success!
test_14513_permanent passed 1 out of the required 1 times. Success!
test_14330 passed 1 out of the required 1 times. Success!
test_quorum_available_during_failure passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 16 passed, 11 skipped in 1269.34 seconds ===================
[msx] rc = 0
