cassandra cdc_test.py true true
the_test is cdc_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 5 items

cdc_test.py::TestCDC::test_cdc_enabled_data_readable_on_round_trip 
-------------------------------- live log call ---------------------------------
16:56:45,101 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:56:45,185 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:56:45,254 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:56:45,309 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:56:45,393 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 20%]
cdc_test.py::TestCDC::test_cdc_disabled_data_readable_on_round_trip 
-------------------------------- live log call ---------------------------------
16:56:52,808 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:56:52,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:56:52,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:56:53,13 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:56:53,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
cdc_test.py::TestCDC::test_non_cdc_segments_deleted_after_replay 
-------------------------------- live log call ---------------------------------
16:57:00,535 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:57:00,621 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:57:00,687 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:57:00,741 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:57:00,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
cdc_test.py::TestCDC::test_insertion_and_commitlog_behavior_after_reaching_cdc_total_space 
-------------------------------- live log call ---------------------------------
16:57:20,545 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:57:20,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:57:20,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:57:20,752 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:57:20,848 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 80%]
cdc_test.py::TestCDC::test_cdc_data_available_in_cdc_raw 
-------------------------------- live log call ---------------------------------
16:57:53,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:57:53,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:57:53,420 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:57:53,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:57:53,560 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:58:12,497 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:58:12,583 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:58:12,650 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [100%]
===Flaky Test Report===

test_cdc_enabled_data_readable_on_round_trip passed 1 out of the required 1 times. Success!
test_cdc_disabled_data_readable_on_round_trip passed 1 out of the required 1 times. Success!
test_non_cdc_segments_deleted_after_replay passed 1 out of the required 1 times. Success!
test_insertion_and_commitlog_behavior_after_reaching_cdc_total_space passed 1 out of the required 1 times. Success!
test_cdc_data_available_in_cdc_raw passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 5 passed in 242.95 seconds ==========================
[msx] rc = 0
