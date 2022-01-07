cassandra global_row_key_cache_test.py true true
the_test is global_row_key_cache_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

global_row_key_cache_test.py::TestGlobalRowKeyCache::test_functional 
-------------------------------- live log call ---------------------------------
19:12:39,51 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:12:39,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:12:39,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:12:39,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:12:39,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:12:39,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:12:39,542 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:12:39,627 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:12:39,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:12:39,748 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:12:39,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:12:39,884 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:12:39,968 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:12:40,18 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:12:40,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:13:21,832 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:13:22,940 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:13:25,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:13:28,957 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:13:29,761 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:13:30,62 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:13:31,867 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:13:35,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:13:38,384 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:13:44,70 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:13:44,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:13:45,302 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:13:47,106 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:13:51,719 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:13:53,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:13:58,843 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:00,347 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:14:24,714 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 61.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:14:29,526 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 60.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:14:40,679 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:14:41,757 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:43,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:48,97 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:14:48,98 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:14:48,99 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:14:48,101 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:14:48,475 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:49,103 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:49,104 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:14:49,204 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:14:51,108 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:14:51,209 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:51,510 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:14:54,718 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:54,819 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:14:55,799 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:14:55,877 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:14:55,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:14:55,949 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:14:56,36 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:14:56,89 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:14:56,171 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:14:56,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:15:02,663 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:15:03,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:03,766 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:12,264 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:15:38,449 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:15:38,450 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:15:39,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:39,659 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:41,546 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:41,566 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:45,358 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:45,565 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:15:45,576 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:15:45,779 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:46,581 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:46,663 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:48,99 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:15:48,99 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:15:48,102 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:48,689 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:48,779 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:49,304 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:49,305 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:51,511 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:51,611 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:52,498 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:52,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:54,92 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:54,604 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:55,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:15:56,123 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:15:59,516 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:00,686 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:16:00,686 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:16:01,10 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:01,812 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:01,822 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:03,142 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:16:04,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:04,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:05,47 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:08,640 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:08,730 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:09,232 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:16:10,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:16:15,758 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:16,150 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:16,751 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:17,967 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 34.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:18,101 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:16:18,110 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:19,188 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:20,90 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:20,891 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:20,992 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:16:24,301 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:31,601 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:33,298 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:33,526 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:16:42,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 61.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:16:47,342 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 62.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:16:50,142 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:52,259 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 55.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:55,986 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 66.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:16:56,287 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 65.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:17:01,683 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 68.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:02,475 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:10,398 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:17:10,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:17:10,545 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:17:10,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:17:10,681 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:17:10,682 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:17:10,683 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:17:10,686 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:17:10,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:17:10,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:17:11,691 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:17:11,692 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:17:11,793 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:13,701 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:17:13,901 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:17:14,2 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:17,912 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:17:17,913 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:17:18,102 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:17:18,104 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:18,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:19,166 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:21,70 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:25,181 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:26,435 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:17:26,936 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:17:53,735 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:17:54,944 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:17:57,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:17:59,37 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:00,765 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:00,851 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:18:00,853 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:00,862 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:18:01,867 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:01,970 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:02,68 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:02,292 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 115.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:02,593 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 135.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:03,672 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:03,975 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:04,73 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:07,382 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:07,585 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:07,586 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:07,783 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:07,964 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:18:09,92 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:10,196 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 138.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:10,389 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 120.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:10,683 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:18:10,683 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:18:10,684 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:18:10,686 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:10,896 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:11,688 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:11,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:11,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:13,393 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:13,794 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:14,95 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:14,807 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:15,131 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:15,133 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:15,408 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:16,215 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:16,218 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:16,506 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:16,908 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:17,7 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:17,410 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:18,13 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:18,105 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:18:18,108 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:18,522 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:18,524 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:19,139 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:21,245 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:22,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:22,230 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:22,231 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:23,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:24,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:24,955 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:25,436 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:26,338 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:30,652 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:32,880 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:18:33,350 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:41,579 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:48,223 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:18:48,225 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:49,298 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:49,298 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:51,403 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:51,503 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:55,17 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:55,316 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:18:55,616 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:58,825 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:18:59,39 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:00,126 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:02,29 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:03,349 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:19:03,841 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:03,841 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:04,443 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:05,537 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:06,339 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 66.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:06,749 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:10,685 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:19:10,686 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:19:10,688 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:10,869 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:19:10,870 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:19:10,871 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:19:10,873 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:11,56 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 62.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:11,160 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:11,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:11,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:11,875 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:11,981 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:11,981 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:13,864 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:13,884 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:13,959 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:14,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:14,84 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:14,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:15,133 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:16,172 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:17,593 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:17,674 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:18,95 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:18,96 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:18,106 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:19:18,108 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:18,177 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:18,476 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:19:18,570 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:19:18,581 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:18,625 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:19:18,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:19:18,784 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:19:18,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:19:19,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:19,230 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:20,393 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:21,342 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:22,699 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:25,752 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:26,7 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:26,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:19:26,441 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:26,842 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:27,10 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:28,916 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:29,39 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:19:33,72 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:19:36,437 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:01,931 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:20:01,932 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:20:01,933 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:20:01,934 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:20:02,941 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:03,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:03,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:03,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:04,832 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:04,948 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:05,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:05,232 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:08,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:08,641 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:08,641 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:08,741 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:09,47 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:20:09,52 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:20:10,65 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:10,145 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:10,686 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:20:10,871 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:20:10,871 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:20:11,750 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:11,876 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:11,977 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:12,70 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:12,352 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:12,954 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 111.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:13,782 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:13,857 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:13,857 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 147.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:13,882 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:15,662 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:16,63 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:16,181 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:16,564 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:16,883 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:16,965 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:17,391 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:17,566 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:18,108 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:20:18,294 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:18,369 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 289.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:19,170 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:21,75 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:24,170 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:20:24,180 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:24,503 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:24,685 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:25,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:25,306 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:26,489 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:26,619 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:27,512 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:28,491 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 276.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:29,40 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:29,662 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:29,663 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:29,900 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 29.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:30,99 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:30,100 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 29.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:30,803 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:30,804 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:31,21 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:31,523 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:31,903 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:32,405 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:32,507 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:32,508 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:32,803 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:36,116 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:36,117 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:36,916 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:38,842 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:39,444 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:40,688 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:20:40,690 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:40,873 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:20:40,877 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:41,229 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:41,831 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:41,962 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:42,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:43,166 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:43,767 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:43,935 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:44,168 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:44,237 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:20:44,237 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:45,239 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:47,777 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:47,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:48,108 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
19:20:48,110 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:48,247 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:20:49,150 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:51,55 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:55,66 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:55,266 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:55,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
19:20:56,399 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_functional passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 508.18 seconds ==========================
[msx] rc = 0
