cassandra delete_insert_test.py true true
the_test is delete_insert_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

delete_insert_test.py::TestDeleteInsert::test_delete_insert_search 
-------------------------------- live log call ---------------------------------
18:27:05,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:27:05,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:27:05,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:27:05,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:27:05,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:27:05,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:27:05,992 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:27:06,76 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:27:06,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:27:06,235 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:27:06,319 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:27:06,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [100%]
===Flaky Test Report===

test_delete_insert_search passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 33.29 seconds ===========================
[msx] rc = 0
