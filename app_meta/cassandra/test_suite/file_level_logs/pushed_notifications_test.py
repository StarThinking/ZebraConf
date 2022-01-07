cassandra pushed_notifications_test.py true true
the_test is pushed_notifications_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 7 items

pushed_notifications_test.py::TestPushedNotifications::test_move_single_node 
-------------------------------- live log call ---------------------------------
22:32:53,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:32:53,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:32:54,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:32:54,124 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:32:54,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:32:54,274 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:32:54,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:32:54,449 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:32:54,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 14%]
pushed_notifications_test.py::TestPushedNotifications::test_move_single_node_localhost 
-------------------------------- live log call ---------------------------------
22:34:15,65 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:15,149 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:34:15,216 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:34:15,308 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:15,393 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:34:15,460 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:34:15,551 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:15,635 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:34:15,702 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:34:15,755 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:15,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:34:15,889 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:15,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:34:16,23 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:16,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:34:16,157 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:16,241 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:34:16,295 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:16,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:34:16,432 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:34:16,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 28%]
pushed_notifications_test.py::TestPushedNotifications::test_restart_node 
-------------------------------- live log call ---------------------------------
22:35:38,861 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:35:38,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:35:39,13 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:35:39,105 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:35:39,190 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:35:39,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:36:18,209 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
22:36:41,227 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
22:37:04,241 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
22:37:27,256 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
PASSED                                                                   [ 42%]
pushed_notifications_test.py::TestPushedNotifications::test_restart_node_localhost 
-------------------------------- live log call ---------------------------------
22:37:50,860 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:37:50,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:37:51,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:37:51,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:37:51,188 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:37:51,254 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:37:51,307 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:37:51,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:37:51,442 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:37:51,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:37:51,578 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:37:51,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:37:51,713 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:37:51,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:38:38,616 cassandra.cluster WARNING Host 127.0.0.1:9044 has been marked down
22:38:39,622 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
22:38:41,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
22:38:45,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
22:38:52,967 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
PASSED                                                                   [ 57%]
pushed_notifications_test.py::TestPushedNotifications::test_add_and_remove_node 
-------------------------------- live log call ---------------------------------
22:39:02,421 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:39:02,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:39:02,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:39:38,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:39:39,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:39:39,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 71%]
pushed_notifications_test.py::TestPushedNotifications::test_schema_changes 
-------------------------------- live log call ---------------------------------
22:42:03,951 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:42:04,37 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:42:04,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:42:04,194 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:42:04,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:42:04,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:42:21,378 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks is higher than the number of nodes 2
22:42:23,542 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 85%]
pushed_notifications_test.py::TestVariousNotifications::test_tombstone_failure_threshold_message 
-------------------------------- live log call ---------------------------------
22:42:28,851 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:42:28,936 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:42:29,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:42:29,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:42:29,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:42:29,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:42:29,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:42:29,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:42:29,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_move_single_node passed 1 out of the required 1 times. Success!
test_move_single_node_localhost passed 1 out of the required 1 times. Success!
test_restart_node passed 1 out of the required 1 times. Success!
test_restart_node_localhost passed 1 out of the required 1 times. Success!
test_add_and_remove_node passed 1 out of the required 1 times. Success!
test_schema_changes passed 1 out of the required 1 times. Success!
test_tombstone_failure_threshold_message passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 7 passed in 601.11 seconds ==========================
[msx] rc = 0
