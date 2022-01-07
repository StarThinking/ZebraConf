cassandra scrub_test.py true true
the_test is scrub_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 7 items

scrub_test.py::TestScrubIndexes::test_scrub_static_table 
-------------------------------- live log call ---------------------------------
01:00:41,668 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:00:41,758 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:00:41,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:01:17,863 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:01:17,866 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:01:18,873 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 14%]
scrub_test.py::TestScrubIndexes::test_standalone_scrub 
-------------------------------- live log call ---------------------------------
01:01:21,733 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:01:21,820 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:01:21,887 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:01:57,915 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:01:57,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:01:58,923 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 28%]
scrub_test.py::TestScrubIndexes::test_scrub_collections_table 
-------------------------------- live log call ---------------------------------
01:02:00,792 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:02:00,878 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:02:00,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 42%]
scrub_test.py::TestScrub::test_nodetool_scrub 
-------------------------------- live log call ---------------------------------
01:02:18,537 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:02:18,623 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:02:18,690 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 57%]
scrub_test.py::TestScrub::test_standalone_scrub 
-------------------------------- live log call ---------------------------------
01:02:45,556 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:02:45,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:02:45,710 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 71%]
scrub_test.py::TestScrub::test_standalone_scrub_essential_files_only 
-------------------------------- live log call ---------------------------------
01:03:10,570 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:03:10,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:03:10,723 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 85%]
scrub_test.py::TestScrub::test_scrub_with_UDT 
-------------------------------- live log call ---------------------------------
01:03:35,329 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:03:35,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:03:35,482 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_scrub_static_table passed 1 out of the required 1 times. Success!
test_standalone_scrub passed 1 out of the required 1 times. Success!
test_scrub_collections_table passed 1 out of the required 1 times. Success!
test_nodetool_scrub passed 1 out of the required 1 times. Success!
test_standalone_scrub passed 1 out of the required 1 times. Success!
test_standalone_scrub_essential_files_only passed 1 out of the required 1 times. Success!
test_scrub_with_UDT passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 7 passed in 185.24 seconds ==========================
[msx] rc = 0
