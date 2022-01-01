cassandra internode_ssl_test.py true true
the_test is internode_ssl_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

internode_ssl_test.py::TestInternodeSSL::test_putget_with_internode_ssl 
-------------------------------- live log call ---------------------------------
05:37:37,620 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:37:37,706 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:37:37,706 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:37:37,776 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:37:37,776 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:37:37,872 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:37:37,958 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:37:37,958 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:37:38,25 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:37:38,25 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:37:38,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:37:38,202 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:37:38,202 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:37:38,269 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:37:38,269 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
internode_ssl_test.py::TestInternodeSSL::test_putget_with_internode_ssl_without_compression 
-------------------------------- live log call ---------------------------------
05:38:14,466 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:38:14,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:38:14,554 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:38:14,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:38:14,624 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:38:14,715 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:38:14,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:38:14,800 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:38:14,866 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:38:14,866 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:38:14,958 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:38:15,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:38:15,42 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:38:15,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:38:15,109 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_putget_with_internode_ssl passed 1 out of the required 1 times. Success!
test_putget_with_internode_ssl_without_compression passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 74.23 seconds ===========================
[msx] rc = 0
