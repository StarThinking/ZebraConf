cassandra sstablesplit_test.py true true
the_test is sstablesplit_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

sstablesplit_test.py::TestSSTableSplit::test_split 
-------------------------------- live log call ---------------------------------
11:52:32,988 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:52:33,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:52:33,74 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:52:33,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:52:33,143 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
sstablesplit_test.py::TestSSTableSplit::test_single_file_split 
-------------------------------- live log call ---------------------------------
11:53:44,133 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:53:44,219 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:53:44,219 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:53:44,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:53:44,286 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_split passed 1 out of the required 1 times. Success!
test_single_file_split passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 99.63 seconds ===========================
[msx] rc = 0
