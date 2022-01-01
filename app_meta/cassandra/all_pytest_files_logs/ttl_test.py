cassandra ttl_test.py true true
the_test is ttl_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 25 items

ttl_test.py::TestTTL::test_default_ttl 
-------------------------------- live log setup --------------------------------
13:11:57,987 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:11:58,72 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:11:58,72 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:11:58,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:11:58,141 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:12:07,290 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  4%]
ttl_test.py::TestTTL::test_insert_ttl_has_priority_on_defaut_ttl 
-------------------------------- live log setup --------------------------------
13:12:07,713 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:12:07,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:07,799 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:12:07,866 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:07,866 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:12:16,9 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:12:20,990 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  8%]
ttl_test.py::TestTTL::test_insert_ttl_works_without_default_ttl 
-------------------------------- live log setup --------------------------------
13:12:21,434 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:12:21,520 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:21,520 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:12:21,587 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:21,587 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:12:30,719 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 12%]
ttl_test.py::TestTTL::test_default_ttl_can_be_removed 
-------------------------------- live log setup --------------------------------
13:12:31,145 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:12:31,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:31,230 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:12:31,297 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:31,297 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:12:38,935 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 16%]
ttl_test.py::TestTTL::test_removing_default_ttl_does_not_affect_existing_rows 
-------------------------------- live log setup --------------------------------
13:12:39,349 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:12:39,434 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:39,435 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:12:39,501 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:12:39,501 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:12:50,777 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:12:57,751 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:13:05,753 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 20%]
ttl_test.py::TestTTL::test_update_single_column_ttl 
-------------------------------- live log setup --------------------------------
13:13:06,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:13:06,190 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:06,190 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:13:06,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:06,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 24%]
ttl_test.py::TestTTL::test_update_multiple_columns_ttl 
-------------------------------- live log setup --------------------------------
13:13:17,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:13:17,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:17,907 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:13:17,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:17,974 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 28%]
ttl_test.py::TestTTL::test_update_column_ttl_with_default_ttl 
-------------------------------- live log setup --------------------------------
13:13:28,532 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:13:28,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:28,619 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:13:28,686 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:28,686 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:13:44,839 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 32%]
ttl_test.py::TestTTL::test_remove_column_ttl 
-------------------------------- live log setup --------------------------------
13:13:45,272 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:13:45,359 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:45,359 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:13:45,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:45,427 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
ttl_test.py::TestTTL::test_set_ttl_to_zero_to_default_ttl 
-------------------------------- live log setup --------------------------------
13:13:55,983 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:13:56,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:56,68 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:13:56,136 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:13:56,136 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
ttl_test.py::TestTTL::test_remove_column_ttl_with_default_ttl SKIPPED    [ 44%]
ttl_test.py::TestTTL::test_collection_list_ttl 
-------------------------------- live log setup --------------------------------
13:14:08,20 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:14:08,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:14:08,108 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:14:08,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:14:08,176 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:14:26,473 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 48%]
ttl_test.py::TestTTL::test_collection_set_ttl 
-------------------------------- live log setup --------------------------------
13:14:26,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:14:26,859 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:14:26,859 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:14:26,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:14:26,926 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:14:45,248 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 52%]
ttl_test.py::TestTTL::test_collection_map_ttl 
-------------------------------- live log setup --------------------------------
13:14:45,485 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:14:45,570 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:14:45,570 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:14:45,636 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:14:45,636 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:14:59,912 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 56%]
ttl_test.py::TestTTL::test_delete_with_ttl_expired 
-------------------------------- live log setup --------------------------------
13:15:00,209 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:15:00,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:00,296 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:15:00,363 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:00,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:15:08,608 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 60%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_cap 
-------------------------------- live log setup --------------------------------
13:15:08,920 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:15:09,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:09,12 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:15:09,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:09,79 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:15:16,705 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:15:17,914 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:15:19,819 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:15:24,138 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:15:28,713 cassandra.protocol WARNING Server warning: Request on table ks.ttl_table with ttl of 630720000 seconds exceeds maximum supported expiration date of 2038-01-19T03:14:06+00:00 and will have its expiration capped to that date. In order to avoid this use a lower TTL or upgrade to a version where this limitation is fixed. See CASSANDRA-14092 for more details.
13:15:30,604 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 64%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_cap_default_ttl 
-------------------------------- live log setup --------------------------------
13:15:30,929 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:15:31,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:31,15 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:15:31,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:31,82 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:15:38,509 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:15:39,716 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:15:41,922 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:15:46,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:15:49,688 cassandra.protocol WARNING Server warning: Request on table ks.ttl_table with default ttl of 630720000 seconds exceeds maximum supported expiration date of 2038-01-19T03:14:06+00:00 and will have its expiration capped to that date. In order to avoid this use a lower TTL or upgrade to a version where this limitation is fixed. See CASSANDRA-14092 for more details.
13:15:51,542 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 68%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_capnowarn 
-------------------------------- live log setup --------------------------------
13:15:51,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:15:52,18 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:52,18 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:15:52,86 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:15:52,86 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:15:58,317 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:15:59,424 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:01,429 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:05,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:12,610 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 72%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_capnowarn_default_ttl 
-------------------------------- live log setup --------------------------------
13:16:12,943 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:16:13,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:16:13,28 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:16:13,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:16:13,95 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:16:20,401 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:16:21,407 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:23,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:28,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:33,482 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 76%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_reject 
-------------------------------- live log setup --------------------------------
13:16:33,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:16:34,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:16:34,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:16:34,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:16:34,101 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:16:41,829 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:16:42,836 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:44,742 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:49,257 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:16:55,499 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 80%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_reject_default_ttl 
-------------------------------- live log setup --------------------------------
13:16:55,960 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:16:56,46 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:16:56,46 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:16:56,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:16:56,114 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:17:04,48 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:17:05,255 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:17:07,160 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:17:11,177 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:17:17,617 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 84%]
ttl_test.py::TestDistributedTTL::test_ttl_is_replicated 
-------------------------------- live log setup --------------------------------
13:17:18,5 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:17:18,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:17:18,91 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:17:18,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:17:18,164 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:17:18,257 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:17:18,341 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:17:18,342 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:17:18,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:17:18,409 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 88%]
ttl_test.py::TestDistributedTTL::test_ttl_is_respected_on_delayed_replication 
-------------------------------- live log setup --------------------------------
13:17:42,910 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:17:42,997 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:17:42,997 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:17:43,64 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:17:43,65 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:17:43,158 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:17:43,243 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:17:43,243 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:17:43,313 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:17:43,314 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:17:59,930 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
13:18:00,148 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:18:01,250 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:18:03,55 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:18:07,267 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:18:14,187 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:18:28,24 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:18:28,676 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:18:28,677 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:18:29,733 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:18:31,537 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:18:35,146 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:18:42,666 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:18:59,309 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:19:04,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 67.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
13:19:14,489 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:19:28,274 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 92%]
ttl_test.py::TestDistributedTTL::test_ttl_is_respected_on_repair 
-------------------------------- live log setup --------------------------------
13:19:28,791 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:19:28,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:19:28,878 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:19:28,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:19:28,946 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:19:29,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:19:29,127 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:19:29,127 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:19:29,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:19:29,200 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
13:20:14,108 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
13:20:14,542 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:20:17,439 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:20:17,440 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:20:18,447 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:20:20,354 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:20:23,865 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:20:24,573 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 96%]
ttl_test.py::TestRecoverNegativeExpirationDate::test_recover_negative_expiration_date_sstables_with_scrub 
-------------------------------- live log call ---------------------------------
13:20:24,930 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:20:25,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:20:25,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:20:25,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:20:25,84 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:20:32,743 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [100%]
===Flaky Test Report===

test_default_ttl passed 1 out of the required 1 times. Success!
test_insert_ttl_has_priority_on_defaut_ttl passed 1 out of the required 1 times. Success!
test_insert_ttl_works_without_default_ttl passed 1 out of the required 1 times. Success!
test_default_ttl_can_be_removed passed 1 out of the required 1 times. Success!
test_removing_default_ttl_does_not_affect_existing_rows passed 1 out of the required 1 times. Success!
test_update_single_column_ttl passed 1 out of the required 1 times. Success!
test_update_multiple_columns_ttl passed 1 out of the required 1 times. Success!
test_update_column_ttl_with_default_ttl passed 1 out of the required 1 times. Success!
test_remove_column_ttl passed 1 out of the required 1 times. Success!
test_set_ttl_to_zero_to_default_ttl passed 1 out of the required 1 times. Success!
test_collection_list_ttl passed 1 out of the required 1 times. Success!
test_collection_set_ttl passed 1 out of the required 1 times. Success!
test_collection_map_ttl passed 1 out of the required 1 times. Success!
test_delete_with_ttl_expired passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_cap passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_cap_default_ttl passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_capnowarn passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_capnowarn_default_ttl passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_reject passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_reject_default_ttl passed 1 out of the required 1 times. Success!
test_ttl_is_replicated passed 1 out of the required 1 times. Success!
test_ttl_is_respected_on_delayed_replication passed 1 out of the required 1 times. Success!
test_ttl_is_respected_on_repair passed 1 out of the required 1 times. Success!
test_recover_negative_expiration_date_sstables_with_scrub passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 24 passed, 1 skipped in 531.79 seconds ====================
[msx] rc = 0
