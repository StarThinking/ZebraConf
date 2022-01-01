cassandra multidc_putget_test.py true true
the_test is multidc_putget_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

multidc_putget_test.py::TestMultiDCPutGet::test_putget_2dc_rf1 
-------------------------------- live log call ---------------------------------
07:43:43,469 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:43:43,556 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:43:43,556 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:43:43,625 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:43:43,625 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:43:43,716 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:43:43,802 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:43:43,802 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:43:43,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:43:43,868 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
multidc_putget_test.py::TestMultiDCPutGet::test_putget_2dc_rf2 
-------------------------------- live log call ---------------------------------
07:44:11,623 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:44:11,709 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:44:11,709 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:11,776 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:44:11,776 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:11,866 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:44:11,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:44:11,952 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:12,18 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:44:12,19 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:12,113 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:44:12,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:44:12,201 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:12,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:44:12,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:12,358 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:44:12,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:44:12,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:44:12,510 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:44:12,510 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_putget_2dc_rf1 passed 1 out of the required 1 times. Success!
test_putget_2dc_rf2 passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 69.71 seconds ===========================
[msx] rc = 0
