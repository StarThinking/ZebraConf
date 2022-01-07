cassandra wide_rows_test.py true true
the_test is wide_rows_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

wide_rows_test.py::TestWideRows::test_wide_rows 
-------------------------------- live log call ---------------------------------
03:44:54,863 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:44:54,950 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:44:55,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
wide_rows_test.py::TestWideRows::test_column_index_stress 
-------------------------------- live log call ---------------------------------
03:45:43,502 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:45:43,587 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:45:43,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:45:49,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:45:49,547 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_wide_rows passed 1 out of the required 1 times. Success!
test_column_index_stress passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 177.86 seconds ==========================
[msx] rc = 0
