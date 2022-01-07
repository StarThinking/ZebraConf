cassandra largecolumn_test.py true true
the_test is largecolumn_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

largecolumn_test.py::TestLargeColumn::test_cleanup 
-------------------------------- live log call ---------------------------------
19:53:46,732 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:53:46,820 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:53:46,889 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:53:46,981 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:53:47,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:53:47,133 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [100%]
===Flaky Test Report===

test_cleanup passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 66.64 seconds ===========================
[msx] rc = 0
