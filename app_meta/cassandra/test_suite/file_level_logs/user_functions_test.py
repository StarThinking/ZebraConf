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
03:36:29,7 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:36:29,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:36:29,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:36:29,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:36:29,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:36:29,400 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:36:29,492 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:36:29,575 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:36:29,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 12%]
user_functions_test.py::TestUserFunctions::test_udf_overload 
-------------------------------- live log call ---------------------------------
03:36:57,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:36:57,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:36:57,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:36:57,553 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:36:57,641 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:36:57,708 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:36:57,801 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:36:57,885 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:36:57,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 25%]
user_functions_test.py::TestUserFunctions::test_udf_scripting 
-------------------------------- live log call ---------------------------------
03:37:28,336 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:28,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:28,488 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 37%]
user_functions_test.py::TestUserFunctions::test_default_aggregate 
-------------------------------- live log call ---------------------------------
03:37:36,47 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:36,132 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:36,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:42,780 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:37:42,792 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:37:42,801 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:37:42,813 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:37:42,823 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 50%]
user_functions_test.py::TestUserFunctions::test_aggregate_udf 
-------------------------------- live log call ---------------------------------
03:37:43,256 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:43,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:43,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:50,530 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 62%]
user_functions_test.py::TestUserFunctions::test_udf_with_udt 
-------------------------------- live log call ---------------------------------
03:37:51,223 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:51,308 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:51,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:58,462 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:37:58,625 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 75%]
user_functions_test.py::TestUserFunctions::test_udf_with_udt_keyspace_isolation 
-------------------------------- live log call ---------------------------------
03:37:58,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:59,16 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:59,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 87%]
user_functions_test.py::TestUserFunctions::test_aggregate_with_udt_keyspace_isolation 
-------------------------------- live log call ---------------------------------
03:38:06,136 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:38:06,255 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:38:06,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
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

========================== 8 passed in 104.91 seconds ==========================
[msx] rc = 0
