cassandra refresh_test.py true true
the_test is refresh_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

refresh_test.py::TestRefresh::test_refresh_deadlock_startup 
-------------------------------- live log call ---------------------------------
23:04:29,815 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:04:29,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:04:29,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:04:30,23 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:04:30,107 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:05:02,2 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:05:02,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:05:06,653 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:05:06,657 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:05:07,662 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:05:09,668 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:05:14,79 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:05:23,203 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:05:39,142 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:06:15,334 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:07:24,505 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 115.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_refresh_deadlock_startup passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 236.92 seconds ==========================
[msx] rc = 0
