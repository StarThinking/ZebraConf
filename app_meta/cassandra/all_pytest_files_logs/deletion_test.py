cassandra deletion_test.py true true
the_test is deletion_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

deletion_test.py::TestDeletion::test_gc 
-------------------------------- live log call ---------------------------------
04:28:48,721 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:28:48,806 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:28:48,807 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:28:48,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:28:48,875 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
deletion_test.py::TestDeletion::test_tombstone_size 
-------------------------------- live log call ---------------------------------
04:29:01,700 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:29:01,785 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:29:01,785 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:29:01,851 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:29:01,851 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_gc passed 1 out of the required 1 times. Success!
test_tombstone_size passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 22.53 seconds ===========================
[msx] rc = 0
