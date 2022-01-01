cassandra secondary_indexes_test.py true true
the_test is secondary_indexes_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 23 items / 1 deselected

secondary_indexes_test.py::TestSecondaryIndexes::test_data_created_before_index_not_returned_in_where_query 
-------------------------------- live log call ---------------------------------
10:56:17,309 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:17,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:56:17,395 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:17,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:56:17,463 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:24,99 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:56:24,131 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:56:24,140 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  4%]
secondary_indexes_test.py::TestSecondaryIndexes::test_low_cardinality_indexes 
-------------------------------- live log call ---------------------------------
10:56:24,522 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:24,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:56:24,608 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:24,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:56:24,674 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:24,764 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:24,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:56:24,847 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:24,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:56:24,913 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:25,3 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:25,88 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:56:25,88 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:25,153 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:56:25,154 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  9%]
secondary_indexes_test.py::TestSecondaryIndexes::test_6924_dropping_ks 
-------------------------------- live log call ---------------------------------
10:56:50,801 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:50,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:56:50,886 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:50,953 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:56:50,953 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:51,44 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:51,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:56:51,128 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:51,194 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:56:51,194 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:51,284 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:56:51,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:56:51,368 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:56:51,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:56:51,433 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:57:31,537 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:57:37,538 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:57:42,299 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:57:48,455 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:57:53,460 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:57:58,641 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:03,809 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:09,552 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:15,258 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:19,542 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 13%]
secondary_indexes_test.py::TestSecondaryIndexes::test_6924_dropping_cf 
-------------------------------- live log call ---------------------------------
10:58:20,170 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:58:20,256 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:58:20,256 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:58:20,322 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:58:20,322 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:58:20,413 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:58:20,497 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:58:20,497 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:58:20,566 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
10:58:20,567 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:58:20,657 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:58:20,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:58:20,742 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:58:20,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
10:58:20,807 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:58:40,726 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:44,231 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:48,559 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:52,454 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:58:56,306 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:59:00,577 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:59:04,508 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:59:08,241 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:59:11,191 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
10:59:15,339 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 18%]
secondary_indexes_test.py::TestSecondaryIndexes::test_8280_validate_indexed_values 
-------------------------------- live log call ---------------------------------
10:59:15,868 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:59:15,953 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:59:15,953 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:59:16,18 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:59:16,18 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
secondary_indexes_test.py::TestSecondaryIndexes::test_8280_validate_indexed_values_compact SKIPPED [ 27%]
secondary_indexes_test.py::TestSecondaryIndexes::test_manual_rebuild_index 
-------------------------------- live log call ---------------------------------
10:59:23,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:59:23,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:59:23,963 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:59:24,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:59:24,28 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 31%]
secondary_indexes_test.py::TestSecondaryIndexes::test_failing_manual_rebuild_index 
-------------------------------- live log call ---------------------------------
10:59:46,897 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:59:46,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:59:46,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:59:47,52 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:59:47,52 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
secondary_indexes_test.py::TestSecondaryIndexes::test_drop_index_while_building 
-------------------------------- live log call ---------------------------------
11:00:13,426 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:00:13,511 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:00:13,511 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:00:13,577 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:00:13,578 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
secondary_indexes_test.py::TestSecondaryIndexes::test_index_is_not_rebuilt_at_restart 
-------------------------------- live log call ---------------------------------
11:00:46,964 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:00:47,49 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:00:47,49 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:00:47,118 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:00:47,118 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:00:54,908 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:00:56,15 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:00:58,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:01:02,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 45%]
secondary_indexes_test.py::TestSecondaryIndexes::test_multi_index_filtering_query 
-------------------------------- live log call ---------------------------------
11:01:08,218 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:01:08,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:01:08,303 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:08,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:01:08,370 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
secondary_indexes_test.py::TestSecondaryIndexes::test_only_coordinator_chooses_index_for_query 
-------------------------------- live log call ---------------------------------
11:01:15,442 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:01:15,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:01:15,527 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:15,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:01:15,593 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:15,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:01:15,771 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:01:15,771 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:15,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:01:15,838 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:15,929 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:01:16,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:01:16,14 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:16,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:01:16,79 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 54%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_tuple_indexes 
-------------------------------- live log call ---------------------------------
11:01:41,990 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:01:42,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:01:42,81 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:01:42,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:01:42,147 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 59%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_list_indexes 
-------------------------------- live log call ---------------------------------
11:02:09,543 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:02:09,628 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:02:09,628 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:02:09,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:02:09,694 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 63%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_set_indexes 
-------------------------------- live log call ---------------------------------
11:03:32,516 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:03:32,601 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:03:32,601 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:03:32,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:03:32,667 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 68%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_multiple_indexes_on_single_map_column 
-------------------------------- live log call ---------------------------------
11:04:53,169 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:04:53,254 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:04:53,254 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:04:53,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:04:53,321 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 72%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_map_indexes 
-------------------------------- live log call ---------------------------------
11:05:01,132 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:05:01,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:05:01,218 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:05:01,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:05:01,284 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 77%]
secondary_indexes_test.py::TestUpgradeSecondaryIndexes::test_read_old_sstables_after_upgrade SKIPPED [ 81%]
secondary_indexes_test.py::TestPreJoinCallback::test_bootstrap 
-------------------------------- live log call ---------------------------------
11:06:40,498 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:06:40,583 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:06:40,583 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:06:40,649 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:06:40,649 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:06:40,701 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:06:40,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:06:40,786 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:06:50,272 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:06:50,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:06:50,366 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:06:50,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:06:50,439 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:06:50,494 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:06:50,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:06:50,589 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 86%]
secondary_indexes_test.py::TestPreJoinCallback::test_resume 
-------------------------------- live log call ---------------------------------
11:07:48,130 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:07:48,215 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:07:48,215 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:07:48,281 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:07:48,281 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:07:48,333 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:07:48,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:07:48,418 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:08:05,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:08:05,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:08:05,343 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:08:11,626 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:08:11,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:08:11,718 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:08:11,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:08:11,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:08:11,840 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:08:11,930 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:08:11,931 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:08:24,300 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 90%]
secondary_indexes_test.py::TestPreJoinCallback::test_manual_join 
-------------------------------- live log call ---------------------------------
11:09:03,710 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:09:03,801 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:09:03,802 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:09:03,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:09:03,870 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:09:03,924 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:09:04,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:09:04,11 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:09:13,459 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:09:13,552 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:09:13,553 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:09:13,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:09:13,626 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:09:13,681 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:09:13,774 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:09:13,774 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 95%]
secondary_indexes_test.py::TestPreJoinCallback::test_write_survey 
-------------------------------- live log call ---------------------------------
11:10:10,375 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:10:10,460 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:10:10,461 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:10:10,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:10:10,526 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:10:10,577 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:10:10,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:10:10,661 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:10:20,193 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:10:20,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:10:20,288 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:10:20,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:10:20,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:10:20,417 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:10:20,508 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:10:20,509 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_data_created_before_index_not_returned_in_where_query passed 1 out of the required 1 times. Success!
test_low_cardinality_indexes passed 1 out of the required 1 times. Success!
test_6924_dropping_ks passed 1 out of the required 1 times. Success!
test_6924_dropping_cf passed 1 out of the required 1 times. Success!
test_8280_validate_indexed_values passed 1 out of the required 1 times. Success!
test_manual_rebuild_index passed 1 out of the required 1 times. Success!
test_failing_manual_rebuild_index passed 1 out of the required 1 times. Success!
test_drop_index_while_building passed 1 out of the required 1 times. Success!
test_index_is_not_rebuilt_at_restart passed 1 out of the required 1 times. Success!
test_multi_index_filtering_query passed 1 out of the required 1 times. Success!
test_only_coordinator_chooses_index_for_query passed 1 out of the required 1 times. Success!
test_tuple_indexes passed 1 out of the required 1 times. Success!
test_list_indexes passed 1 out of the required 1 times. Success!
test_set_indexes passed 1 out of the required 1 times. Success!
test_multiple_indexes_on_single_map_column passed 1 out of the required 1 times. Success!
test_map_indexes passed 1 out of the required 1 times. Success!
test_bootstrap passed 1 out of the required 1 times. Success!
test_resume passed 1 out of the required 1 times. Success!
test_manual_join passed 1 out of the required 1 times. Success!
test_write_survey passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

============= 20 passed, 2 skipped, 1 deselected in 902.90 seconds =============
[msx] rc = 0
