cassandra udtencoding_test.py true true
the_test is udtencoding_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

udtencoding_test.py::TestUDTEncoding::test_udt 
-------------------------------- live log call ---------------------------------
03:33:03,843 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:33:03,930 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:33:03,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:33:04,91 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:33:04,175 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:33:04,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:33:04,333 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:33:04,417 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:33:04,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_udt passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 22.09 seconds ===========================
[msx] rc = 0
