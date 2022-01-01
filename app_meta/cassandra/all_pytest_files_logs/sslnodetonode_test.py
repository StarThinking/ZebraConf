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
11:36:01,952 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:02,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:02,38 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:02,107 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:02,108 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:02,202 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:02,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:02,289 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:02,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:02,355 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:02,409 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:02,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:02,493 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:02,544 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:02,628 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:02,628 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 12%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_correct_hostname_with_validation 
-------------------------------- live log call ---------------------------------
11:36:27,455 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:27,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:27,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:27,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:27,608 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:27,699 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:27,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:27,784 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:27,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:27,849 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:27,903 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:27,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:27,988 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:28,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:28,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:28,123 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_wrong_hostname_no_validation 
-------------------------------- live log call ---------------------------------
11:36:57,48 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:57,135 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:57,135 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:57,202 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:57,202 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:57,293 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:57,378 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:57,378 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:57,444 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:57,444 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:57,497 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:57,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:36:57,582 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:36:57,633 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:36:57,716 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:36:57,716 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 37%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_wrong_hostname_with_validation 
-------------------------------- live log call ---------------------------------
11:37:26,574 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:37:26,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:37:26,662 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:37:26,730 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:37:26,730 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:37:26,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:37:26,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:37:26,908 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:37:26,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:37:26,974 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:37:27,28 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:37:27,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:37:27,112 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:37:27,162 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:37:27,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:37:27,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_client_auth_required_fail 
-------------------------------- live log call ---------------------------------
11:39:01,551 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:39:01,658 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:39:01,658 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:39:01,727 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:39:01,727 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:39:01,837 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:39:01,921 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:39:01,921 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:39:01,987 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:39:01,987 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:39:02,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:39:02,125 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:39:02,125 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:39:02,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:39:02,259 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:39:02,259 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 62%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ssl_client_auth_required_succeed 
-------------------------------- live log call ---------------------------------
11:40:36,297 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:40:36,383 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:40:36,383 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:40:36,450 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:40:36,450 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:40:36,541 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:40:36,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:40:36,626 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:40:36,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:40:36,692 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:40:36,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:40:36,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:40:36,849 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:40:36,899 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:40:36,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:40:36,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_ca_mismatch 
-------------------------------- live log call ---------------------------------
11:41:05,245 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:41:05,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:41:05,354 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:41:05,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:41:05,423 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:41:05,515 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:41:05,600 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:41:05,600 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:41:05,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:41:05,666 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:41:05,720 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:41:05,803 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:41:05,803 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:41:05,854 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:41:05,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:41:05,939 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 87%]
sslnodetonode_test.py::TestNodeToNodeSSLEncryption::test_optional_outbound_tls 
-------------------------------- live log call ---------------------------------
11:42:38,797 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:42:38,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:42:38,908 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:42:38,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:42:38,976 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:42:39,68 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:42:39,153 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:42:39,154 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:42:39,219 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:42:39,219 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:42:39,273 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:42:39,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:42:39,357 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:42:39,408 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:42:39,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:42:39,493 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:43:03,984 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:43:04,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:43:04,77 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:43:19,200 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:43:19,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:43:19,292 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:43:26,813 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:43:26,815 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
11:43:26,818 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:43:27,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:43:29,525 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:43:41,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:43:41,547 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:43:41,547 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:43:56,679 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:43:56,773 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:43:56,773 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:43:56,814 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:43:56,814 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
11:43:56,817 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:43:57,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:44:00,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:44:04,542 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:44:26,815 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:44:26,815 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
11:44:26,817 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:44:27,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:44:27,921 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:44:29,725 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:44:30,127 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:44:33,235 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
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

========================== 8 passed in 521.01 seconds ==========================
[msx] rc = 0
