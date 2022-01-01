cassandra system_keyspaces_test.py true true
the_test is system_keyspaces_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

system_keyspaces_test.py::TestSystemKeyspaces::test_local_system_keyspaces 
-------------------------------- live log call ---------------------------------
12:05:13,888 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:05:13,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:05:13,975 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:05:14,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:05:14,44 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
system_keyspaces_test.py::TestSystemKeyspaces::test_replicated_system_keyspaces 
-------------------------------- live log call ---------------------------------
12:05:20,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:05:20,430 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:05:20,430 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:05:20,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:05:20,496 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_local_system_keyspaces passed 1 out of the required 1 times. Success!
test_replicated_system_keyspaces passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 13.73 seconds ===========================
[msx] rc = 0
