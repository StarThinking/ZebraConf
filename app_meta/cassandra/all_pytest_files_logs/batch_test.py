cassandra batch_test.py true true
the_test is batch_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 25 items

batch_test.py::TestBatch::test_empty_batch_throws_no_error 
-------------------------------- live log call ---------------------------------
02:03:31,775 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:03:31,862 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:31,862 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:03:31,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:31,931 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  4%]
batch_test.py::TestBatch::test_counter_batch_accepts_counter_mutations 
-------------------------------- live log call ---------------------------------
02:03:38,986 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:03:39,71 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:39,71 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:03:39,138 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:39,138 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  8%]
batch_test.py::TestBatch::test_counter_batch_rejects_regular_mutations 
-------------------------------- live log call ---------------------------------
02:03:46,441 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:03:46,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:46,527 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:03:46,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:46,593 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 12%]
batch_test.py::TestBatch::test_logged_batch_accepts_regular_mutations 
-------------------------------- live log call ---------------------------------
02:03:53,662 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:03:53,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:53,747 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:03:53,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:03:53,813 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
batch_test.py::TestBatch::test_logged_batch_gcgs_below_threshold_single_table 
-------------------------------- live log call ---------------------------------
02:04:00,864 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:00,950 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:00,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:01,16 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:01,16 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:07,903 cassandra.protocol WARNING Server warning: Executing a LOGGED BATCH on table [ks.users], configured with a gc_grace_seconds of 0. The gc_grace_seconds is used to TTL batchlog entries, so setting gc_grace_seconds too low on tables involved in an atomic batch might cause batchlog entries to expire before being replayed.
PASSED                                                                   [ 20%]
batch_test.py::TestBatch::test_logged_batch_gcgs_below_threshold_multi_table 
-------------------------------- live log call ---------------------------------
02:04:08,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:08,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:08,424 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:08,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:08,492 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:15,510 cassandra.protocol WARNING Server warning: Executing a LOGGED BATCH on tables [ks.views, ks.users], configured with a gc_grace_seconds of 0. The gc_grace_seconds is used to TTL batchlog entries, so setting gc_grace_seconds too low on tables involved in an atomic batch might cause batchlog entries to expire before being replayed.
PASSED                                                                   [ 24%]
batch_test.py::TestBatch::test_unlogged_batch_gcgs_below_threshold_should_not_print_warning 
-------------------------------- live log call ---------------------------------
02:04:15,794 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:15,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:15,880 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:15,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:15,946 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 28%]
batch_test.py::TestBatch::test_logged_batch_rejects_counter_mutations 
-------------------------------- live log call ---------------------------------
02:04:23,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:23,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:23,334 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:23,400 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:23,400 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 32%]
batch_test.py::TestBatch::test_unlogged_batch_accepts_regular_mutations 
-------------------------------- live log call ---------------------------------
02:04:30,453 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:30,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:30,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:30,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:30,605 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
batch_test.py::TestBatch::test_unlogged_batch_rejects_counter_mutations 
-------------------------------- live log call ---------------------------------
02:04:37,659 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:37,746 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:37,746 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:37,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:37,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
batch_test.py::TestBatch::test_logged_batch_throws_uae 
-------------------------------- live log call ---------------------------------
02:04:44,866 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:44,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:44,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:45,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:45,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:45,107 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:45,217 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:04:45,217 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:45,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:04:45,284 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:45,375 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:45,459 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:04:45,459 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:04:45,524 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:04:45,524 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:06,543 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:05:07,625 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:05:09,832 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:05:13,544 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:05:14,437 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
02:05:15,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:05:17,957 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:05:21,65 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:05:21,968 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 44%]
batch_test.py::TestBatch::test_logged_batch_doesnt_throw_uae 
-------------------------------- live log call ---------------------------------
02:05:22,993 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:05:23,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:05:23,78 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:23,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:05:23,143 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:23,233 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:05:23,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:05:23,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:23,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:05:23,384 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:23,473 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:05:23,557 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:05:23,557 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:23,623 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:05:23,623 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:05:43,806 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
02:05:45,11 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:05:47,219 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:05:51,832 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
02:06:00,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 48%]
batch_test.py::TestBatch::test_acknowledged_by_batchlog_not_set_when_batchlog_write_fails 
-------------------------------- live log call ---------------------------------
02:06:07,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:06:07,670 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:06:07,671 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:07,740 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:06:07,741 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:07,831 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:06:07,917 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:06:07,918 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:07,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:06:07,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:08,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:06:08,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:06:08,158 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:08,223 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:06:08,223 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:39,387 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:06:39,389 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
02:06:40,395 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:06:40,595 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 52%]
batch_test.py::TestBatch::test_acknowledged_by_batchlog_set_when_batchlog_write_succeeds 
-------------------------------- live log call ---------------------------------
02:06:42,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:06:42,261 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:06:42,261 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:42,330 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:06:42,330 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:42,423 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:06:42,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:06:42,507 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:42,573 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:06:42,573 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:42,663 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:06:42,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:06:42,747 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:06:42,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:06:42,813 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:07:16,873 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
02:07:17,879 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 56%]
batch_test.py::TestBatch::test_batch_uses_proper_timestamp 
-------------------------------- live log call ---------------------------------
02:07:18,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:07:18,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:18,966 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:07:19,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:19,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
batch_test.py::TestBatch::test_only_one_timestamp_is_valid 
-------------------------------- live log call ---------------------------------
02:07:26,83 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:07:26,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:26,168 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:07:26,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:26,234 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 64%]
batch_test.py::TestBatch::test_each_statement_in_batch_uses_proper_timestamp 
-------------------------------- live log call ---------------------------------
02:07:33,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:07:33,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:33,371 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:07:33,436 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:33,437 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 68%]
batch_test.py::TestBatch::test_multi_table_batch_for_10554 
-------------------------------- live log call ---------------------------------
02:07:40,744 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:07:40,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:40,829 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:07:40,896 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:07:40,896 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 72%]
batch_test.py::TestBatch::test_logged_batch_compatibility_1 SKIPPED      [ 76%]
batch_test.py::TestBatch::test_batchlog_replay_compatibility_1 SKIPPED   [ 80%]
batch_test.py::TestBatch::test_logged_batch_compatibility_2 SKIPPED      [ 84%]
batch_test.py::TestBatch::test_logged_batch_compatibility_3 SKIPPED      [ 88%]
batch_test.py::TestBatch::test_logged_batch_compatibility_4 SKIPPED      [ 92%]
batch_test.py::TestBatch::test_batchlog_replay_compatibility_4 SKIPPED   [ 96%]
batch_test.py::TestBatch::test_logged_batch_compatibility_5 SKIPPED      [100%]
===Flaky Test Report===

test_empty_batch_throws_no_error passed 1 out of the required 1 times. Success!
test_counter_batch_accepts_counter_mutations passed 1 out of the required 1 times. Success!
test_counter_batch_rejects_regular_mutations passed 1 out of the required 1 times. Success!
test_logged_batch_accepts_regular_mutations passed 1 out of the required 1 times. Success!
test_logged_batch_gcgs_below_threshold_single_table passed 1 out of the required 1 times. Success!
test_logged_batch_gcgs_below_threshold_multi_table passed 1 out of the required 1 times. Success!
test_unlogged_batch_gcgs_below_threshold_should_not_print_warning passed 1 out of the required 1 times. Success!
test_logged_batch_rejects_counter_mutations passed 1 out of the required 1 times. Success!
test_unlogged_batch_accepts_regular_mutations passed 1 out of the required 1 times. Success!
test_unlogged_batch_rejects_counter_mutations passed 1 out of the required 1 times. Success!
test_logged_batch_throws_uae passed 1 out of the required 1 times. Success!
test_logged_batch_doesnt_throw_uae passed 1 out of the required 1 times. Success!
test_acknowledged_by_batchlog_not_set_when_batchlog_write_fails passed 1 out of the required 1 times. Success!
test_acknowledged_by_batchlog_set_when_batchlog_write_succeeds passed 1 out of the required 1 times. Success!
test_batch_uses_proper_timestamp passed 1 out of the required 1 times. Success!
test_only_one_timestamp_is_valid passed 1 out of the required 1 times. Success!
test_each_statement_in_batch_uses_proper_timestamp passed 1 out of the required 1 times. Success!
test_multi_table_batch_for_10554 passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 18 passed, 7 skipped in 273.50 seconds ====================
[msx] rc = 0
