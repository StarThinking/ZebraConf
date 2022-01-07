cassandra bootstrap_test.py true true
the_test is bootstrap_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 28 items

bootstrap_test.py::TestBootstrap::test_simple_bootstrap_with_ssl 
-------------------------------- live log call ---------------------------------
16:07:15,294 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:07:15,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:07:15,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:07:15,502 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:07:15,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:07:32,180 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:07:32,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:07:32,344 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:07:32,397 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:07:32,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [  3%]
bootstrap_test.py::TestBootstrap::test_simple_bootstrap 
-------------------------------- live log call ---------------------------------
16:08:44,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:08:44,671 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:08:44,738 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:08:44,791 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:08:44,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:09:01,803 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:09:01,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:09:01,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:09:02,19 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:09:02,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [  7%]
bootstrap_test.py::TestBootstrap::test_bootstrap_on_write_survey 
-------------------------------- live log call ---------------------------------
16:10:13,316 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:10:13,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:10:13,469 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:10:13,522 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:10:13,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:10:30,65 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:10:30,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:10:30,228 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:10:30,282 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:10:30,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 10%]
bootstrap_test.py::TestBootstrap::test_simple_bootstrap_small_keepalive_period 
-------------------------------- live log call ---------------------------------
16:11:42,266 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:11:42,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:11:42,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:11:42,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:11:42,587 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:11:59,695 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:11:59,781 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:11:59,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 14%]
bootstrap_test.py::TestBootstrap::test_simple_bootstrap_nodata 
-------------------------------- live log call ---------------------------------
16:13:17,845 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:13:17,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:13:18,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:13:18,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:13:18,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:13:18,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:13:34,841 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:13:34,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:13:35,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 17%]
bootstrap_test.py::TestBootstrap::test_schema_removed_nodes 
-------------------------------- live log call ---------------------------------
16:14:47,140 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:14:47,226 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:14:47,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:14:47,385 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:14:47,469 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:14:47,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:16:08,364 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:16:08,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:16:08,534 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 21%]
bootstrap_test.py::TestBootstrap::test_read_from_bootstrapped_node 
-------------------------------- live log call ---------------------------------
16:17:22,557 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:17:22,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:17:22,709 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:17:22,801 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:17:22,885 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:17:22,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:17:23,43 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:17:23,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:17:23,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:17:53,587 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:17:53,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
16:17:53,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 25%]
bootstrap_test.py::TestBootstrap::test_bootstrap_waits_for_streaming_to_finish 
-------------------------------- live log call ---------------------------------
16:19:07,549 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:19:07,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:19:07,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:19:23,413 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:19:23,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:19:23,573 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:19:23,628 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:19:23,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 28%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_true_with_replica_down_should_fail 
-------------------------------- live log call ---------------------------------
16:20:42,659 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:20:42,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:20:42,810 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:20:42,901 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:20:42,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:20:43,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:20:43,109 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:20:43,194 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:20:43,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:20:43,328 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:20:43,377 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:20:43,464 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:20:43,513 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:20:43,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:21:12,883 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
16:21:13,549 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:21:14,678 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:21:16,484 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:21:21,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:21:21,600 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:21:21,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:21:21,754 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:21:29,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:21:46,273 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:22:13,543 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 32%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_false_with_replica_down_should_succeed 
-------------------------------- live log call ---------------------------------
16:22:16,488 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:16,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:22:16,639 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:22:16,731 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:16,816 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:22:16,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:22:16,937 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:17,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:22:17,72 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:17,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:22:17,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:17,294 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:22:17,345 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:17,429 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:22:46,937 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
16:22:47,601 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:22:48,630 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:22:50,936 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:22:55,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:22:55,651 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:22:55,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:22:55,806 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:23:04,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:23:22,428 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 35%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_true_with_rf1_should_fail 
-------------------------------- live log call ---------------------------------
16:23:53,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:23:53,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:23:53,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:23:53,923 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:23:54,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:23:54,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:23:54,130 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:23:54,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:23:54,265 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:23:54,349 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:23:54,400 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:23:54,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:23:54,535 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:23:54,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:24:22,644 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
16:24:22,895 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:24:23,935 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:24:26,241 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:24:30,153 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:24:30,941 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:24:31,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:24:31,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:24:37,286 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:24:53,29 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:25:20,601 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 68.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 39%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_false_with_rf1_should_succeed 
-------------------------------- live log call ---------------------------------
16:25:26,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:25:26,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:25:26,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:25:26,999 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:25:27,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:25:27,149 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:25:27,207 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:25:27,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:25:27,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:25:27,428 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:25:27,479 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:25:27,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:25:27,614 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:25:27,698 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:25:56,860 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
16:25:57,729 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:25:58,852 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:26:00,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:26:05,373 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:26:05,778 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:26:05,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:26:05,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:26:13,702 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:26:31,652 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 42%]
bootstrap_test.py::TestBootstrap::test_rf_gt_nodes_multidc_should_succeed 
-------------------------------- live log call ---------------------------------
16:27:03,929 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:27:04,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:27:04,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:27:04,174 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:27:04,259 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:27:04,326 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:27:21,169 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace k is higher than the number of nodes 1 for datacenter dc1
16:27:21,471 cassandra.protocol WARNING Server warning: Your replication factor 2 for keyspace k is higher than the number of nodes 1 for datacenter dc1
16:27:23,572 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:27:23,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:27:23,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 46%]
bootstrap_test.py::TestBootstrap::test_resumable_bootstrap 
-------------------------------- live log call ---------------------------------
16:28:36,893 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:28:36,977 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:28:37,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:28:37,135 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:28:37,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:28:37,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:28:37,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:28:37,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:29:09,828 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:29:09,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:29:09,994 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 50%]
bootstrap_test.py::TestBootstrap::test_bootstrap_with_reset_bootstrap_state 
-------------------------------- live log call ---------------------------------
16:30:29,502 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:30:29,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:30:29,655 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:30:29,748 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:30:29,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:30:29,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:31:04,420 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:31:04,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:31:04,576 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 53%]
bootstrap_test.py::TestBootstrap::test_manual_bootstrap 
-------------------------------- live log call ---------------------------------
16:34:25,20 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:34:25,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:34:25,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:34:25,270 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:34:25,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:34:25,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:34:53,742 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:34:53,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:34:53,933 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 57%]
bootstrap_test.py::TestBootstrap::test_local_quorum_bootstrap 
-------------------------------- live log call ---------------------------------
16:35:32,958 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:35:33,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:35:33,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:35:33,204 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:35:33,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:35:33,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:36:09,778 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:36:09,866 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:36:09,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 60%]
bootstrap_test.py::TestBootstrap::test_shutdown_wiped_node_cannot_join 
-------------------------------- live log call ---------------------------------
16:36:56,29 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:36:56,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:36:56,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:36:56,274 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:36:56,358 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:36:56,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:36:56,519 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:36:56,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:36:56,672 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:37:26,491 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:37:26,586 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
16:37:26,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 64%]
bootstrap_test.py::TestBootstrap::test_killed_wiped_node_cannot_join 
-------------------------------- live log call ---------------------------------
16:38:55,540 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:38:55,625 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:38:55,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:38:55,784 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:38:55,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:38:55,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:38:56,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:38:56,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:38:56,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:39:25,286 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:39:25,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
16:39:25,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
16:40:40,628 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
16:40:40,639 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
16:40:40,640 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
16:40:41,715 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
16:40:43,621 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 67%]
bootstrap_test.py::TestBootstrap::test_decommissioned_wiped_node_can_join 
-------------------------------- live log call ---------------------------------
16:40:47,563 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:40:47,648 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:40:47,715 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:40:47,811 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:40:47,897 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:40:47,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:40:48,58 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:40:48,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:40:48,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:41:18,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:41:18,441 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
16:41:18,519 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 71%]
bootstrap_test.py::TestBootstrap::test_decommissioned_wiped_node_can_gossip_to_single_seed 
-------------------------------- live log call ---------------------------------
16:44:05,647 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:44:05,733 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:44:05,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:44:11,667 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:44:11,760 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:44:11,828 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 75%]
bootstrap_test.py::TestBootstrap::test_failed_bootstrap_wiped_node_can_join 
-------------------------------- live log call ---------------------------------
16:46:38,653 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:46:38,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:46:38,806 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:46:38,861 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:46:38,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:47:04,434 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:47:04,521 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:47:04,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 78%]
bootstrap_test.py::TestBootstrap::test_node_cannot_join_as_hibernating_node_without_replace_address SKIPPED [ 82%]
bootstrap_test.py::TestBootstrap::test_simultaneous_bootstrap 
-------------------------------- live log call ---------------------------------
16:48:16,657 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:48:16,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:48:16,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:48:54,625 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:48:54,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:48:54,781 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:49:30,157 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:49:30,248 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:49:30,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:50:17,872 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
16:50:25,408 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
16:50:33,197 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
16:50:40,715 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
16:50:48,123 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 85%]
bootstrap_test.py::TestBootstrap::test_cleanup 
-------------------------------- live log call ---------------------------------
16:50:48,544 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:50:48,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:50:48,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:52:06,655 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:52:06,764 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:52:06,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 89%]
bootstrap_test.py::TestBootstrap::test_bootstrap_binary_disabled SKIPPED [ 92%]
bootstrap_test.py::TestBootstrap::test_invalid_host_id 
-------------------------------- live log call ---------------------------------
16:53:24,173 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:53:24,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:53:24,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:53:30,210 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:53:30,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:53:30,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 96%]
bootstrap_test.py::TestBootstrap::test_host_id_override 
-------------------------------- live log call ---------------------------------
16:53:38,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:53:39,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:53:39,67 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:53:44,960 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:53:45,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:53:45,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:55:20,446 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:55:27,620 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:55:27,624 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:55:28,730 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:55:30,535 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:55:35,47 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_simple_bootstrap_with_ssl passed 1 out of the required 1 times. Success!
test_simple_bootstrap passed 1 out of the required 1 times. Success!
test_bootstrap_on_write_survey passed 1 out of the required 1 times. Success!
test_simple_bootstrap_small_keepalive_period passed 1 out of the required 1 times. Success!
test_simple_bootstrap_nodata passed 1 out of the required 1 times. Success!
test_schema_removed_nodes passed 1 out of the required 1 times. Success!
test_read_from_bootstrapped_node passed 1 out of the required 1 times. Success!
test_bootstrap_waits_for_streaming_to_finish passed 1 out of the required 1 times. Success!
test_consistent_range_movement_true_with_replica_down_should_fail passed 1 out of the required 1 times. Success!
test_consistent_range_movement_false_with_replica_down_should_succeed passed 1 out of the required 1 times. Success!
test_consistent_range_movement_true_with_rf1_should_fail passed 1 out of the required 1 times. Success!
test_consistent_range_movement_false_with_rf1_should_succeed passed 1 out of the required 1 times. Success!
test_rf_gt_nodes_multidc_should_succeed passed 1 out of the required 1 times. Success!
test_resumable_bootstrap passed 1 out of the required 1 times. Success!
test_bootstrap_with_reset_bootstrap_state passed 1 out of the required 1 times. Success!
test_manual_bootstrap passed 1 out of the required 1 times. Success!
test_local_quorum_bootstrap passed 1 out of the required 1 times. Success!
test_shutdown_wiped_node_cannot_join passed 1 out of the required 1 times. Success!
test_killed_wiped_node_cannot_join passed 1 out of the required 1 times. Success!
test_decommissioned_wiped_node_can_join passed 1 out of the required 1 times. Success!
test_decommissioned_wiped_node_can_gossip_to_single_seed passed 1 out of the required 1 times. Success!
test_failed_bootstrap_wiped_node_can_join passed 1 out of the required 1 times. Success!
test_simultaneous_bootstrap passed 1 out of the required 1 times. Success!
test_cleanup passed 1 out of the required 1 times. Success!
test_invalid_host_id passed 1 out of the required 1 times. Success!
test_host_id_override passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 26 passed, 2 skipped in 2910.93 seconds ====================
[msx] rc = 0
