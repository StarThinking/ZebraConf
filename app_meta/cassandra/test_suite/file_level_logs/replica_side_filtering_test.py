cassandra replica_side_filtering_test.py true true
the_test is replica_side_filtering_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 58 items

replica_side_filtering_test.py::TestSecondaryIndexes::test_update_on_skinny_table 
-------------------------------- live log call ---------------------------------
23:47:39,999 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:47:40,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:47:40,152 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:47:40,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:47:40,328 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:47:40,394 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:48:00,356 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:48:07,518 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:48:07,521 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:48:08,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:48:10,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:48:13,949 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [  1%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_update_on_wide_table 
-------------------------------- live log call ---------------------------------
23:48:15,425 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:48:15,510 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:48:15,577 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:48:15,670 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:48:15,754 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:48:15,821 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:48:43,917 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:48:43,921 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:48:45,31 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:48:47,240 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:48:51,754 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [  3%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_update_on_static_column_with_empty_partition 
-------------------------------- live log call ---------------------------------
23:48:52,887 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:48:52,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:48:53,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:48:53,133 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:48:53,217 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:48:53,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:49:21,394 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:49:21,397 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:49:22,505 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:49:24,714 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:49:28,325 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [  5%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_update_on_static_column_with_not_empty_partition 
-------------------------------- live log call ---------------------------------
23:49:29,297 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:49:29,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:49:29,450 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:49:29,545 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:49:29,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:49:29,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:49:57,801 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:49:57,804 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:49:58,912 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:50:00,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:50:04,632 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [  6%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_update_on_collection 
-------------------------------- live log call ---------------------------------
23:50:05,740 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:50:05,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:50:05,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:50:06,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:50:06,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:50:06,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:50:34,287 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:50:34,289 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:50:35,398 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:50:37,206 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:50:40,818 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [  8%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_partition_key_column_with_empty_partitions 
-------------------------------- live log call ---------------------------------
23:50:42,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:50:42,263 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:50:42,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:50:42,422 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:50:42,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:50:42,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:51:10,755 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:51:10,758 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:51:11,766 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:51:13,574 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:51:17,584 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:51:27,119 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:27,121 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:51:28,130 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:29,269 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:51:29,270 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:29,937 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:30,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:32,280 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:33,349 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:51:36,692 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 10%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_partition_key_column_with_not_empty_partitions 
-------------------------------- live log call ---------------------------------
23:51:40,190 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:51:40,277 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:51:40,344 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:51:40,438 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:51:40,523 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:51:40,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:52:08,488 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:52:08,492 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:52:09,602 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:52:11,912 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:52:15,926 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:52:24,901 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:24,903 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:52:26,12 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:27,315 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:52:27,318 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:27,821 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:28,323 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:30,328 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:31,732 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:52:34,138 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 12%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_clustering_key_column 
-------------------------------- live log call ---------------------------------
23:52:37,950 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:52:38,35 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:52:38,107 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:52:38,201 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:52:38,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:52:38,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:53:06,469 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:53:06,471 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:53:07,580 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:53:09,689 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:53:13,201 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:53:22,792 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:22,794 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:53:23,802 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:25,79 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:53:25,81 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:25,610 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:26,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:28,395 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:29,623 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:53:32,607 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 13%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_static_column_with_empty_partitions 
-------------------------------- live log call ---------------------------------
23:53:35,713 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:53:35,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:53:35,869 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:53:35,963 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:53:36,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:53:36,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:54:04,229 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:54:04,231 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:54:05,240 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:54:07,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:54:11,464 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:54:20,593 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:20,596 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:54:21,704 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:22,856 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:54:22,857 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:23,712 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:23,863 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:25,667 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:27,925 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:54:29,878 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 15%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_static_column_with_empty_partitions_and_rows_after 
-------------------------------- live log call ---------------------------------
23:54:33,734 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:54:33,820 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:54:33,889 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:54:33,984 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:54:34,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:54:34,135 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:54:54,157 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:55:01,317 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:55:01,321 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:55:02,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:55:04,540 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:55:07,951 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:55:17,617 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:17,620 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:55:18,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:19,833 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:55:19,835 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:20,738 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:20,841 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:23,47 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:24,952 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:55:27,157 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 17%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions 
-------------------------------- live log call ---------------------------------
23:55:30,747 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:55:30,836 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:55:30,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:55:30,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:55:31,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:55:31,152 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:55:59,263 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:55:59,266 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:56:00,375 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:56:02,283 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:56:06,498 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:56:15,592 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:15,594 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:56:16,602 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:17,860 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:56:17,862 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:18,811 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:18,868 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:21,174 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:22,523 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:56:24,984 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 18%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions_and_rows_after 
-------------------------------- live log call ---------------------------------
23:56:28,507 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:56:28,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:56:28,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:56:28,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:56:28,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:56:28,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:56:57,129 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:56:57,133 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:56:58,241 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:57:00,349 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:57:04,60 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:57:11,683 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:57:13,607 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:13,608 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:57:14,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:15,628 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:57:15,629 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:16,635 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:17,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:18,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:21,235 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:57:22,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 20%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_on_regular_column 
-------------------------------- live log call ---------------------------------
23:57:26,765 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:57:26,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:57:26,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:57:27,12 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:57:27,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:57:27,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:57:55,345 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:57:55,348 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:57:56,460 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:57:58,368 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:58:02,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:58:11,841 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:11,843 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:58:12,950 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:13,910 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:58:13,912 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:14,758 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:14,916 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:17,223 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:19,172 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:58:20,832 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 22%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_and_rows_after 
-------------------------------- live log call ---------------------------------
23:58:25,50 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:58:25,135 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:58:25,203 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:58:25,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:58:25,387 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:58:25,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:58:53,659 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:58:53,663 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:58:54,674 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:58:56,682 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:59:00,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:59:10,13 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:10,15 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:59:11,223 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:12,191 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:59:12,192 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:13,198 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:13,232 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:15,304 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:17,645 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:59:19,114 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 24%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_deletion_with_limit_and_rows_between 
-------------------------------- live log call ---------------------------------
23:59:23,61 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:59:23,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:59:23,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:59:23,310 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:59:23,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:59:23,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:59:51,566 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:59:51,569 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
23:59:52,781 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:59:55,89 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
23:59:59,610 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:00:07,900 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:07,902 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:00:08,914 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:10,203 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:00:10,205 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:10,722 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:11,310 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:13,417 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:15,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:00:17,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 25%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_update_with_limit_on_static_column_with_empty_partitions 
-------------------------------- live log call ---------------------------------
00:00:22,89 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:00:22,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:00:22,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:00:22,335 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:00:22,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:00:22,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:00:59,30 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:00:59,34 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:01:00,42 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:01:01,949 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:01:05,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:01:15,225 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:01:15,227 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:15,410 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:15,412 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:01:16,235 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:16,520 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:18,40 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:18,728 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:22,352 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:01:22,640 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 27%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_update_with_limit_on_static_column_with_not_empty_partitions 
-------------------------------- live log call ---------------------------------
00:01:28,652 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:01:28,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:01:28,805 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:01:28,899 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:01:28,982 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:01:29,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:01:57,155 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:01:57,158 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:01:58,167 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:01:59,975 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:02:03,687 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:02:10,909 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:02:13,584 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:13,586 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:02:14,594 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:15,763 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:02:15,764 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:16,502 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:16,770 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:18,877 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:20,915 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:02:22,486 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 29%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_update_with_limit_on_regular_column 
-------------------------------- live log call ---------------------------------
00:02:26,909 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:02:27,51 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:02:27,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:02:27,213 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:02:27,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:02:27,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:02:55,486 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:02:55,489 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:02:56,599 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:02:58,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:03:02,18 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:03:11,845 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:11,847 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:03:12,854 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:14,90 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:03:14,92 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:14,863 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:15,198 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:17,203 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:19,177 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:03:20,913 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 31%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_complementary_update_with_limit_and_rows_between 
-------------------------------- live log call ---------------------------------
00:03:24,945 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:03:25,30 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:03:25,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:03:25,190 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:03:25,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:03:25,348 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:03:45,369 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:03:52,538 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:03:52,540 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:03:53,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:03:55,860 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:03:59,673 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:04:08,893 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:08,894 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:04:10,104 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:11,129 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:04:11,132 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:12,136 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:12,212 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:14,41 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:16,826 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:04:17,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 32%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_partition_deletion_on_skinny_table 
-------------------------------- live log call ---------------------------------
00:04:22,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:04:22,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:04:22,360 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:04:22,452 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:04:22,539 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:04:22,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:04:50,694 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:04:50,697 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:04:51,705 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:04:53,512 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:04:57,424 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:05:07,44 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:07,47 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:05:08,255 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:09,332 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:05:09,335 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:10,339 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:10,364 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:12,646 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:14,76 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:05:17,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 34%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_partition_deletion_on_wide_table 
-------------------------------- live log call ---------------------------------
00:05:19,956 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:05:20,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:05:20,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:05:20,203 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:05:20,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:05:20,358 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:05:48,451 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:05:48,453 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:05:49,561 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:05:51,770 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:05:55,180 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:05:57,573 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:05:58,683 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:00,688 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:04,499 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:04,832 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:04,835 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:06:05,844 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:07,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:11,263 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:06:12,829 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 36%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_row_deletion_on_wide_table 
-------------------------------- live log call ---------------------------------
00:06:17,971 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:06:18,56 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:06:18,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:06:18,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:06:18,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:06:18,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:06:46,267 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:06:46,271 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:06:47,281 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:06:49,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:06:53,803 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:07:03,636 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:03,638 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:07:04,647 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:05,142 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:07:05,144 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:06,350 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:06,754 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:08,156 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:11,268 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:07:11,566 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 37%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_range_deletion_on_wide_table 
-------------------------------- live log call ---------------------------------
00:07:16,755 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:07:16,840 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:07:16,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:07:17,2 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:07:17,86 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:07:17,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:07:45,225 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:07:45,227 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:07:46,236 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:07:48,243 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:07:52,457 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:08:01,645 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:01,648 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:08:02,757 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:03,885 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:08:03,887 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:04,865 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:05,94 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:06,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:08,877 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:10,709 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 39%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_mismatching_insertions_on_skinny_table 
-------------------------------- live log call ---------------------------------
00:08:14,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:08:14,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:08:14,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:08:15,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:08:15,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:08:15,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:08:43,203 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:08:43,206 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:08:44,416 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:08:46,725 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:08:50,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:08:59,543 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:08:59,546 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:09:00,654 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:01,915 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:09:01,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:02,763 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:03,21 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:05,328 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:06,475 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:09,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 41%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_mismatching_insertions_on_wide_table 
-------------------------------- live log call ---------------------------------
00:09:12,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:09:12,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:09:12,942 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:09:13,35 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:09:13,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:09:13,187 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:09:41,256 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:09:41,260 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:09:42,370 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:09:44,378 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:09:47,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:09:54,612 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:09:57,638 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:57,640 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:09:58,650 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:09:59,915 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:09:59,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:10:00,658 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:10:01,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:10:03,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:10:04,369 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:10:07,540 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 43%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_consistent_skinny_table 
-------------------------------- live log call ---------------------------------
00:10:10,813 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:10:10,899 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:10:10,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:10:11,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:10:11,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:10:11,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 44%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_consistent_wide_table 
-------------------------------- live log call ---------------------------------
00:10:31,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:10:31,271 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:10:31,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:10:31,429 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:10:31,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:10:31,581 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 46%]
replica_side_filtering_test.py::TestSecondaryIndexes::test_count 
-------------------------------- live log call ---------------------------------
00:10:51,309 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:10:51,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:10:51,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:10:51,583 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:10:51,670 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:10:51,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:11:19,951 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:11:19,954 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:11:21,63 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:11:23,272 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:11:27,301 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
00:11:27,324 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
00:11:27,339 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 48%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_on_skinny_table 
-------------------------------- live log call ---------------------------------
00:11:27,768 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:11:27,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:11:27,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:11:28,30 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:11:28,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:11:28,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:11:55,264 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:11:55,267 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:11:56,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:11:58,585 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_on_wide_table 
-------------------------------- live log call ---------------------------------
00:12:03,198 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:12:03,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:12:03,359 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:12:03,453 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:12:03,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:12:03,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:12:30,707 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:12:30,710 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:12:31,819 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:12:34,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:12:38,39 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 51%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_on_static_column_with_empty_partition 
-------------------------------- live log call ---------------------------------
00:12:38,630 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:12:38,716 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:12:38,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:12:38,881 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:12:38,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:12:39,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:13:06,157 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:13:06,160 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:13:07,169 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:13:09,278 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 53%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_on_static_column_with_not_empty_partition 
-------------------------------- live log call ---------------------------------
00:13:14,62 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:13:14,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:13:14,215 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:13:14,308 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:13:14,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:13:14,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:13:41,767 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:13:41,771 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:13:42,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:13:44,893 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:13:48,505 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 55%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_on_collection 
-------------------------------- live log call ---------------------------------
00:13:49,632 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:13:49,719 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:13:49,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:13:49,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:13:49,962 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:13:50,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:14:17,82 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:14:17,85 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:14:18,296 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:14:20,305 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:14:23,716 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 56%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_partition_key_column_with_empty_partitions 
-------------------------------- live log call ---------------------------------
00:14:26,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:14:26,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:14:26,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:14:26,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:14:26,387 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:14:26,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:14:45,453 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:14:52,617 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:14:52,620 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:14:53,633 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:14:55,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:14:59,452 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:15:08,919 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:08,921 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:15:10,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:12,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:12,216 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:15:12,217 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:13,323 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:15,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:16,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:15:19,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 58%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_partition_key_column_with_not_empty_partitions 
-------------------------------- live log call ---------------------------------
00:15:22,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:15:22,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:15:22,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:15:22,318 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:15:22,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:15:22,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:15:49,602 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:15:49,606 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:15:50,614 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:15:52,621 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:15:56,232 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:16:03,254 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:16:06,40 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:06,41 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:16:07,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:09,235 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:16:09,236 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:09,358 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:10,242 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:12,247 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:12,870 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:16:16,258 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 60%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_clustering_key_column 
-------------------------------- live log call ---------------------------------
00:16:20,78 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:16:20,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:16:20,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:16:20,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:16:20,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:16:20,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:16:39,199 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:16:46,366 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:16:46,369 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:16:47,479 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:16:49,688 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:16:53,100 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:17:03,743 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:03,745 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:17:04,855 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:06,245 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:17:06,247 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:06,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:07,253 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:09,561 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:10,874 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:13,771 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 62%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_static_column_with_empty_partitions 
-------------------------------- live log call ---------------------------------
00:17:16,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:17:16,935 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:17:17,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:17:17,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:17:17,261 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:17:17,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:17:36,75 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:17:43,241 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:17:43,244 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:17:44,253 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:17:46,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:17:50,374 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:17:57,195 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:17:59,639 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:17:59,642 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:18:00,650 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:02,458 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:03,70 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:18:03,71 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:04,76 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:05,881 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:06,571 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:10,293 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 63%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_static_column_with_empty_partitions_and_rows_after 
-------------------------------- live log call ---------------------------------
00:18:12,824 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:18:12,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:18:12,977 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:18:13,69 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:18:13,153 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:18:13,220 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:18:40,410 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:18:40,414 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:18:41,526 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:18:43,735 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:18:47,649 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:18:54,570 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:18:56,841 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:56,843 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:18:57,851 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:59,959 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:18:59,968 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:18:59,969 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:00,974 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:02,879 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:04,273 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:07,391 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 65%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions 
-------------------------------- live log call ---------------------------------
00:19:09,859 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:19:09,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:19:10,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:19:10,107 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:19:10,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:19:10,259 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:19:29,220 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:19:36,375 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:19:36,378 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:19:37,387 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:19:39,696 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:19:44,112 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:19:52,803 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:52,805 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:19:53,812 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:55,720 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:55,978 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:19:55,979 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:57,85 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:19:58,890 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:00,34 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:03,2 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 67%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions_and_rows_after 
-------------------------------- live log call ---------------------------------
00:20:05,869 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:20:05,954 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:20:06,21 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:20:06,114 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:20:06,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:20:06,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:20:33,423 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:20:33,427 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:20:34,537 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:20:36,646 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:20:41,163 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:20:49,782 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:49,784 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:20:50,792 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:52,700 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:53,30 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:20:53,31 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:54,137 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:56,343 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:20:56,914 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:00,654 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 68%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_on_regular_column 
-------------------------------- live log call ---------------------------------
00:21:02,888 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:21:02,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:21:03,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:21:03,133 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:21:03,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:21:03,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:21:30,254 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:21:30,257 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:21:31,266 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:21:33,274 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:21:37,388 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:21:47,581 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:47,583 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:21:48,595 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:50,143 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:21:50,145 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:50,704 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:51,150 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:52,955 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:54,115 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:21:56,365 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 70%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_and_rows_after 
-------------------------------- live log call ---------------------------------
00:22:00,641 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:22:00,726 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:22:00,793 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:22:00,886 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:22:00,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:22:01,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:22:28,123 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:22:28,127 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:22:29,236 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:22:31,44 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:22:34,455 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:22:44,463 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:44,465 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:22:45,472 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:47,581 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:47,798 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:22:47,799 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:48,905 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:51,11 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:51,895 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:22:54,521 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 72%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_deletion_with_limit_and_rows_between 
-------------------------------- live log call ---------------------------------
00:22:57,653 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:22:57,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:22:57,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:22:57,900 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:22:57,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:22:58,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:23:25,205 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:23:25,211 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:23:26,421 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:23:28,329 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:23:32,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:23:41,578 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:41,580 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:23:42,689 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:44,807 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:23:44,808 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:44,898 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:45,913 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:48,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:49,312 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:23:52,431 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 74%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_update_with_limit_on_static_column_with_empty_partitions 
-------------------------------- live log call ---------------------------------
00:23:54,662 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:23:54,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:23:54,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:23:54,908 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:23:54,992 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:23:55,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:24:22,172 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:24:22,176 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:24:23,186 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:24:24,994 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:24:29,610 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:24:38,623 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:38,625 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:24:39,635 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:41,643 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:41,810 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:24:41,811 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:43,17 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:45,22 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:45,656 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:24:48,731 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 75%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_update_with_limit_on_static_column_with_not_empty_partitions 
-------------------------------- live log call ---------------------------------
00:24:51,667 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:24:51,751 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:24:51,820 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:24:51,915 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:24:51,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:24:52,67 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:25:11,22 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:25:18,180 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:25:18,183 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:25:19,295 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:25:21,303 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:25:25,417 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:25:34,674 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:34,676 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:25:35,885 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:37,792 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:37,819 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:25:37,821 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:38,824 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:40,930 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:42,6 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:25:45,141 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 77%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_update_with_limit_on_regular_column 
-------------------------------- live log call ---------------------------------
00:25:47,812 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:25:47,898 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:25:47,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:25:48,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:25:48,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:25:48,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:26:15,274 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:26:15,278 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:26:16,487 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:26:18,395 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:26:21,906 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:26:31,622 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:31,625 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:26:32,634 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:34,843 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:34,932 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:26:34,933 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:36,39 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:38,346 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:38,555 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:26:42,155 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 79%]
replica_side_filtering_test.py::TestAllowFiltering::test_complementary_update_with_limit_and_rows_between 
-------------------------------- live log call ---------------------------------
00:26:44,562 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:26:44,647 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:26:44,715 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:26:44,807 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:26:44,892 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:26:44,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:27:03,880 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:27:11,62 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:27:11,69 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:27:12,178 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:27:13,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:27:18,198 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:27:25,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:27:27,501 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:27,503 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:27:28,611 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:30,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:30,708 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:27:30,710 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:31,817 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:33,724 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:34,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:27:37,735 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 81%]
replica_side_filtering_test.py::TestAllowFiltering::test_partition_deletion_on_skinny_table 
-------------------------------- live log call ---------------------------------
00:27:40,810 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:27:40,895 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:27:40,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:27:41,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:27:41,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:27:41,209 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:27:59,906 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:28:07,76 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:28:07,82 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:28:08,91 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:28:10,0 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:28:14,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:28:21,337 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:28:24,496 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:24,498 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:28:25,605 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:26,963 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:28:26,965 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:27,312 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:27,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:30,77 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:31,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:28:34,288 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 82%]
replica_side_filtering_test.py::TestAllowFiltering::test_partition_deletion_on_wide_table 
-------------------------------- live log call ---------------------------------
00:28:37,566 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:28:37,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:28:37,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:28:37,814 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:28:37,898 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:28:37,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:28:56,811 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:29:03,974 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:29:03,976 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:29:05,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:29:06,796 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:29:10,809 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:29:13,95 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:29:14,221 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:16,126 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:19,735 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:20,282 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:20,285 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:29:21,392 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:23,300 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:23,690 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:29:23,693 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:24,899 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:27,205 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:27,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:27,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:29:31,416 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 84%]
replica_side_filtering_test.py::TestAllowFiltering::test_row_deletion_on_wide_table 
-------------------------------- live log call ---------------------------------
00:29:34,659 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:29:34,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:29:34,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:29:34,904 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:29:34,989 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:29:35,55 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:29:53,757 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:30:00,924 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:30:00,927 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:30:02,35 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:30:03,844 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:30:07,657 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:30:18,312 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:18,315 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:30:19,325 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:20,821 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:30:20,823 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:21,433 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:21,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:24,33 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:25,647 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:30:28,646 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 86%]
------------------------------ live log teardown -------------------------------
00:30:30,922 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down

replica_side_filtering_test.py::TestAllowFiltering::test_range_deletion_on_wide_table 
-------------------------------- live log call ---------------------------------
00:30:31,670 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:30:31,755 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:30:31,823 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:30:31,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:30:32,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:30:32,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:30:59,127 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:30:59,131 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:31:00,139 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:31:02,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:31:06,61 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:31:15,505 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:15,507 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:31:16,616 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:18,523 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:18,814 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:31:18,815 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:19,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:21,926 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:22,537 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:31:25,937 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 87%]
replica_side_filtering_test.py::TestAllowFiltering::test_mismatching_insertions_on_skinny_table 
-------------------------------- live log call ---------------------------------
00:31:28,423 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:31:28,509 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:31:28,577 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:31:28,671 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:31:28,756 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:31:28,823 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:31:55,883 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:31:55,887 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:31:57,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:31:59,105 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:32:03,318 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:32:13,238 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:13,241 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:32:14,248 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:15,581 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:32:15,583 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:16,357 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:16,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:18,594 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:20,672 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:32:22,204 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 89%]
replica_side_filtering_test.py::TestAllowFiltering::test_mismatching_insertions_on_wide_table 
-------------------------------- live log call ---------------------------------
00:32:26,429 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:32:26,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:32:26,581 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:32:26,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:32:26,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:32:26,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:32:45,745 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:32:52,912 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:32:52,914 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:32:54,123 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:32:56,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:32:59,843 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:33:10,279 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:10,281 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:33:11,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:12,596 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:33:12,598 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:13,597 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:13,604 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:15,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:17,408 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:19,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:33:22,910 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 91%]
replica_side_filtering_test.py::TestAllowFiltering::test_consistent_skinny_table 
-------------------------------- live log call ---------------------------------
00:33:24,431 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:33:24,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:33:24,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:33:24,675 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:33:24,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:33:24,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 93%]
replica_side_filtering_test.py::TestAllowFiltering::test_consistent_wide_table 
-------------------------------- live log call ---------------------------------
00:33:42,549 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:33:42,636 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:33:42,703 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:33:42,795 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:33:42,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:33:42,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 94%]
replica_side_filtering_test.py::TestAllowFiltering::test_count 
-------------------------------- live log call ---------------------------------
00:34:01,918 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:34:02,7 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:34:02,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:34:02,168 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:34:02,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:34:02,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:34:29,426 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:34:29,430 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:34:30,440 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:34:32,248 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:34:36,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:34:36,780 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
00:34:36,800 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
00:34:36,815 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 96%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_missed_by_transient_replica 
-------------------------------- live log call ---------------------------------
00:34:37,347 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:34:37,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:34:37,508 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:34:37,604 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:34:37,691 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:34:37,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 98%]
replica_side_filtering_test.py::TestAllowFiltering::test_update_only_on_transient_replica 
-------------------------------- live log call ---------------------------------
00:34:57,215 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:34:57,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:34:57,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:34:57,467 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:34:57,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:34:57,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [100%]
===Flaky Test Report===

test_update_on_skinny_table passed 1 out of the required 1 times. Success!
test_update_on_wide_table passed 1 out of the required 1 times. Success!
test_update_on_static_column_with_empty_partition passed 1 out of the required 1 times. Success!
test_update_on_static_column_with_not_empty_partition passed 1 out of the required 1 times. Success!
test_update_on_collection passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_partition_key_column_with_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_partition_key_column_with_not_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_clustering_key_column passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_empty_partitions_and_rows_after passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions_and_rows_after passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_regular_column passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_and_rows_after passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_and_rows_between passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_on_static_column_with_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_on_static_column_with_not_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_on_regular_column passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_and_rows_between passed 1 out of the required 1 times. Success!
test_partition_deletion_on_skinny_table passed 1 out of the required 1 times. Success!
test_partition_deletion_on_wide_table passed 1 out of the required 1 times. Success!
test_row_deletion_on_wide_table passed 1 out of the required 1 times. Success!
test_range_deletion_on_wide_table passed 1 out of the required 1 times. Success!
test_mismatching_insertions_on_skinny_table passed 1 out of the required 1 times. Success!
test_mismatching_insertions_on_wide_table passed 1 out of the required 1 times. Success!
test_consistent_skinny_table passed 1 out of the required 1 times. Success!
test_consistent_wide_table passed 1 out of the required 1 times. Success!
test_count passed 1 out of the required 1 times. Success!
test_update_on_skinny_table passed 1 out of the required 1 times. Success!
test_update_on_wide_table passed 1 out of the required 1 times. Success!
test_update_on_static_column_with_empty_partition passed 1 out of the required 1 times. Success!
test_update_on_static_column_with_not_empty_partition passed 1 out of the required 1 times. Success!
test_update_on_collection passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_partition_key_column_with_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_partition_key_column_with_not_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_clustering_key_column passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_empty_partitions_and_rows_after passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_static_column_with_not_empty_partitions_and_rows_after passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_on_regular_column passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_and_rows_after passed 1 out of the required 1 times. Success!
test_complementary_deletion_with_limit_and_rows_between passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_on_static_column_with_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_on_static_column_with_not_empty_partitions passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_on_regular_column passed 1 out of the required 1 times. Success!
test_complementary_update_with_limit_and_rows_between passed 1 out of the required 1 times. Success!
test_partition_deletion_on_skinny_table passed 1 out of the required 1 times. Success!
test_partition_deletion_on_wide_table passed 1 out of the required 1 times. Success!
test_row_deletion_on_wide_table passed 1 out of the required 1 times. Success!
test_range_deletion_on_wide_table passed 1 out of the required 1 times. Success!
test_mismatching_insertions_on_skinny_table passed 1 out of the required 1 times. Success!
test_mismatching_insertions_on_wide_table passed 1 out of the required 1 times. Success!
test_consistent_skinny_table passed 1 out of the required 1 times. Success!
test_consistent_wide_table passed 1 out of the required 1 times. Success!
test_count passed 1 out of the required 1 times. Success!
test_update_missed_by_transient_replica passed 1 out of the required 1 times. Success!
test_update_only_on_transient_replica passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 58 passed in 2856.94 seconds =========================
[msx] rc = 0
