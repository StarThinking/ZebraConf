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
00:36:18,66 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:36:18,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:36:18,221 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:36:18,314 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:36:18,398 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:36:18,465 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:36:18,558 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:36:18,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:36:18,710 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  6%]
replication_test.py::TestReplication::test_network_topology 
-------------------------------- live log call ---------------------------------
00:38:26,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:38:27,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:38:27,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:38:27,191 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:38:27,275 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:38:27,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:38:27,433 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:38:27,518 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:38:27,584 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:38:27,675 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:38:27,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:38:27,825 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:38:27,917 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:38:28,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:38:28,67 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:38:28,159 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:38:28,243 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:38:28,309 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
PASSED                                                                   [ 13%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_gossiping_property_file_snitch 
-------------------------------- live log call ---------------------------------
00:40:56,696 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:40:56,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:40:56,848 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:40:56,940 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:40:57,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:40:57,90 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:40:57,182 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:40:57,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:40:57,332 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:40:57,387 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:40:57,471 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:40:57,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:40:57,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:40:57,658 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:40:57,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:41:46,686 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:41:46,687 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
00:41:47,698 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:41:47,699 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:41:49,606 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:41:49,706 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:41:53,319 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:41:54,321 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:42:00,240 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 20%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_gossiping_property_file_snitch 
-------------------------------- live log call ---------------------------------
00:42:22,770 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:42:22,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:42:22,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:42:23,20 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:42:23,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:42:23,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:42:23,276 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:42:23,360 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:42:23,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:42:23,483 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:42:23,567 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:42:23,617 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:42:23,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:42:23,752 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:42:23,836 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:43:12,781 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:43:12,782 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
00:43:13,890 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:43:13,891 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:43:15,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:43:15,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:43:20,214 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:43:20,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:43:28,237 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 26%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_gossiping_property_file_snitch_multi_dc 
-------------------------------- live log call ---------------------------------
00:43:49,770 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:49,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:43:49,924 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:43:50,18 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:50,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:43:50,170 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:43:50,277 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:50,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:43:50,429 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:43:50,522 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:50,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:43:50,673 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:43:50,776 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:50,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:43:50,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:43:51,20 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:51,104 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:43:51,171 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:43:51,227 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:51,313 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:43:51,363 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:51,447 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:43:51,498 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:51,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:43:51,671 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:51,755 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:43:51,805 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:51,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:43:51,940 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:43:52,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:44:43,568 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:44:43,569 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
00:44:44,575 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:44:44,675 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:44:46,580 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:44:46,881 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:44:51,92 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:44:51,193 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:44:58,9 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:45:00,315 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:45:13,570 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
00:45:13,570 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
00:45:14,353 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:45:14,653 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:45:14,754 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:45:15,757 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:45:16,860 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:45:17,61 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:45:20,574 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:45:21,175 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:45:27,393 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:45:29,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:45:44,540 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:45:45,242 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 33%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_gossiping_property_file_snitch_multi_dc 
-------------------------------- live log call ---------------------------------
00:46:25,296 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:25,387 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:46:25,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:46:25,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:25,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:46:25,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:46:25,789 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:25,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:46:25,939 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:46:26,31 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:26,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:46:26,181 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:46:26,273 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:26,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:46:26,425 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:46:26,517 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:26,601 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:46:26,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:46:26,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:26,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:46:26,858 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:26,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:46:26,991 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:27,76 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:46:27,137 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:27,221 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
00:46:27,271 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:27,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
00:46:27,405 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:46:27,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
00:47:19,110 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
00:47:19,111 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
00:47:20,118 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:47:20,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:47:21,825 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:47:22,327 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:47:26,137 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:47:26,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:47:33,457 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:47:35,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:47:49,111 cassandra.cluster WARNING Host 127.0.0.6:9042 has been marked down
00:47:49,112 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
00:47:50,203 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:47:50,204 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:47:51,707 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
00:47:51,907 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:47:52,8 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:47:52,409 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:47:55,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:47:56,822 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:48:02,337 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:48:04,948 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
00:48:18,84 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.6:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.6', 9042)]. Last error: Connection refused
00:48:21,293 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 28.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 40%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_property_file_snitch 
-------------------------------- live log call ---------------------------------
00:49:08,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:49:08,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:49:08,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:49:09,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:49:09,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:49:09,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:49:09,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:49:09,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:49:09,398 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:49:09,453 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:49:09,537 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:49:09,588 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:49:09,672 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:49:09,722 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:49:09,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:49:36,102 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:49:37,309 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:49:39,316 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:49:43,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:49:44,119 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
00:49:45,135 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:49:47,40 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:49:50,649 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:49:51,50 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:49:58,669 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:50:08,296 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:50:13,610 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 46%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_property_file_snitch 
-------------------------------- live log call ---------------------------------
00:50:42,607 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:50:42,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:50:42,760 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:50:42,853 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:50:42,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:50:43,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:50:43,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:50:43,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:50:43,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:50:43,302 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:50:43,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:50:43,467 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:50:43,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:50:43,603 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:50:43,686 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:51:10,131 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
00:51:11,238 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:51:13,246 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:51:17,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:51:18,145 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
00:51:19,166 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:51:21,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:51:24,881 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:51:25,82 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:51:33,704 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
00:51:38,719 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
00:51:49,748 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 53%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_collapse_yaml_file_snitch SKIPPED [ 60%]
replication_test.py::TestSnitchConfigurationUpdate::test_rf_expand_yaml_file_snitch SKIPPED [ 66%]
replication_test.py::TestSnitchConfigurationUpdate::test_cannot_restart_with_different_rack 
-------------------------------- live log call ---------------------------------
00:52:17,567 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:17,651 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:52:17,718 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:52:17,773 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:17,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 73%]
replication_test.py::TestSnitchConfigurationUpdate::test_failed_snitch_update_gossiping_property_file_snitch 
-------------------------------- live log call ---------------------------------
00:52:36,473 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:36,558 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:52:36,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:52:36,715 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:36,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:52:36,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:52:36,960 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:37,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:52:37,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:52:37,164 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:37,249 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:52:37,299 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:37,383 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:52:37,433 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:52:37,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 80%]
replication_test.py::TestSnitchConfigurationUpdate::test_failed_snitch_update_property_file_snitch 
-------------------------------- live log call ---------------------------------
00:53:16,609 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:16,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:53:16,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:53:16,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:16,935 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:53:17,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:53:17,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:17,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:53:17,243 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
00:53:17,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:17,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:53:17,432 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:17,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
00:53:17,566 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:17,650 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 86%]
replication_test.py::TestSnitchConfigurationUpdate::test_failed_snitch_update_yaml_file_snitch SKIPPED [ 93%]
replication_test.py::TestSnitchConfigurationUpdate::test_switch_data_center_startup_fails 
-------------------------------- live log call ---------------------------------
00:53:56,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:56,872 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:53:56,939 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:53:56,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:53:57,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
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

=================== 12 passed, 3 skipped in 1077.97 seconds ====================
[msx] rc = 0
