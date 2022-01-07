cassandra sstableutil_test.py true true
the_test is sstableutil_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

sstableutil_test.py::TestSSTableUtil::test_compaction 
-------------------------------- live log call ---------------------------------
02:04:46,642 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:04:46,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:04:46,796 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
sstableutil_test.py::TestSSTableUtil::test_abortedcompaction 
-------------------------------- live log call ---------------------------------
02:05:42,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:05:42,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:05:42,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_compaction passed 1 out of the required 1 times. Success!
test_abortedcompaction passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 147.88 seconds ==========================
[msx] rc = 0
