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
17:37:12,985 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:37:13,70 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:37:13,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 25%]
compression_test.py::TestCompression::test_compression_cql_options 
-------------------------------- live log call ---------------------------------
17:37:21,962 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:37:22,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:37:22,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
compression_test.py::TestCompression::test_compression_cql_disabled_with_alter 
-------------------------------- live log call ---------------------------------
17:37:32,687 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:37:32,772 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:37:32,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 75%]
compression_test.py::TestCompression::test_compression_cql_enabled_with_alter 
-------------------------------- live log call ---------------------------------
17:37:39,642 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:37:39,727 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:37:39,794 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_disable_compression_cql passed 1 out of the required 1 times. Success!
test_compression_cql_options passed 1 out of the required 1 times. Success!
test_compression_cql_disabled_with_alter passed 1 out of the required 1 times. Success!
test_compression_cql_enabled_with_alter passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 4 passed in 35.19 seconds ===========================
[msx] rc = 0
