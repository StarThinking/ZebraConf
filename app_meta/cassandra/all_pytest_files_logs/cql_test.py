cassandra cql_test.py true true
the_test is cql_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 27 items

cql_test.py::TestCQL::test_keyspace 
-------------------------------- live log call ---------------------------------
04:16:11,449 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:16:11,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:11,535 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:16:11,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:11,604 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  3%]
cql_test.py::TestCQL::test_table 
-------------------------------- live log call ---------------------------------
04:16:18,661 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:16:18,746 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:18,746 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:16:18,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:18,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  7%]
cql_test.py::TestCQL::test_table_compact_storage SKIPPED                 [ 11%]
cql_test.py::TestCQL::test_index 
-------------------------------- live log call ---------------------------------
04:16:26,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:16:26,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:26,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:16:26,612 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:26,612 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 14%]
cql_test.py::TestCQL::test_type 
-------------------------------- live log call ---------------------------------
04:16:33,661 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:16:33,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:33,747 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:16:33,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:33,814 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 18%]
cql_test.py::TestCQL::test_user 
-------------------------------- live log call ---------------------------------
04:16:40,865 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:16:40,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:40,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:16:41,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:16:41,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
cql_test.py::TestCQL::test_statements 
-------------------------------- live log call ---------------------------------
04:17:00,103 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:00,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:00,189 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:00,256 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:00,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:06,497 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
04:17:06,507 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
PASSED                                                                   [ 25%]
cql_test.py::TestCQL::test_partition_key_allow_filtering 
-------------------------------- live log call ---------------------------------
04:17:07,61 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:07,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:07,147 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:07,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:07,213 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 29%]
cql_test.py::TestCQL::test_batch 
-------------------------------- live log call ---------------------------------
04:17:14,19 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:14,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:14,105 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:14,171 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:14,171 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
cql_test.py::TestMiscellaneousCQL::test_large_collection_errors SKIPPED  [ 37%]
cql_test.py::TestMiscellaneousCQL::test_cql3_insert_thrift SKIPPED       [ 40%]
cql_test.py::TestMiscellaneousCQL::test_rename SKIPPED                   [ 44%]
cql_test.py::TestMiscellaneousCQL::test_invalid_string_literals 
-------------------------------- live log call ---------------------------------
04:17:21,702 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:21,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:21,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:21,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:21,856 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 48%]
cql_test.py::TestMiscellaneousCQL::test_prepared_statement_invalidation 
-------------------------------- live log call ---------------------------------
04:17:28,406 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:28,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:28,492 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:28,558 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:28,558 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 51%]
cql_test.py::TestMiscellaneousCQL::test_range_slice 
-------------------------------- live log call ---------------------------------
04:17:35,361 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:35,447 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:35,447 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:35,513 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:35,513 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:35,604 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:35,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:17:35,692 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:35,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:17:35,760 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 55%]
cql_test.py::TestMiscellaneousCQL::test_many_columns SKIPPED             [ 59%]
cql_test.py::TestMiscellaneousCQL::test_drop_compact_storage_flag SKIPPED [ 62%]
cql_test.py::TestMiscellaneousCQL::test_truncate_failure 
-------------------------------- live log call ---------------------------------
04:17:55,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:55,383 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:55,383 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:55,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:17:55,451 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:55,544 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:55,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:17:55,629 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:55,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:17:55,697 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:55,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:17:55,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:17:55,875 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:17:55,942 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:17:55,942 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:18:15,247 cassandra.cluster WARNING Host 127.0.0.1:9042 error: Error during truncate.
PASSED                                                                   [ 66%]
cql_test.py::TestCQLSlowQuery::test_local_query 
-------------------------------- live log call ---------------------------------
04:18:15,808 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:18:15,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:18:15,894 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:18:15,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:18:15,960 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:18:33,258 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
04:19:05,4 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
PASSED                                                                   [ 70%]
cql_test.py::TestCQLSlowQuery::test_remote_query 
-------------------------------- live log call ---------------------------------
04:19:49,476 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:19:49,562 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:19:49,562 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:19:49,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:19:49,629 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:19:49,719 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:19:49,804 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:19:49,805 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:19:49,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:19:49,871 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:20:21,767 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
04:21:06,728 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
PASSED                                                                   [ 74%]
cql_test.py::TestCQLSlowQuery::test_disable_slow_query_log 
-------------------------------- live log call ---------------------------------
04:21:56,914 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:21:57,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:21:57,1 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:21:57,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:21:57,70 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 77%]
cql_test.py::TestLWTWithCQL::test_lwt_with_static_columns 
-------------------------------- live log setup --------------------------------
04:22:04,881 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:04,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:22:04,968 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:05,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:22:05,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:05,122 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:05,207 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:22:05,207 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:05,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:22:05,272 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:05,361 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:05,446 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:22:05,446 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:05,511 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:22:05,511 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 81%]
cql_test.py::TestLWTWithCQL::test_conditional_updates_on_static_columns_with_null_values 
-------------------------------- live log setup --------------------------------
04:22:25,378 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:25,464 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:22:25,464 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:25,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:22:25,530 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:25,619 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:25,704 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:22:25,704 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:25,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:22:25,770 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:25,860 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:25,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:22:25,944 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:26,10 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:22:26,10 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 85%]
cql_test.py::TestLWTWithCQL::test_conditional_updates_on_static_columns_with_non_existing_values 
-------------------------------- live log setup --------------------------------
04:22:45,870 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:45,956 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:22:45,957 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:46,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:22:46,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:46,112 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:46,196 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:22:46,196 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:46,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:22:46,262 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:46,351 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:22:46,436 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:22:46,436 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:22:46,504 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:22:46,505 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 88%]
cql_test.py::TestLWTWithCQL::test_conditional_updates_on_static_columns_with_null_values_batch 
-------------------------------- live log setup --------------------------------
04:23:06,373 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:06,459 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:23:06,459 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:06,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:23:06,525 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:06,615 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:06,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:23:06,700 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:06,767 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:23:06,767 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:06,857 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:06,942 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:23:06,942 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:07,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:23:07,11 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 92%]
cql_test.py::TestLWTWithCQL::test_conditional_deletes_on_static_columns_with_null_values 
-------------------------------- live log setup --------------------------------
04:23:26,362 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:26,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:23:26,449 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:26,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:23:26,515 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:26,605 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:26,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:23:26,690 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:26,755 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:23:26,755 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:26,846 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:26,933 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:23:26,933 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:27,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:23:27,0 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 96%]
cql_test.py::TestLWTWithCQL::test_conditional_deletes_on_static_columns_with_null_values_batch 
-------------------------------- live log setup --------------------------------
04:23:46,354 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:46,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:23:46,440 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:46,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:23:46,507 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:46,597 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:46,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:23:46,682 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:46,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:23:46,782 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:46,873 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:23:46,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:23:46,957 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:23:47,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:23:47,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_keyspace passed 1 out of the required 1 times. Success!
test_table passed 1 out of the required 1 times. Success!
test_index passed 1 out of the required 1 times. Success!
test_type passed 1 out of the required 1 times. Success!
test_user passed 1 out of the required 1 times. Success!
test_statements passed 1 out of the required 1 times. Success!
test_partition_key_allow_filtering passed 1 out of the required 1 times. Success!
test_batch passed 1 out of the required 1 times. Success!
test_invalid_string_literals passed 1 out of the required 1 times. Success!
test_prepared_statement_invalidation passed 1 out of the required 1 times. Success!
test_range_slice passed 1 out of the required 1 times. Success!
test_truncate_failure passed 1 out of the required 1 times. Success!
test_local_query passed 1 out of the required 1 times. Success!
test_remote_query passed 1 out of the required 1 times. Success!
test_disable_slow_query_log passed 1 out of the required 1 times. Success!
test_lwt_with_static_columns passed 1 out of the required 1 times. Success!
test_conditional_updates_on_static_columns_with_null_values passed 1 out of the required 1 times. Success!
test_conditional_updates_on_static_columns_with_non_existing_values passed 1 out of the required 1 times. Success!
test_conditional_updates_on_static_columns_with_null_values_batch passed 1 out of the required 1 times. Success!
test_conditional_deletes_on_static_columns_with_null_values passed 1 out of the required 1 times. Success!
test_conditional_deletes_on_static_columns_with_null_values_batch passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 21 passed, 6 skipped in 475.32 seconds ====================
[msx] rc = 0
