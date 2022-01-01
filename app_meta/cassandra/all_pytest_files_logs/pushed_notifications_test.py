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
08:28:42,448 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:28:42,533 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:28:42,534 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:28:42,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:28:42,602 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:28:42,692 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:28:42,777 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:28:42,777 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:28:42,842 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:28:42,843 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:28:42,933 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:28:43,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:28:43,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:28:43,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:28:43,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 14%]
pushed_notifications_test.py::TestPushedNotifications::test_move_single_node_localhost 
-------------------------------- live log call ---------------------------------
08:30:02,872 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:02,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:30:02,957 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:30:03,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,114 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:03,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:30:03,199 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:30:03,265 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,356 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:03,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:30:03,441 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:30:03,507 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:03,644 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:30:03,645 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,694 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:03,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:30:03,779 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,828 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:03,914 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:30:03,914 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:03,964 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:04,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:30:04,48 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:04,102 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:04,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:30:04,190 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:30:04,239 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:30:04,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:30:04,324 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 28%]
pushed_notifications_test.py::TestPushedNotifications::test_restart_node 
-------------------------------- live log call ---------------------------------
08:31:25,912 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:31:25,998 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:31:25,998 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:31:26,64 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:31:26,64 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:31:26,155 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:31:26,241 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:31:26,241 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:31:26,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:31:26,307 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:32:04,838 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
08:32:27,998 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
08:32:51,68 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
08:33:14,82 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
PASSED                                                                   [ 42%]
pushed_notifications_test.py::TestPushedNotifications::test_restart_node_localhost 
-------------------------------- live log call ---------------------------------
08:33:37,677 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:33:37,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:33:37,762 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:37,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:33:37,830 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:37,922 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:33:38,34 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:33:38,34 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:38,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:33:38,101 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:38,154 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:33:38,238 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:33:38,239 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:38,288 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:33:38,373 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:33:38,373 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:38,422 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:33:38,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:33:38,506 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:33:38,556 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:33:38,640 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:33:38,641 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:34:26,108 cassandra.cluster WARNING Host 127.0.0.1:9044 has been marked down
08:34:27,214 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
08:34:29,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
08:34:33,434 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
08:34:41,59 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9044, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9044)]. Last error: Connection refused
PASSED                                                                   [ 57%]
pushed_notifications_test.py::TestPushedNotifications::test_add_and_remove_node 
-------------------------------- live log call ---------------------------------
08:34:48,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:34:49,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:34:49,38 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:34:49,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:34:49,105 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:35:25,276 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:35:25,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:35:25,368 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:35:25,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:35:25,440 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 71%]
pushed_notifications_test.py::TestPushedNotifications::test_schema_changes 
-------------------------------- live log call ---------------------------------
08:37:50,178 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:37:50,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:37:50,265 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:37:50,331 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:37:50,331 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:37:50,426 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:37:50,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:37:50,512 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:37:50,578 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:37:50,578 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:38:06,300 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks is higher than the number of nodes 2
08:38:09,303 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 85%]
pushed_notifications_test.py::TestVariousNotifications::test_tombstone_failure_threshold_message 
-------------------------------- live log call ---------------------------------
08:38:14,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:38:14,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:38:14,907 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:38:14,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:38:14,975 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:38:15,67 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:38:15,153 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:38:15,153 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:38:15,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:38:15,219 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:38:15,312 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:38:15,397 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:38:15,397 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:38:15,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:38:15,463 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

========================== 7 passed in 598.51 seconds ==========================
[msx] rc = 0
