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
19:38:39,790 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:38:39,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:38:39,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:38:40,38 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:38:40,125 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:38:40,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:38:40,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:38:40,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:38:40,438 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 50%]
internode_ssl_test.py::TestInternodeSSL::test_putget_with_internode_ssl_without_compression 
-------------------------------- live log call ---------------------------------
19:39:18,319 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:39:18,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:39:18,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:39:18,567 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:39:18,651 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:39:18,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:39:18,809 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:39:18,892 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:39:18,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_putget_with_internode_ssl passed 1 out of the required 1 times. Success!
test_putget_with_internode_ssl_without_compression passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 77.49 seconds ===========================
[msx] rc = 0
