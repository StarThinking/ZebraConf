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
16:01:34,368 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:01:34,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:01:34,521 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  4%]
batch_test.py::TestBatch::test_counter_batch_accepts_counter_mutations 
-------------------------------- live log call ---------------------------------
16:01:41,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:01:41,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:01:42,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  8%]
batch_test.py::TestBatch::test_counter_batch_rejects_regular_mutations 
-------------------------------- live log call ---------------------------------
16:01:49,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:01:49,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:01:49,438 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 12%]
batch_test.py::TestBatch::test_logged_batch_accepts_regular_mutations 
-------------------------------- live log call ---------------------------------
16:01:56,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:01:56,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:01:56,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 16%]
batch_test.py::TestBatch::test_logged_batch_gcgs_below_threshold_single_table 
-------------------------------- live log call ---------------------------------
16:02:04,200 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:04,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:04,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:11,432 cassandra.protocol WARNING Server warning: Executing a LOGGED BATCH on table [ks.users], configured with a gc_grace_seconds of 0. The gc_grace_seconds is used to TTL batchlog entries, so setting gc_grace_seconds too low on tables involved in an atomic batch might cause batchlog entries to expire before being replayed.
PASSED                                                                   [ 20%]
batch_test.py::TestBatch::test_logged_batch_gcgs_below_threshold_multi_table 
-------------------------------- live log call ---------------------------------
16:02:11,912 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:11,997 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:12,63 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:19,241 cassandra.protocol WARNING Server warning: Executing a LOGGED BATCH on tables [ks.views, ks.users], configured with a gc_grace_seconds of 0. The gc_grace_seconds is used to TTL batchlog entries, so setting gc_grace_seconds too low on tables involved in an atomic batch might cause batchlog entries to expire before being replayed.
PASSED                                                                   [ 24%]
batch_test.py::TestBatch::test_unlogged_batch_gcgs_below_threshold_should_not_print_warning 
-------------------------------- live log call ---------------------------------
16:02:19,628 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:19,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:19,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 28%]
batch_test.py::TestBatch::test_logged_batch_rejects_counter_mutations 
-------------------------------- live log call ---------------------------------
16:02:27,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:27,425 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:27,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 32%]
batch_test.py::TestBatch::test_unlogged_batch_accepts_regular_mutations 
-------------------------------- live log call ---------------------------------
16:02:34,799 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:34,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:34,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 36%]
batch_test.py::TestBatch::test_unlogged_batch_rejects_counter_mutations 
-------------------------------- live log call ---------------------------------
16:02:42,251 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:42,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:42,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
batch_test.py::TestBatch::test_logged_batch_throws_uae 
-------------------------------- live log call ---------------------------------
16:02:49,708 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:49,793 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:49,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:02:49,956 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:50,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:02:50,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:02:50,202 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:02:50,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:02:50,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:03:10,952 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:03:12,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:03:14,266 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:03:17,676 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:03:18,969 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
16:03:20,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
16:03:22,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
16:03:25,798 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
16:03:26,200 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 44%]
batch_test.py::TestBatch::test_logged_batch_doesnt_throw_uae 
-------------------------------- live log call ---------------------------------
16:03:27,577 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:03:27,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:03:27,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:03:27,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:03:27,910 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:03:27,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:03:28,67 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:03:28,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:03:28,217 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:03:47,968 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
16:03:48,976 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
16:03:50,782 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
16:03:55,97 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
16:04:02,420 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 48%]
batch_test.py::TestBatch::test_acknowledged_by_batchlog_not_set_when_batchlog_write_fails 
-------------------------------- live log call ---------------------------------
16:04:11,927 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:04:12,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:04:12,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:04:12,174 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:04:12,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:04:12,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:04:12,415 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:04:12,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:04:12,566 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:04:45,710 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
16:04:46,715 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
16:04:46,816 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
16:04:47,719 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 52%]
batch_test.py::TestBatch::test_acknowledged_by_batchlog_set_when_batchlog_write_succeeds 
-------------------------------- live log call ---------------------------------
16:04:49,24 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:04:49,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:04:49,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:04:49,270 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:04:49,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:04:49,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:04:49,516 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:04:49,600 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:04:49,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
16:05:21,977 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
16:05:22,982 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 56%]
batch_test.py::TestBatch::test_batch_uses_proper_timestamp 
-------------------------------- live log call ---------------------------------
16:05:24,966 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:05:25,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:05:25,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
batch_test.py::TestBatch::test_only_one_timestamp_is_valid 
-------------------------------- live log call ---------------------------------
16:05:32,423 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:05:32,510 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:05:32,578 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 64%]
batch_test.py::TestBatch::test_each_statement_in_batch_uses_proper_timestamp 
-------------------------------- live log call ---------------------------------
16:05:39,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:05:39,962 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:05:40,31 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 68%]
batch_test.py::TestBatch::test_multi_table_batch_for_10554 
-------------------------------- live log call ---------------------------------
16:05:47,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:05:47,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:05:47,490 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
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

==================== 18 passed, 7 skipped in 278.02 seconds ====================
[msx] rc = 0
