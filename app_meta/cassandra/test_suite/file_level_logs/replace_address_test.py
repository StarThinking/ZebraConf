cassandra replace_address_test.py true true
the_test is replace_address_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 16 items

replace_address_test.py::TestReplaceAddress::test_replace_stopped_node 
-------------------------------- live log call ---------------------------------
23:09:27,595 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:09:27,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:09:27,750 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:09:27,841 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:09:27,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:09:27,992 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:09:28,84 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:09:28,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:09:28,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:09:28,289 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:09:28,374 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:09:28,425 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:09:28,509 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:09:28,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:09:28,644 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:09:47,757 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:10:39,68 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:10:39,69 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:10:40,75 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:40,77 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:41,982 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:41,984 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:42,663 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:42,667 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:10:42,762 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:10:42,857 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:10:42,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:10:43,781 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:45,889 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:46,307 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:46,507 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:49,902 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:54,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:54,730 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:10:57,824 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:11:09,268 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:11:09,470 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:11:14,869 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:11:30,329 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:30,331 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:11:30,332 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:11:30,440 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:30,441 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:11:30,442 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:11:31,243 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:31,245 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:11:31,246 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:11:31,415 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:31,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:32,332 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:33,320 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:33,838 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:34,237 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:37,230 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:37,446 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:37,946 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:44,467 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:45,164 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:11:45,820 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:11:45,910 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:11:47,60 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:47,565 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:11:47,567 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:48,577 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:48,965 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:50,481 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:53,176 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:54,291 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:56,341 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:11:56,342 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:57,402 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:11:59,407 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:12:00,516 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:12:00,543 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:12:01,109 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:12:01,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:12:02,202 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:12:02,318 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:12:02,343 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:12:03,16 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:12:03,415 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:12:03,818 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:12:05,619 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:12:08,228 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:12:09,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:12:10,27 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:12:10,535 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
PASSED                                                                   [  6%]
replace_address_test.py::TestReplaceAddress::test_replace_shutdown_node 
-------------------------------- live log call ---------------------------------
23:12:11,262 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:12:11,350 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:12:11,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:12:11,510 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:12:11,595 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:12:11,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:12:11,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:12:11,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:12:11,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:12:11,958 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:12:12,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:12:12,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:12:12,238 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:12:12,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:12:12,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:12:31,499 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:13:18,261 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:18,266 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:13:18,365 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:13:18,461 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:13:18,536 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:13:19,279 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:21,488 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:25,801 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:31,331 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:13:32,437 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:33,622 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:34,244 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:38,357 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:39,994 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:13:40,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:43,206 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:47,582 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:47,719 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:49,866 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:13:56,43 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:14:02,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:14:03,869 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 350, in handle_read
    buf = self._socket.recv(self.in_buffer_size)
ConnectionResetError: [Errno 104] Connection reset by peer
23:14:03,871 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:14:03,871 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:14:04,349 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:04,352 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:14:04,353 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:14:05,70 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:05,434 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:05,724 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:05,726 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:14:05,727 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:14:06,812 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:07,75 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:07,641 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:09,18 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:11,653 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:11,687 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:13,329 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:18,871 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:14:20,68 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:14:20,161 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:14:21,174 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:22,158 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:14:22,184 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:14:23,82 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:23,255 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:25,561 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:26,793 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:29,573 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:31,333 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:14:31,334 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:32,405 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:34,310 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:35,918 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:37,495 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:37,817 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:39,995 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:14:41,134 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:14:43,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:14:46,636 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:14:47,350 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:14:47,725 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:14:48,148 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
PASSED                                                                   [ 12%]
replace_address_test.py::TestReplaceAddress::test_replace_stopped_node_same_address 
-------------------------------- live log call ---------------------------------
23:14:48,910 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:14:48,996 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:14:49,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:14:49,162 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:14:49,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:14:49,314 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:14:49,406 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:14:49,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:14:49,559 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:14:49,612 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:14:49,699 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:14:49,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:14:49,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:14:49,885 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:14:49,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:15:09,129 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:15:58,273 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:15:58,274 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:15:58,625 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:15:58,630 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:15:58,737 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:15:58,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:15:58,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:15:59,388 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:15:59,489 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:15:59,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:01,195 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:01,597 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:01,850 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:05,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:05,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:06,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:13,285 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:14,233 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:14,733 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:28,872 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:29,27 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:31,880 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:16:58,624 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:16:59,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:01,718 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:05,628 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:08,969 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:17:08,970 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:17:09,977 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:17:09,977 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:11,783 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:17:12,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:13,650 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:15,994 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:17:16,332 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:17:16,333 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:17:16,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:17,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:17:17,599 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 18%]
replace_address_test.py::TestReplaceAddress::test_replace_first_boot 
-------------------------------- live log call ---------------------------------
23:17:18,226 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:17:18,311 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:17:18,378 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:17:18,470 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:17:18,556 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:17:18,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:17:18,714 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:17:18,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:17:18,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:17:18,919 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:17:19,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:17:19,55 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:17:19,140 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:17:19,190 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:17:19,276 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:17:38,440 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:18:28,697 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:18:28,699 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:18:28,778 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:28,782 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:18:28,867 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:18:28,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:18:29,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:18:29,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:29,714 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:29,798 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:31,525 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:31,725 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:32,6 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:35,237 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:36,137 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:36,419 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:42,658 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:43,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:44,59 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:58,397 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:18:59,303 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:19:01,86 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:19:14,541 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:14,543 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:19:14,545 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:19:15,65 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:15,75 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:19:15,81 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:19:15,464 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:15,466 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
23:19:15,466 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
23:19:15,627 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:16,147 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:16,653 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:17,432 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:18,253 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:18,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:21,644 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:22,464 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:23,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
23:19:30,126 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:19:30,216 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:19:30,396 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:19:30,425 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:19:30,592 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:19:30,618 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
23:19:31,273 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:31,492 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:31,698 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:33,476 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:33,497 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:33,704 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:36,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:37,307 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:37,917 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:44,527 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:44,803 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:45,639 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:19:46,482 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:19:47,545 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:19:49,751 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:19:53,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:19:54,5 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:19:54,7 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:19:54,690 cassandra.cluster WARNING Found an invalid row for peer (127.0.0.3). Ignoring host.
PASSED                                                                   [ 25%]
replace_address_test.py::TestReplaceAddress::test_replace_active_node 
-------------------------------- live log call ---------------------------------
23:19:55,395 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:19:55,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:19:55,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:19:55,648 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:19:55,735 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:19:55,803 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:19:55,896 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:19:55,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:19:56,74 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:19:56,130 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:19:56,217 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:19:56,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:19:56,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:19:56,408 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:19:56,495 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:20:15,637 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:20:16,382 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:16,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:20:16,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
PASSED                                                                   [ 31%]
replace_address_test.py::TestReplaceAddress::test_replace_nonexistent_node 
-------------------------------- live log call ---------------------------------
23:20:46,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:46,409 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:20:46,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:20:46,572 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:46,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:20:46,725 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:20:46,817 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:46,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:20:46,969 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:20:47,23 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:47,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:20:47,159 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:47,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:20:47,295 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:20:47,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:21:06,557 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:21:07,313 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:07,409 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:21:07,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
PASSED                                                                   [ 37%]
replace_address_test.py::TestReplaceAddress::test_fail_without_replace 
-------------------------------- live log call ---------------------------------
23:21:17,179 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:17,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:21:17,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:21:17,425 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:17,557 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:21:17,625 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:21:17,718 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:17,804 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:21:17,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:21:17,923 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:18,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:21:18,58 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:18,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:21:18,194 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:21:18,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:21:37,441 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:22:15,582 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:15,673 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:21,965 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:22,60 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:27,656 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 43%]
replace_address_test.py::TestReplaceAddress::test_fail_when_seed 
-------------------------------- live log call ---------------------------------
23:22:28,951 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:29,37 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:22:29,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:22:29,195 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:29,282 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:22:29,350 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:22:29,442 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:29,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:29,595 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:29,648 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:29,734 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:22:29,785 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:29,869 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:22:29,920 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:30,5 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:49,152 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 50%]
replace_address_test.py::TestReplaceAddress::test_unsafe_replace 
-------------------------------- live log call ---------------------------------
23:22:55,802 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:55,889 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:22:55,956 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:22:56,48 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:56,133 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:22:56,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:22:56,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:56,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:56,442 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:22:56,495 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:56,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:22:56,632 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:56,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:22:56,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:22:56,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:23:15,976 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:23:53,607 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:23:53,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:24:00,2 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:00,102 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:24:05,231 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:24:05,232 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:24:06,238 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:24:06,240 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:24:08,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:24:08,347 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:24:11,560 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:24:11,858 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:24:15,813 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:24:15,817 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:16,978 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:19,284 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:23,194 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:23,274 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:24:24,280 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:26,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:30,199 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:31,524 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:24:38,322 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 56%]
replace_address_test.py::TestReplaceAddress::test_insert_data_during_replace_same_address 
-------------------------------- live log call ---------------------------------
23:24:45,20 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:45,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:24:45,173 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:24:45,265 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:45,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:24:45,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:24:45,511 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:45,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:24:45,664 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:24:45,719 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:45,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:24:45,860 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:45,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:24:45,995 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:46,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:24:46,132 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:46,249 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:24:46,301 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:46,386 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:24:46,436 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:24:46,521 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:25:05,698 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:25:56,820 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:25:56,821 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:25:57,34 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:25:57,39 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:25:57,149 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:25:57,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:25:57,320 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:25:57,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:25:57,949 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:25:58,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:25:59,949 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:25:59,958 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:00,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:03,570 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:03,861 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:04,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:10,791 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:11,282 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:12,196 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:27,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:28,39 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:26:28,427 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:27:14,714 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:27:15,726 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:27:17,833 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:27:21,945 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:27:27,33 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:27:27,34 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:27:28,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:27:28,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:27:30,48 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:27:30,248 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:27:30,669 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 62%]
replace_address_test.py::TestReplaceAddress::test_insert_data_during_replace_different_address 
-------------------------------- live log call ---------------------------------
23:27:33,159 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:33,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:27:33,311 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:27:33,403 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:33,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:27:33,559 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:27:33,651 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:33,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:27:33,805 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:27:33,860 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:33,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:27:33,996 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:34,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:27:34,132 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:34,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:27:34,270 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:34,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:27:34,405 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:34,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:27:34,542 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:27:34,627 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:27:53,805 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:28:43,956 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:28:43,957 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:28:44,163 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:44,167 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:28:44,264 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:28:44,358 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:28:44,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:28:44,978 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:45,72 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:45,282 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:47,290 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:47,290 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:47,381 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:51,393 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:51,403 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:51,503 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:58,425 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:28:59,127 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:00,518 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:14,656 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:14,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:16,575 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:43,551 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 58.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:47,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:29:48,348 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:30:04,179 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:30:04,185 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:30:05,192 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:30:07,401 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:30:07,720 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:30:08,206 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:30:08,303 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:30:08,828 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:09,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:09,315 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:10,833 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:11,120 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:11,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:11,933 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:30:13,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:14,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:14,931 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:15,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:15,447 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:18,450 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:22,450 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:23,454 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:23,623 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:30:23,624 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:30:23,979 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:24,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:30:25,270 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:30:26,566 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:30:31,78 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:30:31,850 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:30:31,851 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 68%]
replace_address_test.py::TestReplaceAddress::test_resume_failed_replace 
-------------------------------- live log call ---------------------------------
23:30:32,931 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:33,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:30:33,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:30:33,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:33,263 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:30:33,330 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:30:33,423 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:33,508 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:30:33,576 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:30:33,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:33,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:30:33,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:33,857 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:30:33,908 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:33,994 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:30:34,44 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:30:34,131 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:30:53,290 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:31:43,571 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:31:43,573 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:31:43,855 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:43,859 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:31:44,183 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:31:44,302 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:31:44,376 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:31:44,593 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:44,692 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:44,876 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:46,802 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:46,903 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:46,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:50,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:51,217 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:51,517 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:58,118 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:59,440 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:31:59,941 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:32:14,280 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:32:14,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:32:15,785 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:32:25,995 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:32:26,215 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:32:26,416 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:32:27,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:27,219 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:27,518 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:29,202 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:29,323 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:29,525 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:33,33 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:33,312 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:33,535 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:40,653 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:41,155 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:41,533 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:32:43,854 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:32:43,855 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:32:44,946 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:32:47,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:32:50,860 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 75%]
replace_address_test.py::TestReplaceAddress::test_restart_failed_replace_with_reset_resume_state 
-------------------------------- live log call ---------------------------------
23:32:52,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:52,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:32:52,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:32:52,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:52,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:32:52,536 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:32:52,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:52,715 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:32:52,781 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:32:52,834 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:52,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:32:52,969 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:53,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:32:53,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:53,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:32:53,239 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:32:53,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:33:12,452 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:34:03,813 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:34:03,814 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:34:04,246 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:04,250 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:34:04,549 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:34:04,641 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:34:04,712 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:34:04,828 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:04,929 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:05,262 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:06,939 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:07,39 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:07,170 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:10,751 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:10,982 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:11,253 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:18,72 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:18,704 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:20,378 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:35,819 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:36,319 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:34:36,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:35:03,698 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 55.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:35:05,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 72.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:35:08,341 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 59.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:35:59,444 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 144.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:36:07,897 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 138.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:36:17,890 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 144.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:36:41,787 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:36:42,290 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:36:42,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:43,363 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:44,594 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:45,670 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:47,674 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:36:48,677 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:49,206 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:49,279 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:50,782 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:54,291 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:57,332 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:36:58,3 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:37:01,811 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:37:04,247 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:37:04,248 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:37:05,454 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:37:05,796 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:37:05,797 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
PASSED                                                                   [ 81%]
------------------------------ live log teardown -------------------------------
23:37:06,825 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused

replace_address_test.py::TestReplaceAddress::test_restart_failed_replace 
-------------------------------- live log call ---------------------------------
23:37:07,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:07,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:37:07,519 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:37:07,615 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:07,702 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:37:07,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:37:07,862 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:07,949 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:37:08,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:37:08,69 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:08,155 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:37:08,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:08,291 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:37:08,342 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:08,428 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:37:08,478 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:37:08,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:37:27,790 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:38:18,158 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:38:18,160 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:38:19,0 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:19,4 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:38:19,169 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:19,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:38:19,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:38:19,396 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:19,464 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:38:20,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:21,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:21,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:22,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:24,596 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:24,925 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:26,142 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:32,217 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:33,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:33,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:47,758 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:48,187 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:38:51,810 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:39:15,458 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 58.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:39:19,540 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:39:27,702 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:40:14,409 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 124.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:40:27,417 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 125.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:40:36,878 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 124.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:41:51,757 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:41:52,761 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:52,944 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:41:53,372 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:41:53,947 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:54,474 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:54,765 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:55,952 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:56,680 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:58,173 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:41:59,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:42:01,292 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:42:05,728 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:42:05,729 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:42:06,784 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:42:07,400 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:42:07,687 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:42:08,514 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:42:08,589 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:42:12,599 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 87%]
replace_address_test.py::TestReplaceAddress::test_replace_with_insufficient_replicas 
-------------------------------- live log call ---------------------------------
23:42:18,318 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:42:18,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:42:18,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:42:18,565 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:42:18,650 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:42:18,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:42:18,808 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:42:18,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:42:18,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:42:19,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:42:19,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:42:19,150 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:42:19,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:42:19,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:42:19,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:42:38,554 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:43:27,791 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:43:28,185 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:28,190 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
23:43:28,897 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:29,195 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:31,101 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:31,105 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:35,117 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:35,314 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:36,291 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:43:36,380 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:43:36,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:43:38,370 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:43:38,372 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:43:39,442 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:43:41,747 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:43:42,250 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:44,53 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:45,256 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:43:53,479 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:43:57,793 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:43:58,185 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:43:58,186 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:43:59,299 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:44:01,305 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:44:02,502 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
23:44:05,616 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:44:08,217 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:44:13,136 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 93%]
replace_address_test.py::TestReplaceAddress::test_multi_dc_replace_with_rf1 
-------------------------------- live log call ---------------------------------
23:44:22,94 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:44:22,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:44:22,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:44:22,340 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:44:22,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:44:22,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:44:22,548 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:44:22,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:44:22,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:44:22,771 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:44:41,703 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:45:38,151 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:45:38,153 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:45:38,782 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:38,784 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:45:38,869 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:45:38,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:45:39,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
23:45:39,170 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:39,270 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:40,2 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:41,182 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:41,281 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:41,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:45,295 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:45,393 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:46,222 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:53,142 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:54,19 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:45:54,620 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:46:07,857 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:46:09,485 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:46:12,868 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:46:26,411 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:46:27,235 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:46:27,514 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:28,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:29,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:30,242 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:33,128 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:33,629 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:46:34,154 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:34,631 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:46:36,537 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_replace_stopped_node passed 1 out of the required 1 times. Success!
test_replace_shutdown_node passed 1 out of the required 1 times. Success!
test_replace_stopped_node_same_address passed 1 out of the required 1 times. Success!
test_replace_first_boot passed 1 out of the required 1 times. Success!
test_replace_active_node passed 1 out of the required 1 times. Success!
test_replace_nonexistent_node passed 1 out of the required 1 times. Success!
test_fail_without_replace passed 1 out of the required 1 times. Success!
test_fail_when_seed passed 1 out of the required 1 times. Success!
test_unsafe_replace passed 1 out of the required 1 times. Success!
test_insert_data_during_replace_same_address passed 1 out of the required 1 times. Success!
test_insert_data_during_replace_different_address passed 1 out of the required 1 times. Success!
test_resume_failed_replace passed 1 out of the required 1 times. Success!
test_restart_failed_replace_with_reset_resume_state passed 1 out of the required 1 times. Success!
test_restart_failed_replace passed 1 out of the required 1 times. Success!
test_replace_with_insufficient_replicas passed 1 out of the required 1 times. Success!
test_multi_dc_replace_with_rf1 passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 16 passed in 2231.54 seconds =========================
[msx] rc = 0
