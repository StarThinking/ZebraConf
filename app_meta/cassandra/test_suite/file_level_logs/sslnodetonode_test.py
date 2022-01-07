cassandra sslnodetonode_test.py true true
the_test is sslnodetonode_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 8 items

sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_enabled 
-------------------------------- live log call ---------------------------------
01:45:23,123 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:23,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:23,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:23,374 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:23,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:45:23,530 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:45:23,583 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:23,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:23,719 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:23,805 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 12%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_correct_hostname_with_validation 
-------------------------------- live log call ---------------------------------
01:45:51,100 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:51,188 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:51,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:51,351 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:51,438 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:45:51,504 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:45:51,558 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:51,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:51,693 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:51,778 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 25%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_wrong_hostname_no_validation 
-------------------------------- live log call ---------------------------------
01:46:20,785 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:20,896 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:20,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:21,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:21,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:46:21,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:46:21,262 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:21,345 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:21,396 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:21,480 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 37%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_wrong_hostname_with_validation 
-------------------------------- live log call ---------------------------------
01:46:50,678 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:50,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:50,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:50,948 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:51,34 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:46:51,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:46:51,155 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:51,239 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:51,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:51,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 50%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_client_auth_required_fail 
-------------------------------- live log call ---------------------------------
01:48:25,880 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:25,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:26,35 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:26,127 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:26,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:48:26,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:48:26,334 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:26,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:26,469 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:26,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 62%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_client_auth_required_succeed 
-------------------------------- live log call ---------------------------------
01:50:00,429 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:00,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:00,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:00,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:00,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:50:00,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:50:00,879 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:00,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:01,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:01,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 75%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ca_mismatch 
-------------------------------- live log call ---------------------------------
01:50:29,811 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:29,897 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:29,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:30,59 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:30,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:50:30,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:50:30,264 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:30,348 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:30,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:30,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 87%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_optional_outbound_tls 
-------------------------------- live log call ---------------------------------
01:52:03,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:03,513 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:03,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:03,700 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:03,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:52:03,851 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:52:03,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:03,989 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:04,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:04,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:52:29,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:29,133 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:44,455 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:44,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:52:51,854 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:52:51,855 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
01:52:51,859 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:52:52,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:52:55,168 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:52:59,180 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:06,864 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:53:06,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:21,855 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:53:21,856 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
01:53:21,859 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:22,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:53:22,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:53:22,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:25,178 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:28,791 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:36,613 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:50,951 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:53:51,856 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:53:51,857 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:53:52,959 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:53:54,964 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:53:59,75 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_ssl_enabled passed 1 out of the required 1 times. Success!
test_ssl_correct_hostname_with_validation passed 1 out of the required 1 times. Success!
test_ssl_wrong_hostname_no_validation passed 1 out of the required 1 times. Success!
test_ssl_wrong_hostname_with_validation passed 1 out of the required 1 times. Success!
test_ssl_client_auth_required_fail passed 1 out of the required 1 times. Success!
test_ssl_client_auth_required_succeed passed 1 out of the required 1 times. Success!
test_ca_mismatch passed 1 out of the required 1 times. Success!
test_optional_outbound_tls passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 8 passed in 525.45 seconds ==========================
[msx] rc = 0
