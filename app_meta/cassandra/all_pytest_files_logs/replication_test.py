cassandra replication_test.py true true
the_test is replication_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 15 items

replication_test.py::TestReplication::test_simple 
-------------------------------- live log call ---------------------------------
10:28:39,113 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:28:39,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:28:39,199 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:28:39,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:28:39,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:28:39,358 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:28:39,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:28:39,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:28:39,509 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:28:39,509 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:28:39,599 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:28:39,684 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:28:39,684 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:28:39,751 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:28:39,751 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  6%]
replication_test.py::TestReplication::test_network_topology 
-------------------------------- live log call ---------------------------------
10:30:51,5 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:30:51,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:30:51,91 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:30:51,157 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,247 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:30:51,332 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:30:51,332 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:30:51,399 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,490 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:30:51,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:30:51,574 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,640 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:30:51,640 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,731 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:30:51,816 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:30:51,816 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:30:51,882 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:51,972 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:30:52,56 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:30:52,56 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:52,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:30:52,125 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:30:52,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:30:52,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:30:52,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:30:52,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:30:52,367 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
PASSED                                                                   [ 13%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_gossiping_property_file_snitch 
-------------------------------- live log call ---------------------------------
10:33:13,207 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:33:13,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:33:13,294 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:13,360 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:33:13,361 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:13,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:33:13,536 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:33:13,536 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:13,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:33:13,603 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:13,693 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:33:13,778 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:33:13,778 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:13,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:33:13,844 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:13,899 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:33:13,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:33:13,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:14,34 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:33:14,119 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:33:14,119 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:33:14,192 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:33:14,279 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:33:14,279 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:02,696 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:34:02,697 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
10:34:03,806 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:34:03,906 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:34:06,14 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:34:06,15 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:34:09,830 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:34:10,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:34:18,555 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 20%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_gossiping_property_file_snitch 
-------------------------------- live log call ---------------------------------
10:34:38,235 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:34:38,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:34:38,322 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:38,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:34:38,390 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:38,485 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:34:38,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:34:38,573 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:38,639 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:34:38,639 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:38,731 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:34:38,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:34:38,815 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:38,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:34:38,882 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:38,937 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:34:39,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:34:39,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:39,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:34:39,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:34:39,157 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:34:39,207 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:34:39,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:34:39,292 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:35:27,701 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:35:27,702 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
10:35:28,809 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:35:28,909 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:35:30,615 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:35:30,715 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:35:34,727 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:35:35,328 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:35:43,553 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 26%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_gossiping_property_file_snitch_multi_dc 
-------------------------------- live log call ---------------------------------
10:36:02,302 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:02,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:36:02,389 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:02,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:36:02,456 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:02,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:02,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:36:02,634 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:02,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:36:02,701 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:02,795 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:02,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:36:02,882 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:02,949 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:36:02,949 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:03,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:03,126 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:36:03,126 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:03,192 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:36:03,192 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:03,283 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:03,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:36:03,369 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:03,436 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:36:03,436 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:03,527 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:03,614 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:36:03,614 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:36:03,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:36:03,681 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:36:03,735 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:03,822 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:36:03,823 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:03,872 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:03,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:36:03,957 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:04,6 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:04,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:36:04,91 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:04,142 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:04,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:36:04,265 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:04,315 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:04,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:36:04,401 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:36:04,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:36:04,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:36:04,535 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:36:54,849 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:36:54,851 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
10:36:55,858 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:36:56,58 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:36:56,101 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
10:36:57,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:36:57,964 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:36:58,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:36:59,67 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:37:01,674 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:37:02,175 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:37:03,579 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:37:10,96 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:37:10,597 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:37:10,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:37:24,851 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
10:37:24,853 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.6:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:37:24,942 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:37:25,945 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:37:26,748 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:37:27,951 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:37:28,252 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:37:32,567 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:37:40,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:37:58,439 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:37:58,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 33%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_gossiping_property_file_snitch_multi_dc 
-------------------------------- live log call ---------------------------------
10:38:33,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:33,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:38:33,839 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:33,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:38:33,907 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:33,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:34,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:38:34,84 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:38:34,150 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,241 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:34,328 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:38:34,328 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,394 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:38:34,395 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,485 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:34,570 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:38:34,570 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,636 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:38:34,637 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,727 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:34,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:38:34,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:38:34,879 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:34,969 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:38:35,55 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:38:35,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:38:35,121 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:38:35,176 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,261 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:38:35,261 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:35,311 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:38:35,396 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:35,446 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,533 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:38:35,533 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:35,584 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,671 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
10:38:35,671 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:35,722 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
10:38:35,808 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:38:35,859 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:38:35,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
10:38:35,945 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
10:39:26,107 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:39:26,108 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
10:39:26,110 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
10:39:27,114 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:39:27,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:39:27,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:39:29,320 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:39:29,321 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:39:29,521 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:39:32,708 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
10:39:33,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:39:33,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:39:33,134 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:39:33,733 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:39:35,638 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:39:39,247 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:39:40,351 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:39:41,353 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:39:41,554 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
10:39:46,467 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:39:54,990 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:39:57,697 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:40:02,313 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
10:40:25,77 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 59.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
10:40:35,4 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 71.04 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
PASSED                                                                   [ 40%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_property_file_snitch 
-------------------------------- live log call ---------------------------------
10:41:02,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:41:02,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:41:02,486 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:02,552 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:41:02,552 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:02,643 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:41:02,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:41:02,729 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:02,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:41:02,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:02,886 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:41:02,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:41:02,971 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:03,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:41:03,41 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:03,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:41:03,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:41:03,182 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:03,232 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:41:03,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:41:03,317 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:03,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:41:03,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:41:03,452 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:41:29,232 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
10:41:30,339 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:41:32,647 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:41:36,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:41:37,244 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
10:41:38,365 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:41:40,70 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:41:43,679 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:41:44,983 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:41:50,497 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:42:02,833 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:42:06,241 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 46%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_property_file_snitch 
-------------------------------- live log call ---------------------------------
10:42:34,505 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:42:34,591 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:42:34,591 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:34,658 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:42:34,658 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:34,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:42:34,836 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:42:34,836 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:34,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:42:34,904 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:34,995 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:42:35,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:42:35,81 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:35,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:42:35,148 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:35,203 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:42:35,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:42:35,289 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:35,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:42:35,425 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:42:35,425 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:42:35,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:42:35,561 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:42:35,561 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:43:01,159 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
10:43:02,165 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:43:04,373 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:43:08,85 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:43:09,172 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
10:43:10,192 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:43:11,997 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:43:15,406 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:43:16,7 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:43:23,527 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
10:43:29,946 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
10:43:41,674 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 53%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_yaml_file_snitch SKIPPED [ 60%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_yaml_file_snitch SKIPPED [ 66%]
replication_test.py::TestSnitchConfigurationUpdate::test_cannot_restart_with_different_rack 
-------------------------------- live log call ---------------------------------
10:44:06,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:06,513 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:44:06,513 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:06,579 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:44:06,579 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:06,633 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:06,718 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:44:06,718 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 73%]
replication_test.py::TestSnitchConfigurationUpdate::test_failed_snitch_update_gossiping_property_file_snitch 
-------------------------------- live log call ---------------------------------
10:44:24,332 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:24,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:44:24,419 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:24,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:44:24,485 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:24,575 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:24,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:44:24,661 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:24,729 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:44:24,730 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:24,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:24,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:44:24,907 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:24,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:44:24,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:25,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:25,113 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:44:25,113 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:25,162 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:25,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:44:25,247 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:44:25,296 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:44:25,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:44:25,385 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
replication_test.py::TestSnitchConfigurationUpdate::test_failed_snitch_update_property_file_snitch 
-------------------------------- live log call ---------------------------------
10:45:02,964 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:03,49 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:45:03,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:45:03,116 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:03,291 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:45:03,291 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:45:03,357 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,447 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:03,532 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:45:03,532 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:45:03,598 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,652 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:03,738 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:45:03,738 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,787 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:03,871 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:45:03,871 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:03,921 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:04,6 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:45:04,6 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 86%]
replication_test.py::TestSnitchConfigurationUpdate::test_failed_snitch_update_yaml_file_snitch SKIPPED [ 93%]
replication_test.py::TestSnitchConfigurationUpdate::test_switch_data_center_startup_fails 
-------------------------------- live log call ---------------------------------
10:45:41,899 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:41,987 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:45:41,987 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:42,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:45:42,54 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:45:42,109 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:45:42,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:45:42,198 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_simple passed 1 out of the required 1 times. Success!
test_network_topology passed 1 out of the required 1 times. Success!
test_rf_collapse_gossiping_property_file_snitch passed 1 out of the required 1 times. Success!
test_rf_expand_gossiping_property_file_snitch passed 1 out of the required 1 times. Success!
test_rf_collapse_gossiping_property_file_snitch_multi_dc passed 1 out of the required 1 times. Success!
test_rf_expand_gossiping_property_file_snitch_multi_dc passed 1 out of the required 1 times. Success!
test_rf_collapse_property_file_snitch passed 1 out of the required 1 times. Success!
test_rf_expand_property_file_snitch passed 1 out of the required 1 times. Success!
test_cannot_restart_with_different_rack passed 1 out of the required 1 times. Success!
test_failed_snitch_update_gossiping_property_file_snitch passed 1 out of the required 1 times. Success!
test_failed_snitch_update_property_file_snitch passed 1 out of the required 1 times. Success!
test_switch_data_center_startup_fails passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 12 passed, 3 skipped in 1040.61 seconds ====================
[msx] rc = 0
