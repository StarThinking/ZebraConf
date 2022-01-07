cassandra fqltool_test.py true true
the_test is fqltool_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 5 items

fqltool_test.py::TestFQLTool::test_replay 
-------------------------------- live log call ---------------------------------
19:06:33,633 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:06:33,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:06:33,788 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:06:33,879 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:06:33,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:06:34,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 20%]
fqltool_test.py::TestFQLTool::test_compare 
-------------------------------- live log call ---------------------------------
19:08:22,796 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:08:22,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:08:22,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
fqltool_test.py::TestFQLTool::test_compare_mismatch 
-------------------------------- live log call ---------------------------------
19:09:09,871 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:09:09,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:09:10,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
fqltool_test.py::TestFQLTool::test_jvmdtest 
-------------------------------- live log call ---------------------------------
19:11:09,646 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:11:09,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:11:09,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 80%]
fqltool_test.py::TestFQLTool::test_unclean_enable 
-------------------------------- live log call ---------------------------------
19:11:29,393 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:11:29,478 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:11:29,544 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_replay passed 1 out of the required 1 times. Success!
test_compare passed 1 out of the required 1 times. Success!
test_compare_mismatch passed 1 out of the required 1 times. Success!
test_jvmdtest passed 1 out of the required 1 times. Success!
test_unclean_enable passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 5 passed in 304.55 seconds ==========================
[msx] rc = 0
