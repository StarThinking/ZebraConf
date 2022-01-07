cassandra deletion_test.py true true
the_test is deletion_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

deletion_test.py::TestDeletion::test_gc 
-------------------------------- live log call ---------------------------------
18:28:39,650 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:28:39,736 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:28:39,804 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
deletion_test.py::TestDeletion::test_tombstone_size 
-------------------------------- live log call ---------------------------------
18:28:53,382 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:28:53,469 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:28:53,536 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_gc passed 1 out of the required 1 times. Success!
test_tombstone_size passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 23.78 seconds ===========================
[msx] rc = 0
