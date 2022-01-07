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
17:09:41,886 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:09:41,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:09:42,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:09:42,94 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:09:42,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:09:48,510 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
17:09:52,659 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:09:52,756 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  8%]
commitlog_test.py::TestCommitLog::test_commitlog_replay_on_startup 
-------------------------------- live log setup --------------------------------
17:10:00,450 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:00,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:10:00,601 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:10:00,655 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:00,740 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:10:08,476 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:10:09,584 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:10:11,891 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 16%]
commitlog_test.py::TestCommitLog::test_default_segment_size 
-------------------------------- live log setup --------------------------------
17:10:13,708 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:13,796 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:10:13,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:10:13,923 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:14,7 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 25%]
commitlog_test.py::TestCommitLog::test_small_segment_size 
-------------------------------- live log setup --------------------------------
17:10:32,704 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:32,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:10:32,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:10:32,911 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:32,996 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
commitlog_test.py::TestCommitLog::test_default_compressed_segment_size 
-------------------------------- live log setup --------------------------------
17:10:51,962 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:52,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:10:52,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:10:52,172 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:10:52,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 41%]
commitlog_test.py::TestCommitLog::test_small_compressed_segment_size 
-------------------------------- live log setup --------------------------------
17:11:11,199 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:11:11,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:11:11,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:11:11,406 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:11:11,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
commitlog_test.py::TestCommitLog::test_stop_failure_policy 
-------------------------------- live log setup --------------------------------
17:11:30,202 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:11:30,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:11:30,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:11:30,412 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:11:30,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 58%]
------------------------------ live log teardown -------------------------------
17:11:45,388 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down

commitlog_test.py::TestCommitLog::test_stop_commit_failure_policy 
-------------------------------- live log setup --------------------------------
17:11:45,693 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:11:45,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:11:45,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:11:45,903 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:11:45,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 66%]
commitlog_test.py::TestCommitLog::test_die_failure_policy 
-------------------------------- live log setup --------------------------------
17:14:12,504 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:14:12,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:14:12,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:14:12,715 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:14:12,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 75%]
commitlog_test.py::TestCommitLog::test_ignore_failure_policy 
-------------------------------- live log setup --------------------------------
17:14:28,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:14:28,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:14:28,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:14:28,601 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:14:28,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 83%]
commitlog_test.py::TestCommitLog::test_bad_crc 
-------------------------------- live log setup --------------------------------
17:16:57,828 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:16:57,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:16:57,980 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:16:58,34 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:16:58,119 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:17:06,234 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:17:07,243 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:17:09,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 91%]
commitlog_test.py::TestCommitLog::test_compression_error 
-------------------------------- live log setup --------------------------------
17:17:11,970 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:17:12,55 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:17:12,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
17:17:12,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:17:12,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:17:20,189 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
17:17:21,198 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
17:17:23,304 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
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

========================= 12 passed in 464.80 seconds ==========================
[msx] rc = 0
