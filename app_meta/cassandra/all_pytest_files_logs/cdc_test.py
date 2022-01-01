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
02:58:01,875 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:01,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:01,960 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:02,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:02,28 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:02,82 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:02,167 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:02,167 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
cdc_test.py::TestCDC::test_cdc_disabled_data_readable_on_round_trip 
-------------------------------- live log call ---------------------------------
02:58:09,663 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:09,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:09,747 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:09,814 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:09,814 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:09,868 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:09,954 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:09,954 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
cdc_test.py::TestCDC::test_non_cdc_segments_deleted_after_replay 
-------------------------------- live log call ---------------------------------
02:58:17,448 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:17,532 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:17,533 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:17,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:17,598 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:17,653 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:17,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:17,737 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
cdc_test.py::TestCDC::test_insertion_and_commitlog_behavior_after_reaching_cdc_total_space 
-------------------------------- live log call ---------------------------------
02:58:36,929 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:37,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:37,14 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:37,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:37,80 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:58:37,134 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:58:37,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:58:37,218 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
cdc_test.py::TestCDC::test_cdc_data_available_in_cdc_raw 
-------------------------------- live log call ---------------------------------
02:59:08,632 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:59:08,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:59:08,717 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:59:08,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:59:08,784 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:59:08,837 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:59:08,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:59:08,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:59:27,607 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:59:27,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:59:27,693 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:59:27,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:59:27,761 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_cdc_enabled_data_readable_on_round_trip passed 1 out of the required 1 times. Success!
test_cdc_disabled_data_readable_on_round_trip passed 1 out of the required 1 times. Success!
test_non_cdc_segments_deleted_after_replay passed 1 out of the required 1 times. Success!
test_insertion_and_commitlog_behavior_after_reaching_cdc_total_space passed 1 out of the required 1 times. Success!
test_cdc_data_available_in_cdc_raw passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 5 passed in 241.05 seconds ==========================
[msx] rc = 0
