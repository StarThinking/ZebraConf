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
02:09:08,87 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:09:08,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:09:08,174 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:09:08,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:09:08,244 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:09:08,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:09:08,387 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:09:08,387 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:09:24,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:09:24,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:09:24,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:09:24,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:09:24,606 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:09:24,657 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:09:24,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:09:24,742 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  3%]
bootstrap_test.py::TestBootstrap::test_simple_bootstrap 
-------------------------------- live log call ---------------------------------
02:10:33,456 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:10:33,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:10:33,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:10:33,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:10:33,607 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:10:33,660 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:10:33,746 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:10:33,746 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:10:50,66 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:10:50,153 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:10:50,153 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:10:50,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:10:50,225 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:10:50,276 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:10:50,361 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:10:50,361 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  7%]
bootstrap_test.py::TestBootstrap::test_bootstrap_on_write_survey 
-------------------------------- live log call ---------------------------------
02:11:59,297 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:11:59,386 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:11:59,386 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:11:59,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:11:59,452 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:11:59,504 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:11:59,589 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:11:59,589 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:12:15,331 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:12:15,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:12:15,418 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:12:15,486 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:12:15,486 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:12:15,537 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:12:15,623 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:12:15,624 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 10%]
bootstrap_test.py::TestBootstrap::test_simple_bootstrap_small_keepalive_period 
-------------------------------- live log call ---------------------------------
02:13:26,946 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:13:27,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:13:27,32 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:13:27,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:13:27,99 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:13:27,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:13:27,238 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:13:27,238 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:13:43,207 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:13:43,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:13:43,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:13:43,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:13:43,372 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 14%]
bootstrap_test.py::TestBootstrap::test_simple_bootstrap_nodata 
-------------------------------- live log call ---------------------------------
02:15:01,125 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:15:01,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:15:01,211 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:15:01,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:15:01,278 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:15:01,369 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:15:01,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:15:01,454 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:15:01,520 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:15:01,520 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:15:17,263 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:15:17,359 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:15:17,359 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:15:17,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:15:17,433 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 17%]
bootstrap_test.py::TestBootstrap::test_schema_removed_nodes 
-------------------------------- live log call ---------------------------------
02:16:31,346 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:16:31,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:16:31,433 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:16:31,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:16:31,501 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:16:31,592 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:16:31,677 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:16:31,677 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:16:31,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:16:31,743 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:17:52,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:17:52,187 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:17:52,188 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:17:52,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:17:52,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 21%]
bootstrap_test.py::TestBootstrap::test_read_from_bootstrapped_node 
-------------------------------- live log call ---------------------------------
02:19:03,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:19:04,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:19:04,84 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:04,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:19:04,150 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:04,241 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:19:04,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:19:04,325 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:04,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:19:04,392 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:04,482 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:19:04,566 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:19:04,567 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:04,633 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:19:04,633 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:35,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:19:35,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:19:35,401 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:19:35,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:19:35,475 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
bootstrap_test.py::TestBootstrap::test_bootstrap_waits_for_streaming_to_finish 
-------------------------------- live log call ---------------------------------
02:20:48,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:20:48,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:20:48,335 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:20:48,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:20:48,402 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:21:03,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:21:03,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:21:03,477 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:21:03,549 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:21:03,550 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:21:03,605 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:21:03,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:21:03,697 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 28%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_true_with_replica_down_should_fail 
-------------------------------- live log call ---------------------------------
02:22:21,587 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:21,673 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:22:21,673 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:21,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:22:21,739 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:21,832 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:21,918 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:22:21,918 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:21,986 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:22:21,986 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:22,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:22,125 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:22:22,125 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:22,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:22,259 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:22:22,260 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:22,309 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:22,394 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:22:22,394 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:22,443 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:22:22,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:22:22,530 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:22:51,931 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
02:22:52,600 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:22:53,685 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:22:55,893 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:22:59,805 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:23:00,648 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:00,740 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:23:00,742 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:00,821 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:23:00,821 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:06,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:23:22,686 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 32%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_false_with_replica_down_should_succeed 
-------------------------------- live log call ---------------------------------
02:23:57,441 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:57,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:23:57,527 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:57,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:23:57,594 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:57,684 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:57,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:23:57,770 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:57,836 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:23:57,836 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:57,890 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:57,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:23:57,975 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:58,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:58,113 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:23:58,113 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:58,163 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:58,248 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:23:58,248 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:23:58,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:23:58,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:23:58,382 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:24:26,777 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
02:24:27,440 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:24:28,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:24:30,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:24:34,952 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:24:35,489 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:24:35,576 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:24:35,577 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:24:35,645 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:24:35,645 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:24:43,84 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:24:59,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:25:32,415 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 68.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 35%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_true_with_rf1_should_fail 
-------------------------------- live log call ---------------------------------
02:25:33,647 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:25:33,734 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:25:33,734 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:33,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:25:33,801 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:33,892 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:25:33,978 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:25:33,978 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:34,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:25:34,45 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:34,99 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:25:34,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:25:34,184 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:34,233 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:25:34,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:25:34,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:34,368 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:25:34,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:25:34,454 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:25:34,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:25:34,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:25:34,588 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:26:03,877 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
02:26:04,769 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:26:05,774 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:26:07,781 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:26:11,492 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:26:12,814 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:26:12,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:26:12,900 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:26:12,968 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:26:12,969 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:26:19,24 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:26:33,764 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 39%]
bootstrap_test.py::TestBootstrap::test_consistent_range_movement_false_with_rf1_should_succeed 
-------------------------------- live log call ---------------------------------
02:27:06,482 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:06,568 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:27:06,568 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:06,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:27:06,634 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:06,725 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:06,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:27:06,813 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:06,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:27:06,880 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:06,934 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:07,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:27:07,20 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:07,69 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:07,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:27:07,154 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:07,203 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:07,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:27:07,289 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:07,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:07,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:27:07,424 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:36,727 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
02:27:37,602 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:27:38,683 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:27:40,891 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:27:44,903 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:27:45,652 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:27:45,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:27:45,743 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:45,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:27:45,811 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:27:53,542 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:28:11,389 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:28:39,561 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 59.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 42%]
bootstrap_test.py::TestBootstrap::test_rf_gt_nodes_multidc_should_succeed 
-------------------------------- live log call ---------------------------------
02:28:43,699 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:28:43,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:28:43,785 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:28:43,851 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:28:43,851 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:28:43,942 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:28:44,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:28:44,28 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:28:44,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:28:44,95 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:29:00,587 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace k is higher than the number of nodes 1 for datacenter dc1
02:29:00,893 cassandra.protocol WARNING Server warning: Your replication factor 2 for keyspace k is higher than the number of nodes 1 for datacenter dc1
02:29:02,867 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:29:02,958 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:29:02,959 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:29:03,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:29:03,29 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 46%]
bootstrap_test.py::TestBootstrap::test_resumable_bootstrap 
-------------------------------- live log call ---------------------------------
02:30:16,172 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:30:16,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:30:16,258 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:30:16,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:30:16,324 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:30:16,415 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:30:16,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:30:16,500 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:30:16,567 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:30:16,567 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:30:16,622 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:30:16,709 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:30:16,710 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:30:47,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:30:47,387 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:30:47,387 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:30:47,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:30:47,455 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
bootstrap_test.py::TestBootstrap::test_bootstrap_with_reset_bootstrap_state 
-------------------------------- live log call ---------------------------------
02:32:06,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:06,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:32:06,106 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:32:06,173 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:32:06,173 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:32:06,264 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:06,349 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:32:06,349 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:32:06,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:32:06,415 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:32:38,109 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:32:38,196 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:32:38,196 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:32:38,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:32:38,266 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
bootstrap_test.py::TestBootstrap::test_manual_bootstrap 
-------------------------------- live log call ---------------------------------
02:35:58,264 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:35:58,350 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:35:58,350 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:35:58,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:35:58,416 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:35:58,507 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:35:58,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:35:58,592 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:35:58,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:35:58,659 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:36:26,474 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:36:26,575 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:36:26,576 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:36:26,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:36:26,654 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 57%]
bootstrap_test.py::TestBootstrap::test_local_quorum_bootstrap 
-------------------------------- live log call ---------------------------------
02:37:04,937 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:37:05,65 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:37:05,65 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:37:05,132 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:37:05,132 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:37:05,223 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:37:05,308 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:37:05,308 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:37:05,373 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:37:05,374 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:37:39,851 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:37:39,943 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:37:39,944 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:37:40,16 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:37:40,16 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
bootstrap_test.py::TestBootstrap::test_shutdown_wiped_node_cannot_join 
-------------------------------- live log call ---------------------------------
02:38:25,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:25,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:38:25,763 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:25,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:38:25,829 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:25,919 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:26,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:38:26,4 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:26,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:38:26,69 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:26,158 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:26,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:38:26,242 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:26,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:38:26,307 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:55,871 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:38:55,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:38:55,965 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:38:56,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:38:56,45 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:08,907 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
02:40:08,911 cassandra.cluster WARNING Connection pool could not be created, not marking node 127.0.0.4:9042 up
02:40:08,911 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
02:40:10,96 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
02:40:12,304 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
02:40:16,720 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 64%]
bootstrap_test.py::TestBootstrap::test_killed_wiped_node_cannot_join 
-------------------------------- live log call ---------------------------------
02:40:22,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:22,760 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:40:22,760 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:22,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:40:22,826 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:22,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:23,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:40:23,1 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:23,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:40:23,66 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:23,167 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:23,255 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:40:23,256 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:23,323 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:40:23,323 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:51,901 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:40:51,997 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:40:51,998 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:40:52,74 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:40:52,74 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 67%]
bootstrap_test.py::TestBootstrap::test_decommissioned_wiped_node_can_join 
-------------------------------- live log call ---------------------------------
02:42:11,646 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:11,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:42:11,732 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:11,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:42:11,798 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:11,888 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:11,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:42:11,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:12,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:42:12,39 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:12,129 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:12,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:42:12,214 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:12,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:42:12,280 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:40,786 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:40,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:42:40,874 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:42:40,943 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:42:40,944 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 71%]
bootstrap_test.py::TestBootstrap::test_decommissioned_wiped_node_can_gossip_to_single_seed 
-------------------------------- live log call ---------------------------------
02:45:29,449 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:45:29,534 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:45:29,535 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:45:29,601 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:45:29,601 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:45:35,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:45:35,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:45:35,390 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:45:35,472 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:45:35,472 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
bootstrap_test.py::TestBootstrap::test_failed_bootstrap_wiped_node_can_join 
-------------------------------- live log call ---------------------------------
02:48:00,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:01,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:48:01,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:48:01,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:48:01,100 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:48:01,154 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:01,241 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:48:01,241 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:48:26,261 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:26,348 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:48:26,348 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:48:26,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:48:26,416 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 78%]
bootstrap_test.py::TestBootstrap::test_node_cannot_join_as_hibernating_node_without_replace_address SKIPPED [ 82%]
bootstrap_test.py::TestBootstrap::test_simultaneous_bootstrap 
-------------------------------- live log call ---------------------------------
02:49:37,215 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:49:37,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:49:37,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:49:37,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:49:37,366 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:50:15,120 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:50:15,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:50:15,231 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:50:15,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:50:15,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:50:49,230 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:50:49,319 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:50:49,320 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:50:49,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:50:49,390 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:51:38,22 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
02:51:46,364 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
02:51:53,968 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
02:52:02,432 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
02:52:10,156 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 85%]
bootstrap_test.py::TestBootstrap::test_cleanup 
-------------------------------- live log call ---------------------------------
02:52:10,627 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:52:10,712 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:52:10,713 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:52:10,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:52:10,779 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:53:27,337 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:53:27,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:53:27,426 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:53:27,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:53:27,494 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 89%]
bootstrap_test.py::TestBootstrap::test_bootstrap_binary_disabled SKIPPED [ 92%]
bootstrap_test.py::TestBootstrap::test_invalid_host_id 
-------------------------------- live log call ---------------------------------
02:54:42,707 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:54:42,794 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:54:42,794 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:54:42,861 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:54:42,861 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:54:48,556 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:54:48,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:54:48,644 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:54:48,722 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:54:48,722 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 96%]
bootstrap_test.py::TestBootstrap::test_host_id_override 
-------------------------------- live log call ---------------------------------
02:54:57,214 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:54:57,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:54:57,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:54:57,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:54:57,366 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:55:03,59 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:55:03,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:55:03,146 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:55:03,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:55:03,214 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:56:44,590 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:56:44,592 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:56:45,600 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:56:47,606 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:56:52,18 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
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

=================== 26 passed, 2 skipped in 2874.88 seconds ====================
[msx] rc = 0
