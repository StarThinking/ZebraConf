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
13:27:54,140 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:27:54,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:27:54,226 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:27:54,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:27:54,295 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:27:54,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:27:54,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:27:54,483 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:27:54,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:27:54,551 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:27:54,643 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:27:54,727 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:27:54,728 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:27:54,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:27:54,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  8%]
user_types_test.py::TestUserTypes::test_nested_type_dropping 
-------------------------------- live log call ---------------------------------
13:28:18,911 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:28:18,996 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:28:18,997 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:19,64 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:28:19,64 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:19,159 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:28:19,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:28:19,244 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:19,312 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:28:19,312 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:19,406 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:28:19,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:28:19,491 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:19,559 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:28:19,559 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
user_types_test.py::TestUserTypes::test_type_enforcement 
-------------------------------- live log call ---------------------------------
13:28:43,168 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:28:43,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:28:43,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:43,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:28:43,326 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:43,419 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:28:43,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:28:43,505 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:43,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:28:43,572 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:43,665 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:28:43,751 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:28:43,752 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:28:43,819 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:28:43,819 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
user_types_test.py::TestUserTypes::test_nested_user_types 
-------------------------------- live log call ---------------------------------
13:29:06,168 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:06,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:29:06,254 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:06,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:29:06,321 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:06,441 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:06,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:29:06,527 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:06,595 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:29:06,595 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:06,688 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:06,774 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:29:06,774 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:06,842 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:29:06,842 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
user_types_test.py::TestUserTypes::test_type_as_part_of_pkey 
-------------------------------- live log call ---------------------------------
13:29:35,963 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:36,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:29:36,54 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:36,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:29:36,122 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:36,215 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:36,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:29:36,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:36,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:29:36,367 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:36,459 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:36,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:29:36,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:36,611 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:29:36,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 41%]
user_types_test.py::TestUserTypes::test_type_secondary_indexing 
-------------------------------- live log call ---------------------------------
13:29:58,980 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:59,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:29:59,66 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:59,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:29:59,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:59,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:59,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:29:59,329 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:59,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:29:59,396 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:59,488 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:29:59,573 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:29:59,573 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:29:59,640 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:29:59,640 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
user_types_test.py::TestUserTypes::test_type_keyspace_permission_isolation 
-------------------------------- live log call ---------------------------------
13:30:24,252 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:30:24,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:30:24,339 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:30:24,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:30:24,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:30:24,498 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:30:24,583 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:30:24,583 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:30:24,650 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:30:24,650 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:30:24,742 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:30:24,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:30:24,826 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:30:24,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:30:24,893 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 58%]
user_types_test.py::TestUserTypes::test_nulls_in_user_types 
-------------------------------- live log call ---------------------------------
13:31:07,839 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:07,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:07,924 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:07,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:07,991 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:08,84 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:08,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:31:08,169 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:08,237 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:31:08,237 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:08,330 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:08,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:31:08,415 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:08,482 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:31:08,482 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
user_types_test.py::TestUserTypes::test_no_counters_in_user_types 
-------------------------------- live log call ---------------------------------
13:31:30,840 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:30,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:30,925 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:30,994 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:30,994 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
user_types_test.py::TestUserTypes::test_type_as_clustering_col 
-------------------------------- live log call ---------------------------------
13:31:37,292 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:37,376 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:37,377 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:37,444 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:37,444 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:37,537 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:37,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:31:37,622 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:37,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:31:37,694 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:37,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:37,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:31:37,873 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:37,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:31:37,940 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 83%]
user_types_test.py::TestUserTypes::test_udt_subfield 
-------------------------------- live log call ---------------------------------
13:31:59,46 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:59,131 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:59,131 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:59,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:31:59,199 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:59,293 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:59,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:31:59,379 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:59,447 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:31:59,448 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:59,540 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:31:59,625 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:31:59,625 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:31:59,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:31:59,693 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 91%]
user_types_test.py::TestUserTypes::test_user_type_isolation 
-------------------------------- live log call ---------------------------------
13:32:20,52 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:32:20,138 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:32:20,138 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:32:20,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:32:20,235 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

========================= 12 passed in 273.22 seconds ==========================
[msx] rc = 0
