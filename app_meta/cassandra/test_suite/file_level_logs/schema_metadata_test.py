cassandra schema_metadata_test.py true true
the_test is schema_metadata_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 18 items

schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_keyspace 
-------------------------------- live log setup --------------------------------
00:55:16,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:55:17,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:55:17,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  5%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_table 
-------------------------------- live log setup --------------------------------
00:55:24,123 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:55:24,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:55:24,276 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 11%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_table_with_2ary_indexes 
-------------------------------- live log setup --------------------------------
00:55:31,334 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:55:31,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:55:31,486 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 16%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_user_types 
-------------------------------- live log setup --------------------------------
00:55:39,45 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:55:39,131 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:55:39,197 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 22%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_udf 
-------------------------------- live log setup --------------------------------
00:55:46,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:55:46,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:55:46,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 27%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_uda 
-------------------------------- live log setup --------------------------------
00:55:53,736 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:55:53,824 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:55:53,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
schema_metadata_test.py::TestSchemaMetadata::test_basic_table_datatype 
-------------------------------- live log setup --------------------------------
00:56:01,446 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:01,533 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:01,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 38%]
schema_metadata_test.py::TestSchemaMetadata::test_collection_table_datatype 
-------------------------------- live log setup --------------------------------
00:56:08,402 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:08,490 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:08,558 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 44%]
schema_metadata_test.py::TestSchemaMetadata::test_clustering_order 
-------------------------------- live log setup --------------------------------
00:56:15,361 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:15,447 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:15,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
schema_metadata_test.py::TestSchemaMetadata::test_compact_storage SKIPPED [ 55%]
schema_metadata_test.py::TestSchemaMetadata::test_compact_storage_composite SKIPPED [ 61%]
schema_metadata_test.py::TestSchemaMetadata::test_nondefault_table_settings 
-------------------------------- live log setup --------------------------------
00:56:22,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:23,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:23,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 66%]
schema_metadata_test.py::TestSchemaMetadata::test_indexes 
-------------------------------- live log setup --------------------------------
00:56:29,937 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:30,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:30,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 72%]
schema_metadata_test.py::TestSchemaMetadata::test_durable_writes 
-------------------------------- live log setup --------------------------------
00:56:36,893 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:36,980 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:37,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 77%]
schema_metadata_test.py::TestSchemaMetadata::test_static_column 
-------------------------------- live log setup --------------------------------
00:56:43,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:43,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:44,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 83%]
schema_metadata_test.py::TestSchemaMetadata::test_udt_table 
-------------------------------- live log setup --------------------------------
00:56:50,805 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:50,891 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:50,958 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 88%]
schema_metadata_test.py::TestSchemaMetadata::test_udf 
-------------------------------- live log setup --------------------------------
00:56:57,786 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:56:57,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:56:57,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 94%]
schema_metadata_test.py::TestSchemaMetadata::test_uda 
-------------------------------- live log setup --------------------------------
00:57:05,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
00:57:05,88 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
00:57:05,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_creating_and_dropping_keyspace passed 1 out of the required 1 times. Success!
test_creating_and_dropping_table passed 1 out of the required 1 times. Success!
test_creating_and_dropping_table_with_2ary_indexes passed 1 out of the required 1 times. Success!
test_creating_and_dropping_user_types passed 1 out of the required 1 times. Success!
test_creating_and_dropping_udf passed 1 out of the required 1 times. Success!
test_creating_and_dropping_uda passed 1 out of the required 1 times. Success!
test_basic_table_datatype passed 1 out of the required 1 times. Success!
test_collection_table_datatype passed 1 out of the required 1 times. Success!
test_clustering_order passed 1 out of the required 1 times. Success!
test_nondefault_table_settings passed 1 out of the required 1 times. Success!
test_indexes passed 1 out of the required 1 times. Success!
test_durable_writes passed 1 out of the required 1 times. Success!
test_static_column passed 1 out of the required 1 times. Success!
test_udt_table passed 1 out of the required 1 times. Success!
test_udf passed 1 out of the required 1 times. Success!
test_uda passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 16 passed, 2 skipped in 115.88 seconds ====================
[msx] rc = 0
