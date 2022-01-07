cassandra multidc_putget_test.py true true
the_test is multidc_putget_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

multidc_putget_test.py::TestMultiDCPutGet::test_putget_2dc_rf1 
-------------------------------- live log call ---------------------------------
21:47:02,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:47:02,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:47:02,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:47:02,930 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:47:03,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:47:03,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 50%]
multidc_putget_test.py::TestMultiDCPutGet::test_putget_2dc_rf2 
-------------------------------- live log call ---------------------------------
21:47:31,847 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:47:31,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:47:31,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:47:32,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:47:32,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:47:32,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:47:32,341 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:47:32,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:47:32,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:47:32,587 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:47:32,672 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:47:32,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [100%]
===Flaky Test Report===

test_putget_2dc_rf1 passed 1 out of the required 1 times. Success!
test_putget_2dc_rf2 passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 72.49 seconds ===========================
[msx] rc = 0
