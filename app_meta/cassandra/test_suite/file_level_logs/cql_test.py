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
18:16:09,714 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:16:09,802 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:16:09,871 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  3%]
cql_test.py::TestCQL::test_table 
-------------------------------- live log call ---------------------------------
18:16:16,900 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:16:16,986 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:16:17,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  7%]
cql_test.py::TestCQL::test_table_compact_storage SKIPPED                 [ 11%]
cql_test.py::TestCQL::test_index 
-------------------------------- live log call ---------------------------------
18:16:24,660 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:16:24,746 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:16:24,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 14%]
cql_test.py::TestCQL::test_type 
-------------------------------- live log call ---------------------------------
18:16:32,129 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:16:32,217 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:16:32,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 18%]
cql_test.py::TestCQL::test_user 
-------------------------------- live log call ---------------------------------
18:16:39,589 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:16:39,677 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:16:39,745 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 22%]
cql_test.py::TestCQL::test_statements 
-------------------------------- live log call ---------------------------------
18:16:59,78 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:16:59,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:16:59,232 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:05,737 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
18:17:05,745 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
PASSED                                                                   [ 25%]
cql_test.py::TestCQL::test_partition_key_allow_filtering 
-------------------------------- live log call ---------------------------------
18:17:06,281 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:06,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:06,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 29%]
cql_test.py::TestCQL::test_batch 
-------------------------------- live log call ---------------------------------
18:17:13,489 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:13,575 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:13,646 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
cql_test.py::TestMiscellaneousCQL::test_large_collection_errors SKIPPED  [ 37%]
cql_test.py::TestMiscellaneousCQL::test_cql3_insert_thrift SKIPPED       [ 40%]
cql_test.py::TestMiscellaneousCQL::test_rename SKIPPED                   [ 44%]
cql_test.py::TestMiscellaneousCQL::test_invalid_string_literals 
-------------------------------- live log call ---------------------------------
18:17:21,138 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:21,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:21,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 48%]
cql_test.py::TestMiscellaneousCQL::test_prepared_statement_invalidation 
-------------------------------- live log call ---------------------------------
18:17:28,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:28,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:28,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 51%]
cql_test.py::TestMiscellaneousCQL::test_range_slice 
-------------------------------- live log call ---------------------------------
18:17:35,301 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:35,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:35,456 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:35,548 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:35,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:17:35,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 55%]
cql_test.py::TestMiscellaneousCQL::test_many_columns SKIPPED             [ 59%]
cql_test.py::TestMiscellaneousCQL::test_drop_compact_storage_flag SKIPPED [ 62%]
cql_test.py::TestMiscellaneousCQL::test_truncate_failure 
-------------------------------- live log call ---------------------------------
18:17:54,493 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:54,580 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:54,650 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:17:54,743 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:54,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:17:54,898 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:17:54,993 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:17:55,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:17:55,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:18:14,686 cassandra.cluster WARNING Host 127.0.0.1:9042 error: Error during truncate.
PASSED                                                                   [ 66%]
cql_test.py::TestCQLSlowQuery::test_local_query 
-------------------------------- live log call ---------------------------------
18:18:15,246 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:18:15,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:18:15,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:18:29,783 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
18:18:54,222 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
PASSED                                                                   [ 70%]
cql_test.py::TestCQLSlowQuery::test_remote_query 
-------------------------------- live log call ---------------------------------
18:19:27,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:19:27,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:19:28,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:19:28,124 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:19:28,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:19:28,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:20:05,435 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
18:20:47,852 dtest WARNING AlreadyExists executing create ks query 'CREATE KEYSPACE ks WITH replication={'class':'SimpleStrategy', 'replication_factor':1}'
PASSED                                                                   [ 74%]
cql_test.py::TestCQLSlowQuery::test_disable_slow_query_log 
-------------------------------- live log call ---------------------------------
18:21:34,817 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:21:34,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:21:34,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 77%]
cql_test.py::TestLWTWithCQL::test_lwt_with_static_columns 
-------------------------------- live log setup --------------------------------
18:21:43,292 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:21:43,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:21:43,449 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:21:43,542 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:21:43,628 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:21:43,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:21:43,789 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:21:43,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:21:43,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 81%]
cql_test.py::TestLWTWithCQL::test_conditional_updates_on_static_columns_with_null_values 
-------------------------------- live log setup --------------------------------
18:22:04,47 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:04,138 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:22:04,206 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:22:04,299 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:04,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:22:04,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:22:04,545 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:04,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:22:04,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 85%]
cql_test.py::TestLWTWithCQL::test_conditional_updates_on_static_columns_with_non_existing_values 
-------------------------------- live log setup --------------------------------
18:22:24,544 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:24,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:22:24,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:22:24,793 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:24,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:22:24,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:22:25,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:25,127 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:22:25,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 88%]
cql_test.py::TestLWTWithCQL::test_conditional_updates_on_static_columns_with_null_values_batch 
-------------------------------- live log setup --------------------------------
18:22:45,571 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:45,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:22:45,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:22:45,855 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:45,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:22:46,7 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:22:46,99 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:22:46,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:22:46,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 92%]
cql_test.py::TestLWTWithCQL::test_conditional_deletes_on_static_columns_with_null_values 
-------------------------------- live log setup --------------------------------
18:23:07,55 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:23:07,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:23:07,212 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:23:07,304 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:23:07,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:23:07,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:23:07,550 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:23:07,635 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:23:07,703 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 96%]
cql_test.py::TestLWTWithCQL::test_conditional_deletes_on_static_columns_with_null_values_batch 
-------------------------------- live log setup --------------------------------
18:23:28,815 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:23:28,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:23:28,969 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:23:29,62 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:23:29,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:23:29,215 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:23:29,307 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:23:29,393 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:23:29,460 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
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

==================== 21 passed, 6 skipped in 460.99 seconds ====================
[msx] rc = 0
