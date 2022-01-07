cassandra user_types_test.py true true
the_test is user_types_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 12 items

user_types_test.py::TestUserTypes::test_type_dropping 
-------------------------------- live log call ---------------------------------
03:39:14,762 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:39:14,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:39:14,915 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:39:15,7 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:39:15,90 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:39:15,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:39:15,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:39:15,332 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:39:15,398 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  8%]
user_types_test.py::TestUserTypes::test_nested_type_dropping 
-------------------------------- live log call ---------------------------------
03:39:39,531 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:39:39,615 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:39:39,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:39:39,774 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:39:39,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:39:39,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:39:40,24 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:39:40,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:39:40,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 16%]
user_types_test.py::TestUserTypes::test_type_enforcement 
-------------------------------- live log call ---------------------------------
03:40:02,288 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:02,373 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:02,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:02,532 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:02,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:40:02,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:40:02,775 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:02,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:40:02,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 25%]
user_types_test.py::TestUserTypes::test_nested_user_types 
-------------------------------- live log call ---------------------------------
03:40:25,46 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:25,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:25,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:25,293 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:25,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:40:25,446 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:40:25,538 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:25,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:40:25,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
user_types_test.py::TestUserTypes::test_type_as_part_of_pkey 
-------------------------------- live log call ---------------------------------
03:40:56,843 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:56,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:56,997 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:57,91 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:57,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:40:57,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:40:57,346 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:57,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:40:57,498 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 41%]
user_types_test.py::TestUserTypes::test_type_secondary_indexing 
-------------------------------- live log call ---------------------------------
03:41:20,605 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:41:20,695 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:41:20,764 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:41:20,857 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:41:20,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:41:21,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:41:21,101 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:41:21,185 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:41:21,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 50%]
user_types_test.py::TestUserTypes::test_type_keyspace_permission_isolation 
-------------------------------- live log call ---------------------------------
03:41:46,382 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:41:46,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:41:46,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:41:46,631 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:41:46,716 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:41:46,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:41:46,876 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:41:46,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:41:47,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 58%]
user_types_test.py::TestUserTypes::test_nulls_in_user_types 
-------------------------------- live log call ---------------------------------
03:42:28,956 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:29,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:42:29,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:42:29,201 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:29,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:42:29,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:42:29,443 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:29,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:42:29,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 66%]
user_types_test.py::TestUserTypes::test_no_counters_in_user_types 
-------------------------------- live log call ---------------------------------
03:42:53,726 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:42:53,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:42:53,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 75%]
user_types_test.py::TestUserTypes::test_type_as_clustering_col 
-------------------------------- live log call ---------------------------------
03:43:00,427 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:00,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:00,579 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:00,672 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:00,757 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:43:00,824 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:43:00,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:01,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:43:01,67 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 83%]
user_types_test.py::TestUserTypes::test_udt_subfield 
-------------------------------- live log call ---------------------------------
03:43:22,695 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:22,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:22,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:22,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:23,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:43:23,88 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:43:23,184 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:23,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:43:23,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 91%]
user_types_test.py::TestUserTypes::test_user_type_isolation 
-------------------------------- live log call ---------------------------------
03:43:46,469 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:43:46,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:43:46,621 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_type_dropping passed 1 out of the required 1 times. Success!
test_nested_type_dropping passed 1 out of the required 1 times. Success!
test_type_enforcement passed 1 out of the required 1 times. Success!
test_nested_user_types passed 1 out of the required 1 times. Success!
test_type_as_part_of_pkey passed 1 out of the required 1 times. Success!
test_type_secondary_indexing passed 1 out of the required 1 times. Success!
test_type_keyspace_permission_isolation passed 1 out of the required 1 times. Success!
test_nulls_in_user_types passed 1 out of the required 1 times. Success!
test_no_counters_in_user_types passed 1 out of the required 1 times. Success!
test_type_as_clustering_col passed 1 out of the required 1 times. Success!
test_udt_subfield passed 1 out of the required 1 times. Success!
test_user_type_isolation passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 12 passed in 279.25 seconds ==========================
[msx] rc = 0
