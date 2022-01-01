cassandra user_functions_test.py true true
the_test is user_functions_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 8 items

user_functions_test.py::TestUserFunctions::test_migration 
-------------------------------- live log call ---------------------------------
13:25:15,119 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:25:15,204 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:25:15,204 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:15,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:25:15,272 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:15,363 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:25:15,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:25:15,448 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:15,513 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:25:15,514 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:15,604 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:25:15,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:25:15,689 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:15,755 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:25:15,755 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 12%]
user_functions_test.py::TestUserFunctions::test_udf_overload 
-------------------------------- live log call ---------------------------------
13:25:40,894 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:25:40,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:25:40,979 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:41,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:25:41,48 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:41,144 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:25:41,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:25:41,232 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:41,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:25:41,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:41,391 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:25:41,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:25:41,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:25:41,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:25:41,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
user_functions_test.py::TestUserFunctions::test_udf_scripting 
-------------------------------- live log call ---------------------------------
13:26:08,430 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:26:08,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:08,516 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:08,583 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:08,583 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 37%]
user_functions_test.py::TestUserFunctions::test_default_aggregate 
-------------------------------- live log call ---------------------------------
13:26:16,139 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:26:16,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:16,224 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:16,291 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:16,292 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:22,685 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:26:22,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:26:22,708 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:26:22,718 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:26:22,726 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 50%]
user_functions_test.py::TestUserFunctions::test_aggregate_udf 
-------------------------------- live log call ---------------------------------
13:26:23,93 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:26:23,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:23,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:23,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:23,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:30,139 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 62%]
user_functions_test.py::TestUserFunctions::test_udf_with_udt 
-------------------------------- live log call ---------------------------------
13:26:31,70 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:26:31,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:31,156 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:31,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:31,224 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:38,112 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
13:26:38,256 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 75%]
user_functions_test.py::TestUserFunctions::test_udf_with_udt_keyspace_isolation 
-------------------------------- live log call ---------------------------------
13:26:38,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:26:38,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:38,852 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:38,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:38,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 87%]
user_functions_test.py::TestUserFunctions::test_aggregate_with_udt_keyspace_isolation 
-------------------------------- live log call ---------------------------------
13:26:45,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:26:45,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:45,808 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:26:45,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:26:45,875 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_migration passed 1 out of the required 1 times. Success!
test_udf_overload passed 1 out of the required 1 times. Success!
test_udf_scripting passed 1 out of the required 1 times. Success!
test_default_aggregate passed 1 out of the required 1 times. Success!
test_aggregate_udf passed 1 out of the required 1 times. Success!
test_udf_with_udt passed 1 out of the required 1 times. Success!
test_udf_with_udt_keyspace_isolation passed 1 out of the required 1 times. Success!
test_aggregate_with_udt_keyspace_isolation passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 8 passed in 98.15 seconds ===========================
[msx] rc = 0
