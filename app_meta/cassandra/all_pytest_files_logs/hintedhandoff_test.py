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
05:29:30,924 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:29:31,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:29:31,8 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:29:31,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:29:31,77 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:29:31,168 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:29:31,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:29:31,251 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:29:31,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:29:31,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_enabled 
-------------------------------- live log call ---------------------------------
05:30:17,33 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:30:17,117 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:30:17,117 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:30:17,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:30:17,183 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:30:17,274 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:30:17,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:30:17,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:30:17,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:30:17,431 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:31:05,747 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
05:31:05,748 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:31:06,754 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:31:08,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 37%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_setmaxwindow 
-------------------------------- live log call ---------------------------------
05:31:12,423 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:31:12,508 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:31:12,508 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:31:12,595 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:31:12,595 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:31:12,688 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:31:12,772 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:31:12,773 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:31:12,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:31:12,840 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:32:32,486 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
05:32:37,603 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
05:32:38,710 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:32:40,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:32:45,227 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:32:54,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_dc_disabled 
-------------------------------- live log call ---------------------------------
05:33:01,745 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:33:01,833 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:33:01,833 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:33:01,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:33:01,901 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:33:01,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:33:02,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:33:02,77 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:33:02,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:33:02,144 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 62%]
hintedhandoff_test.py::TestHintedHandoffConfig::test_hintedhandoff_dc_reenabled 
-------------------------------- live log call ---------------------------------
05:33:47,130 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:33:47,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:33:47,214 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:33:47,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:33:47,286 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:33:47,379 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:33:47,464 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:33:47,465 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:33:47,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:33:47,531 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
hintedhandoff_test.py::TestHintedHandoff::test_hintedhandoff_decom SKIPPED [ 87%]
hintedhandoff_test.py::TestHintedHandoff::test_hintedhandoff_window 
-------------------------------- live log call ---------------------------------
05:34:52,349 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:34:52,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:34:52,435 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:34:52,502 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:34:52,502 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:34:52,593 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:34:52,677 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:34:52,678 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:34:52,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:34:52,744 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:35:14,286 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
05:35:15,293 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:17,102 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:20,613 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:28,740 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:28,740 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:29,747 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:31,852 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:35,562 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:38,113 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
05:35:38,114 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:35:39,174 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:35:41,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:35:44,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:35:44,788 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:35:52,909 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
05:36:00,830 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
05:36:11,357 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_hintedhandoff_disabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_enabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_setmaxwindow passed 1 out of the required 1 times. Success!
test_hintedhandoff_dc_disabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_dc_reenabled passed 1 out of the required 1 times. Success!
test_hintedhandoff_window passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 6 passed, 2 skipped in 424.14 seconds =====================
[msx] rc = 0
