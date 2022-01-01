cassandra configuration_test.py true true
the_test is configuration_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

configuration_test.py::TestConfiguration::test_compression_chunk_length 
-------------------------------- live log call ---------------------------------
03:40:11,590 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:11,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:11,674 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:40:11,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:11,743 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
configuration_test.py::TestConfiguration::test_change_durable_writes 
-------------------------------- live log call ---------------------------------
03:40:18,554 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:18,639 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:18,639 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:40:18,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:18,705 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:40:18,758 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:18,843 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:18,843 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:40:45,136 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:45,221 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:45,221 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:40:45,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:45,287 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:40:45,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:40:45,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:40:45,424 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_compression_chunk_length passed 1 out of the required 1 times. Success!
test_change_durable_writes passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 63.93 seconds ===========================
[msx] rc = 0
