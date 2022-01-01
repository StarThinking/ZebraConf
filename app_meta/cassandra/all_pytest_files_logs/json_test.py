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
05:47:18,456 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:47:18,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:18,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:47:18,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:18,610 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  6%]
json_test.py::TestToJsonSelect::test_counters 
-------------------------------- live log call ---------------------------------
05:47:28,676 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:47:28,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:28,762 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:47:28,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:28,829 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 13%]
json_test.py::TestToJsonSelect::test_complex_data_types 
-------------------------------- live log call ---------------------------------
05:47:37,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:47:37,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:37,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:47:37,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:37,542 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
json_test.py::TestFromJsonUpdate::test_basic_data_types 
-------------------------------- live log call ---------------------------------
05:47:54,382 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:47:54,467 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:54,467 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:47:54,534 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:47:54,534 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 26%]
json_test.py::TestFromJsonUpdate::test_complex_data_types 
-------------------------------- live log call ---------------------------------
05:48:03,842 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:48:03,928 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:03,928 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:48:03,995 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:03,995 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
json_test.py::TestFromJsonUpdate::test_collection_update 
-------------------------------- live log call ---------------------------------
05:48:20,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:48:20,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:20,431 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:48:20,499 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:20,499 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
json_test.py::TestFromJsonSelect::test_selecting_pkey_as_json 
-------------------------------- live log call ---------------------------------
05:48:32,566 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:48:32,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:32,652 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:48:32,719 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:32,719 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 46%]
json_test.py::TestFromJsonSelect::test_select_using_secondary_index 
-------------------------------- live log call ---------------------------------
05:48:42,282 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:48:42,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:42,370 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:48:42,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:42,439 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
json_test.py::TestFromJsonInsert::test_basic_data_types 
-------------------------------- live log call ---------------------------------
05:48:52,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:48:52,840 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:52,840 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:48:52,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:48:52,907 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
json_test.py::TestFromJsonInsert::test_complex_data_types 
-------------------------------- live log call ---------------------------------
05:49:02,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:49:02,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:02,302 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:49:02,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:02,369 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
json_test.py::TestFromJsonDelete::test_delete_using_pkey_json 
-------------------------------- live log call ---------------------------------
05:49:18,710 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:49:18,796 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:18,796 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:49:18,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:18,863 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 73%]
json_test.py::TestJsonFullRowInsertSelect::test_simple_schema 
-------------------------------- live log call ---------------------------------
05:49:29,678 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:49:29,765 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:29,765 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:49:29,832 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:29,832 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
json_test.py::TestJsonFullRowInsertSelect::test_pkey_requirement 
-------------------------------- live log call ---------------------------------
05:49:43,154 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:49:43,240 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:43,240 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:49:43,306 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:43,307 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 86%]
json_test.py::TestJsonFullRowInsertSelect::test_null_value 
-------------------------------- live log call ---------------------------------
05:49:51,115 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:49:51,200 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:51,200 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:49:51,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:51,267 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 93%]
json_test.py::TestJsonFullRowInsertSelect::test_complex_schema 
-------------------------------- live log call ---------------------------------
05:49:59,854 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:49:59,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:49:59,941 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:50:00,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:50:00,8 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

========================= 15 passed in 180.96 seconds ==========================
[msx] rc = 0
