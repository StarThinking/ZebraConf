cassandra commitlog_test.py true true
the_test is commitlog_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 12 items

commitlog_test.py::TestCommitLog::test_mv_lock_contention_during_replay 
-------------------------------- live log setup --------------------------------
03:10:51,516 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:51,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:51,603 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:10:51,671 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:51,671 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:10:51,724 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:10:51,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:10:51,811 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:10:57,746 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
03:11:01,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:01,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:01,780 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  8%]
commitlog_test.py::TestCommitLog::test_commitlog_replay_on_startup 
-------------------------------- live log setup --------------------------------
03:11:09,55 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:09,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:09,142 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:11:09,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:09,208 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:11:09,261 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:09,347 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:09,347 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:11:16,363 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:11:17,370 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:11:19,176 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 16%]
commitlog_test.py::TestCommitLog::test_default_segment_size 
-------------------------------- live log setup --------------------------------
03:11:21,541 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:21,628 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:21,628 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:11:21,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:21,697 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:11:21,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:21,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:21,839 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
commitlog_test.py::TestCommitLog::test_small_segment_size 
-------------------------------- live log setup --------------------------------
03:11:40,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:40,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:40,404 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:11:40,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:40,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:11:40,531 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:40,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:40,618 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
commitlog_test.py::TestCommitLog::test_default_compressed_segment_size 
-------------------------------- live log setup --------------------------------
03:11:59,277 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:59,364 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:59,364 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:11:59,430 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:59,430 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:11:59,485 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:11:59,571 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:11:59,571 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 41%]
commitlog_test.py::TestCommitLog::test_small_compressed_segment_size 
-------------------------------- live log setup --------------------------------
03:12:18,31 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:18,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:18,121 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:12:18,188 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:18,188 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:12:18,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:18,330 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:18,330 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
commitlog_test.py::TestCommitLog::test_stop_failure_policy 
-------------------------------- live log setup --------------------------------
03:12:36,777 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:36,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:36,865 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:12:36,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:36,932 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:12:36,987 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:37,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:37,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 58%]
commitlog_test.py::TestCommitLog::test_stop_commit_failure_policy 
-------------------------------- live log setup --------------------------------
03:12:52,270 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:52,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:52,357 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:12:52,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:52,425 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:12:52,479 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:12:52,566 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:12:52,566 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
commitlog_test.py::TestCommitLog::test_die_failure_policy 
-------------------------------- live log setup --------------------------------
03:15:19,83 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:19,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:19,170 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:15:19,236 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:19,236 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:15:19,291 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:19,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:19,381 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
commitlog_test.py::TestCommitLog::test_ignore_failure_policy 
-------------------------------- live log setup --------------------------------
03:15:34,716 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:34,803 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:34,803 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:15:34,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:34,870 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:15:34,926 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:15:35,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:15:35,11 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 83%]
commitlog_test.py::TestCommitLog::test_bad_crc 
-------------------------------- live log setup --------------------------------
03:18:03,874 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:03,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:03,963 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:18:04,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:04,32 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:18:04,86 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:04,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:04,172 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 91%]
commitlog_test.py::TestCommitLog::test_compression_error 
-------------------------------- live log setup --------------------------------
03:18:17,751 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:17,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:17,837 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:18:17,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:17,904 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
03:18:17,957 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:18:18,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:18:18,43 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_mv_lock_contention_during_replay passed 1 out of the required 1 times. Success!
test_commitlog_replay_on_startup passed 1 out of the required 1 times. Success!
test_default_segment_size passed 1 out of the required 1 times. Success!
test_small_segment_size passed 1 out of the required 1 times. Success!
test_default_compressed_segment_size passed 1 out of the required 1 times. Success!
test_small_compressed_segment_size passed 1 out of the required 1 times. Success!
test_stop_failure_policy passed 1 out of the required 1 times. Success!
test_stop_commit_failure_policy passed 1 out of the required 1 times. Success!
test_die_failure_policy passed 1 out of the required 1 times. Success!
test_ignore_failure_policy passed 1 out of the required 1 times. Success!
test_bad_crc passed 1 out of the required 1 times. Success!
test_compression_error passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 12 passed in 460.75 seconds ==========================
[msx] rc = 0
