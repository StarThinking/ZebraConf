cassandra compression_test.py true true
the_test is compression_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 4 items

compression_test.py::TestCompression::test_disable_compression_cql 
-------------------------------- live log call ---------------------------------
03:37:36,416 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:36,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:36,500 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:37:36,568 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:36,568 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
compression_test.py::TestCompression::test_compression_cql_options 
-------------------------------- live log call ---------------------------------
03:37:45,136 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:45,219 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:45,220 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:37:45,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:45,285 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
compression_test.py::TestCompression::test_compression_cql_disabled_with_alter 
-------------------------------- live log call ---------------------------------
03:37:55,353 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:37:55,441 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:55,441 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:37:55,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:37:55,507 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
compression_test.py::TestCompression::test_compression_cql_enabled_with_alter 
-------------------------------- live log call ---------------------------------
03:38:02,71 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:38:02,155 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:38:02,156 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:38:02,221 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:38:02,222 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_disable_compression_cql passed 1 out of the required 1 times. Success!
test_compression_cql_options passed 1 out of the required 1 times. Success!
test_compression_cql_disabled_with_alter passed 1 out of the required 1 times. Success!
test_compression_cql_enabled_with_alter passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 4 passed in 33.21 seconds ===========================
[msx] rc = 0
