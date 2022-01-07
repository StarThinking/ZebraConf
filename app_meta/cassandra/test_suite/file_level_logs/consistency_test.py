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
17:41:56,876 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:41:56,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:41:57,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:41:57,120 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:41:57,204 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:41:57,270 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:41:57,361 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:41:57,445 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:41:57,511 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:42:44,410 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:42:44,415 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:45,427 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:47,544 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:47,829 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:42:47,831 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:48,940 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:50,760 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:52,75 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:54,471 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:42:59,795 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:43:02,91 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:43:10,379 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
17:43:10,381 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:43:11,587 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:43:13,392 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:43:16,901 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:43:17,455 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:43:20,253 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [  3%]
------------------------------ live log teardown -------------------------------
17:43:25,222 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused

consistency_test.py::TestAvailability::test_simple_strategy_each_quorum 
-------------------------------- live log call ---------------------------------
17:43:25,686 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:43:25,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:43:25,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:43:25,929 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:43:26,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:43:26,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:43:26,171 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:43:26,255 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:43:26,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:44:13,235 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:44:13,237 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:44:14,243 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:44:15,858 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:44:15,859 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:44:15,947 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:44:16,965 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:44:19,271 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [  7%]
consistency_test.py::TestAvailability::test_network_topology_strategy 
-------------------------------- live log call ---------------------------------
17:44:20,761 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:20,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:44:20,915 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:44:21,8 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:21,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:44:21,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:44:21,251 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:21,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:44:21,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:44:21,494 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:21,578 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:44:21,645 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:44:21,738 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:21,822 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:44:21,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:44:21,982 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:22,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:44:22,133 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:44:22,227 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:22,312 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
17:44:22,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
17:44:22,472 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:22,556 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
17:44:22,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
17:44:22,716 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:44:22,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
17:44:22,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
17:45:16,224 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:45:16,226 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:17,333 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:19,347 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:22,678 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:45:22,680 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:23,697 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:23,978 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:25,709 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:29,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:31,743 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:37,276 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:45,405 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:48,170 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
17:45:48,172 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:45:49,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:45:51,384 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:45:51,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:45:54,993 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:46:01,928 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:46:09,429 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
17:46:09,432 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:46:10,437 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:46:12,242 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:46:14,851 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 71.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:46:16,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:46:16,453 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:46:23,241 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:46:24,915 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:46:26,767 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
17:46:26,770 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:46:27,987 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:46:29,896 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:46:34,107 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:46:41,944 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:46:43,214 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:46:46,993 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
17:46:46,994 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:46:47,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:46:50,205 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:46:51,972 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 66.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:46:54,543 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:46:55,609 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:47:01,687 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:47:07,6 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
17:47:07,9 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.6:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:47:08,220 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:47:09,930 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:47:14,366 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:47:15,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:47:18,771 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 63.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:47:20,259 cassandra.cluster WARNING Host 127.0.0.7:9042 has been marked down
17:47:20,260 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.7:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
17:47:21,466 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
17:47:22,387 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:47:22,831 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 60.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:47:23,575 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
17:47:26,603 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 112.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:47:27,199 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
17:47:28,554 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 110.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 11%]
consistency_test.py::TestAvailability::test_network_topology_strategy_each_quorum 
-------------------------------- live log call ---------------------------------
17:47:35,203 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:35,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:47:35,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:47:35,459 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:35,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:47:35,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:47:35,714 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:35,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:47:35,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:47:35,957 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:36,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:47:36,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:47:36,201 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:36,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:47:36,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:47:36,445 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:36,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:47:36,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:47:36,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:36,773 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
17:47:36,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node7
17:47:36,934 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:37,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
17:47:37,85 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node8
17:47:37,223 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:47:37,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
17:47:37,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node9
17:48:30,793 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:48:30,795 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:31,804 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:33,509 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:38,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:38,910 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:48:38,912 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:40,26 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:41,931 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:45,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:46,43 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:49,850 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
17:48:49,852 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:48:50,858 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:48:52,359 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:48:52,864 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:48:57,74 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:49:00,728 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
17:49:00,729 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:49:01,835 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:49:03,491 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:49:03,740 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:49:06,302 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:49:07,856 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:49:09,107 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
17:49:09,109 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:49:09,402 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:49:10,115 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:49:12,220 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:49:15,929 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:49:16,779 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:49:17,880 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
17:49:17,882 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:49:18,887 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:49:20,892 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:49:23,146 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
17:49:24,301 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:49:24,952 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
17:49:26,637 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
17:49:26,638 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.6:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:49:27,643 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:49:29,649 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:49:32,69 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 66.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:49:32,721 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
17:49:32,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
17:49:34,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
17:49:34,956 cassandra.cluster WARNING Host 127.0.0.7:9042 has been marked down
17:49:34,957 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.7:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
17:49:35,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.7:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.7', 9042)]. Last error: Connection refused
PASSED                                                                   [ 14%]
consistency_test.py::TestAccuracy::test_simple_strategy_users 
-------------------------------- live log call ---------------------------------
17:49:38,178 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:38,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:49:38,336 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:49:38,429 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:38,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:49:38,579 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:49:38,672 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:38,756 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:49:38,823 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:49:38,915 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:38,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:49:39,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:49:39,159 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:39,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:49:39,311 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:49:39,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:39,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:49:39,501 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:39,585 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:49:39,635 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:39,725 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:49:39,776 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:39,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:49:39,910 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:49:39,995 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 18%]
consistency_test.py::TestAccuracy::test_simple_strategy_each_quorum_users 
-------------------------------- live log call ---------------------------------
17:51:50,883 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:51:50,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:51:51,34 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:51:51,127 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:51:51,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:51:51,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:51:51,370 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:51:51,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:51:51,520 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:51:51,612 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:51:51,695 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:51:51,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:51:51,854 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:51:51,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:51:52,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 22%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_users 
-------------------------------- live log call ---------------------------------
17:52:41,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:52:42,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:52:42,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:52:42,201 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:52:42,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:52:42,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:52:42,445 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:52:42,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:52:42,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:52:42,688 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:52:42,772 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:52:42,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:52:42,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:52:43,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:52:43,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:52:43,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:52:43,259 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:52:43,327 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
PASSED                                                                   [ 25%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_each_quorum_users 
-------------------------------- live log call ---------------------------------
17:56:10,681 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:56:10,765 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:56:10,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:56:10,927 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:56:11,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:56:11,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:56:11,173 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:56:11,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:56:11,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:56:11,418 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:56:11,502 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:56:11,570 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:56:11,663 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:56:11,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:56:11,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:56:11,946 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:56:12,30 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:56:12,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
PASSED                                                                   [ 29%]
consistency_test.py::TestAccuracy::test_simple_strategy_counters 
-------------------------------- live log call ---------------------------------
17:57:13,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:13,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:57:13,553 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:57:13,646 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:13,730 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:57:13,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:57:13,891 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:13,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:57:14,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:57:14,98 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:14,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:57:14,234 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:14,319 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:57:14,370 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:14,456 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
consistency_test.py::TestAccuracy::test_simple_strategy_each_quorum_counters 
-------------------------------- live log call ---------------------------------
17:57:54,401 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:54,486 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:57:54,553 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:57:54,646 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:54,730 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:57:54,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:57:54,890 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:57:54,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:57:55,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 37%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_counters 
-------------------------------- live log call ---------------------------------
17:58:21,966 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:58:22,51 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:58:22,119 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:58:22,213 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:58:22,297 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:58:22,364 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:58:22,456 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:58:22,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:58:22,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
17:58:22,699 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:58:22,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:58:22,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
17:58:22,942 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:58:23,25 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:58:23,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
17:58:23,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:58:23,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
17:58:23,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
PASSED                                                                   [ 40%]
consistency_test.py::TestAccuracy::test_network_topology_strategy_each_quorum_counters 
-------------------------------- live log call ---------------------------------
18:00:03,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:04,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:00:04,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:00:04,238 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:04,323 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:00:04,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:00:04,484 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:04,567 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:00:04,635 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:00:04,728 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:04,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:00:04,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:00:04,973 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:05,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
18:00:05,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
18:00:05,218 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:05,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
18:00:05,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
PASSED                                                                   [ 44%]
consistency_test.py::TestConsistency::test_14513_transient 
-------------------------------- live log call ---------------------------------
18:00:54,200 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:00:54,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:00:54,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 48%]
consistency_test.py::TestConsistency::test_14513_permanent 
-------------------------------- live log call ---------------------------------
18:01:08,444 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:01:08,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:01:08,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:01:08,688 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:01:08,771 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:01:08,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:01:08,930 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:01:09,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:01:09,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:01:37,194 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 51%]
consistency_test.py::TestConsistency::test_14330 
-------------------------------- live log call ---------------------------------
18:02:04,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:02:04,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:02:04,655 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:02:04,748 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:02:04,832 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:02:04,899 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:02:23,175 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
18:02:24,181 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:02:26,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:02:30,701 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:02:39,730 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
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
18:02:47,203 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:02:47,290 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:02:47,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:02:47,449 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:02:47,532 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:02:47,599 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:02:47,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:02:47,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:02:47,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:03:07,975 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
18:03:08,980 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:03:11,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
18:03:14,899 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
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

=================== 16 passed, 11 skipped in 1281.12 seconds ===================
[msx] rc = 0
