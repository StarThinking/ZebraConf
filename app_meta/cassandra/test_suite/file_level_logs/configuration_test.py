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
17:39:50,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:39:50,270 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:39:50,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
configuration_test.py::TestConfiguration::test_change_durable_writes 
-------------------------------- live log call ---------------------------------
17:39:57,148 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:39:57,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:39:57,302 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:39:57,356 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:39:57,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:40:26,316 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:40:26,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:40:26,468 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:40:26,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:40:26,605 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_compression_chunk_length passed 1 out of the required 1 times. Success!
test_change_durable_writes passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 65.80 seconds ===========================
[msx] rc = 0
