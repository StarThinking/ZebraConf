cassandra hintedhandoff_test.py true true
the_test is hintedhandoff_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 8 items

hintedhandoff_test.py::TestHintedHandoffConfig::test_nodetool SKIPPED    [ 12%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_disabled 
-------------------------------- live log call ---------------------------------
19:30:21,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:30:21,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:30:21,398 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:30:21,490 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:30:21,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:30:21,641 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 25%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_enabled 
-------------------------------- live log call ---------------------------------
19:31:07,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:31:07,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:31:07,256 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:31:07,348 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:31:07,432 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:31:07,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 37%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_setmaxwindow 
-------------------------------- live log call ---------------------------------
19:32:12,18 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:32:12,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:32:12,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:32:12,267 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:32:12,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:32:12,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:33:33,911 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:33:38,314 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:33:38,337 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:33:39,343 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:33:41,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:33:46,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:33:54,907 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_dc_disabled 
-------------------------------- live log call ---------------------------------
19:34:02,601 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:34:02,687 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:34:02,760 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:34:02,853 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:34:02,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:34:03,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 62%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_dc_reenabled 
-------------------------------- live log call ---------------------------------
19:34:48,220 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:34:48,304 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:34:48,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:34:48,468 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:34:48,553 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:34:48,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:35:44,757 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:35:44,758 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:35:45,764 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:35:47,670 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:35:52,82 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 75%]
hintedhandoff_test.py::TestHintedHandoff::test_hintedhandoff_decom SKIPPED [ 87%]
hintedhandoff_test.py::TestHintedHandoff::test_hintedhandoff_window 
-------------------------------- live log call ---------------------------------
19:35:53,702 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:35:53,788 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:35:53,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:35:53,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:35:54,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:35:54,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:36:15,792 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
19:36:16,805 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:18,811 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:22,722 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:31,650 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:31,851 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:32,953 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:35,160 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:39,571 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:39,829 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
19:36:39,830 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:36:40,878 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:36:43,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:36:47,295 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:36:47,997 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:36:54,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
19:37:04,339 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
19:37:12,460 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_hintedhandoff_disabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_enabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_setmaxwindow passed 1 out of the required 1 times. Success!
test_hintedhandoff_dc_disabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_dc_reenabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_window passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 6 passed, 2 skipped in 435.89 seconds =====================
[msx] rc = 0
