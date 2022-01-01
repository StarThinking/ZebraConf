cassandra fqltool_test.py true true
the_test is fqltool_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 5 items

fqltool_test.py::TestFQLTool::test_replay 
-------------------------------- live log call ---------------------------------
05:06:03,783 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:06:03,871 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:06:03,871 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:06:03,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:06:03,940 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:06:04,30 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:06:04,117 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:06:04,117 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:06:04,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:06:04,184 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
fqltool_test.py::TestFQLTool::test_compare 
-------------------------------- live log call ---------------------------------
05:07:40,417 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:07:40,503 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:07:40,504 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:07:40,569 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:07:40,569 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
fqltool_test.py::TestFQLTool::test_compare_mismatch 
-------------------------------- live log call ---------------------------------
05:08:31,251 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:08:31,341 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:08:31,341 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:08:31,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:08:31,407 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
fqltool_test.py::TestFQLTool::test_jvmdtest 
-------------------------------- live log call ---------------------------------
05:10:27,786 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:10:27,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:10:27,874 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:10:27,939 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:10:27,940 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
fqltool_test.py::TestFQLTool::test_unclean_enable 
-------------------------------- live log call ---------------------------------
05:10:46,534 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:10:46,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:10:46,624 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:10:46,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:10:46,692 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_replay passed 1 out of the required 1 times. Success!
test_compare passed 1 out of the required 1 times. Success!
test_compare_mismatch passed 1 out of the required 1 times. Success!
test_jvmdtest passed 1 out of the required 1 times. Success!
test_unclean_enable passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 5 passed in 291.03 seconds ==========================
[msx] rc = 0
