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
01:04:47,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:04:47,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:04:47,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:04:54,768 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:04:54,799 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:04:54,807 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  4%]
secondary_indexes_test.py::TestSecondaryIndexes::test_low_cardinality_indexes 
-------------------------------- live log call ---------------------------------
01:04:55,214 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:04:55,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:04:55,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:04:55,459 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:04:55,544 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:04:55,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:04:55,702 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:04:55,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:04:55,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  9%]
secondary_indexes_test.py::TestSecondaryIndexes::test_6924_dropping_ks 
-------------------------------- live log call ---------------------------------
01:05:22,238 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:05:22,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:05:22,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:05:22,483 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:05:22,569 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:05:22,635 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:05:22,727 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:05:22,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:05:22,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:06:02,540 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:08,988 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:14,582 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:19,238 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:24,883 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:29,466 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:34,237 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:39,580 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:43,242 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:06:48,101 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 13%]
secondary_indexes_test.py::TestSecondaryIndexes::test_6924_dropping_cf 
-------------------------------- live log call ---------------------------------
01:06:48,834 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:06:48,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:06:48,987 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:06:49,78 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:06:49,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:06:49,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:06:49,321 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:06:49,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:06:49,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:07:10,18 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:14,146 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:18,950 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:22,614 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:25,621 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:30,36 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:33,973 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:37,527 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:41,874 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
01:07:45,630 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 18%]
secondary_indexes_test.py::TestSecondaryIndexes::test_8280_validate_indexed_values 
-------------------------------- live log call ---------------------------------
01:07:46,313 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:07:46,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:07:46,467 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 22%]
secondary_indexes_test.py::TestSecondaryIndexes::test_8280_validate_indexed_values_compact SKIPPED [ 27%]
secondary_indexes_test.py::TestSecondaryIndexes::test_manual_rebuild_index 
-------------------------------- live log call ---------------------------------
01:07:54,331 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:07:54,417 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:07:54,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 31%]
secondary_indexes_test.py::TestSecondaryIndexes::test_failing_manual_rebuild_index 
-------------------------------- live log call ---------------------------------
01:08:17,896 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:08:17,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:08:18,52 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 36%]
secondary_indexes_test.py::TestSecondaryIndexes::test_drop_index_while_building 
-------------------------------- live log call ---------------------------------
01:08:46,180 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:08:46,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:08:46,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
secondary_indexes_test.py::TestSecondaryIndexes::test_index_is_not_rebuilt_at_restart 
-------------------------------- live log call ---------------------------------
01:09:20,971 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:09:21,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:09:21,125 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 45%]
secondary_indexes_test.py::TestSecondaryIndexes::test_multi_index_filtering_query 
-------------------------------- live log call ---------------------------------
01:09:42,467 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:09:42,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:09:42,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
secondary_indexes_test.py::TestSecondaryIndexes::test_only_coordinator_chooses_index_for_query 
-------------------------------- live log call ---------------------------------
01:09:49,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:09:49,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:09:49,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:09:49,923 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:09:50,10 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:09:50,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:09:50,169 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:09:50,255 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:09:50,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 54%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_tuple_indexes 
-------------------------------- live log call ---------------------------------
01:10:16,453 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:10:16,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:10:16,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 59%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_list_indexes 
-------------------------------- live log call ---------------------------------
01:10:44,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:10:44,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:10:44,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 63%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_set_indexes 
-------------------------------- live log call ---------------------------------
01:12:08,387 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:12:08,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:12:08,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 68%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_multiple_indexes_on_single_map_column 
-------------------------------- live log call ---------------------------------
01:13:27,765 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:13:27,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:13:27,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 72%]
secondary_indexes_test.py::TestSecondaryIndexesOnCollections::test_map_indexes 
-------------------------------- live log call ---------------------------------
01:13:35,728 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:13:35,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:13:35,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 77%]
secondary_indexes_test.py::TestUpgradeSecondaryIndexes::test_read_old_sstables_after_upgrade SKIPPED [ 81%]
secondary_indexes_test.py::TestPreJoinCallback::test_bootstrap 
-------------------------------- live log call ---------------------------------
01:15:20,680 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:15:20,767 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:15:20,833 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:15:20,886 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:15:20,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:15:30,817 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:15:30,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:15:30,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:15:31,62 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:15:31,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 86%]
secondary_indexes_test.py::TestPreJoinCallback::test_resume 
-------------------------------- live log call ---------------------------------
01:16:28,807 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:16:28,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:16:28,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:16:29,13 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:16:29,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:16:45,977 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:16:46,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:16:52,563 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:16:52,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:16:52,723 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:16:52,776 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:16:52,862 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:17:05,195 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 90%]
secondary_indexes_test.py::TestPreJoinCallback::test_manual_join 
-------------------------------- live log call ---------------------------------
01:17:45,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:17:45,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:17:45,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:17:45,221 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:17:45,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:17:55,71 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:17:55,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:17:55,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:17:55,311 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:17:55,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 95%]
secondary_indexes_test.py::TestPreJoinCallback::test_write_survey 
-------------------------------- live log call ---------------------------------
01:18:52,208 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:18:52,294 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:18:52,361 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:18:52,414 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:18:52,501 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:19:02,632 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:19:02,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:19:02,803 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:19:02,859 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:19:02,954 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
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

============= 20 passed, 2 skipped, 1 deselected in 914.34 seconds =============
[msx] rc = 0
