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
10:47:00,718 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:00,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:00,807 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:00,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:00,877 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  5%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_table 
-------------------------------- live log setup --------------------------------
10:47:07,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:07,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:07,761 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:07,828 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:07,828 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 11%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_table_with_2ary_indexes 
-------------------------------- live log setup --------------------------------
10:47:14,879 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:14,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:14,967 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:15,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:15,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_user_types 
-------------------------------- live log setup --------------------------------
10:47:22,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:22,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:22,433 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:22,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:22,500 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_udf 
-------------------------------- live log setup --------------------------------
10:47:29,301 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:29,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:29,389 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:29,457 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:29,458 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 27%]
schema_metadata_test.py::TestSchemaMetadata::test_creating_and_dropping_uda 
-------------------------------- live log setup --------------------------------
10:47:36,502 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:36,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:36,592 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:36,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:36,659 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
schema_metadata_test.py::TestSchemaMetadata::test_basic_table_datatype 
-------------------------------- live log setup --------------------------------
10:47:44,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:44,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:44,303 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:44,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:44,371 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 38%]
schema_metadata_test.py::TestSchemaMetadata::test_collection_table_datatype 
-------------------------------- live log setup --------------------------------
10:47:50,945 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:51,35 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:51,35 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:51,102 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:51,102 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 44%]
schema_metadata_test.py::TestSchemaMetadata::test_clustering_order 
-------------------------------- live log setup --------------------------------
10:47:57,644 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:47:57,733 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:57,733 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:47:57,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:47:57,800 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
schema_metadata_test.py::TestSchemaMetadata::test_compact_storage SKIPPED [ 55%]
schema_metadata_test.py::TestSchemaMetadata::test_compact_storage_composite SKIPPED [ 61%]
schema_metadata_test.py::TestSchemaMetadata::test_nondefault_table_settings 
-------------------------------- live log setup --------------------------------
10:48:04,995 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:05,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:05,84 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:05,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:05,152 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
schema_metadata_test.py::TestSchemaMetadata::test_indexes 
-------------------------------- live log setup --------------------------------
10:48:11,700 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:11,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:11,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:11,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:11,854 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 72%]
schema_metadata_test.py::TestSchemaMetadata::test_durable_writes 
-------------------------------- live log setup --------------------------------
10:48:18,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:18,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:18,516 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:18,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:18,583 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 77%]
schema_metadata_test.py::TestSchemaMetadata::test_static_column 
-------------------------------- live log setup --------------------------------
10:48:25,137 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:25,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:25,225 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:25,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:25,292 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 83%]
schema_metadata_test.py::TestSchemaMetadata::test_udt_table 
-------------------------------- live log setup --------------------------------
10:48:31,848 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:31,936 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:31,936 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:32,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:32,3 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 88%]
schema_metadata_test.py::TestSchemaMetadata::test_udf 
-------------------------------- live log setup --------------------------------
10:48:38,557 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:38,644 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:38,645 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:38,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:38,712 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 94%]
schema_metadata_test.py::TestSchemaMetadata::test_uda 
-------------------------------- live log setup --------------------------------
10:48:45,510 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:48:45,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:45,596 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:48:45,664 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:48:45,664 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

==================== 16 passed, 2 skipped in 112.70 seconds ====================
[msx] rc = 0
