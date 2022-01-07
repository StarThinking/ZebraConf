cassandra json_test.py true true
the_test is json_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 15 items

json_test.py::TestToJsonSelect::test_basic_data_types 
-------------------------------- live log call ---------------------------------
19:48:40,148 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:48:40,233 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:48:40,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  6%]
json_test.py::TestToJsonSelect::test_counters 
-------------------------------- live log call ---------------------------------
19:48:50,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:48:50,715 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:48:50,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 13%]
json_test.py::TestToJsonSelect::test_complex_data_types 
-------------------------------- live log call ---------------------------------
19:48:59,593 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:48:59,677 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:48:59,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 20%]
json_test.py::TestFromJsonUpdate::test_basic_data_types 
-------------------------------- live log call ---------------------------------
19:49:16,834 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:49:16,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:49:16,989 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 26%]
json_test.py::TestFromJsonUpdate::test_complex_data_types 
-------------------------------- live log call ---------------------------------
19:49:26,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:49:26,633 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:49:26,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
json_test.py::TestFromJsonUpdate::test_collection_update 
-------------------------------- live log call ---------------------------------
19:49:43,311 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:49:43,398 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:49:43,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
json_test.py::TestFromJsonSelect::test_selecting_pkey_as_json 
-------------------------------- live log call ---------------------------------
19:49:55,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:49:55,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:49:55,676 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 46%]
json_test.py::TestFromJsonSelect::test_select_using_secondary_index 
-------------------------------- live log call ---------------------------------
19:50:05,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:50:05,331 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:50:05,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 53%]
json_test.py::TestFromJsonInsert::test_basic_data_types 
-------------------------------- live log call ---------------------------------
19:50:15,961 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:50:16,46 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:50:16,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
json_test.py::TestFromJsonInsert::test_complex_data_types 
-------------------------------- live log call ---------------------------------
19:50:25,696 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:50:25,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:50:25,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 66%]
json_test.py::TestFromJsonDelete::test_delete_using_pkey_json 
-------------------------------- live log call ---------------------------------
19:50:42,441 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:50:42,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:50:42,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 73%]
json_test.py::TestJsonFullRowInsertSelect::test_simple_schema 
-------------------------------- live log call ---------------------------------
19:50:53,672 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:50:53,758 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:50:53,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 80%]
json_test.py::TestJsonFullRowInsertSelect::test_pkey_requirement 
-------------------------------- live log call ---------------------------------
19:51:07,409 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:51:07,495 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:51:07,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 86%]
json_test.py::TestJsonFullRowInsertSelect::test_null_value 
-------------------------------- live log call ---------------------------------
19:51:15,616 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:51:15,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:51:15,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 93%]
json_test.py::TestJsonFullRowInsertSelect::test_complex_schema 
-------------------------------- live log call ---------------------------------
19:51:24,583 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:51:24,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:51:24,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_basic_data_types passed 1 out of the required 1 times. Success!
test_counters passed 1 out of the required 1 times. Success!
test_complex_data_types passed 1 out of the required 1 times. Success!
test_basic_data_types passed 1 out of the required 1 times. Success!
test_complex_data_types passed 1 out of the required 1 times. Success!
test_collection_update passed 1 out of the required 1 times. Success!
test_selecting_pkey_as_json passed 1 out of the required 1 times. Success!
test_select_using_secondary_index passed 1 out of the required 1 times. Success!
test_basic_data_types passed 1 out of the required 1 times. Success!
test_complex_data_types passed 1 out of the required 1 times. Success!
test_delete_using_pkey_json passed 1 out of the required 1 times. Success!
test_simple_schema passed 1 out of the required 1 times. Success!
test_pkey_requirement passed 1 out of the required 1 times. Success!
test_null_value passed 1 out of the required 1 times. Success!
test_complex_schema passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 15 passed in 184.29 seconds ==========================
[msx] rc = 0
