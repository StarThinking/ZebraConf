cassandra gossip_test.py true true
the_test is gossip_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 4 items

gossip_test.py::TestGossip::test_assassination_of_unknown_node 
-------------------------------- live log call ---------------------------------
19:22:08,119 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:08,206 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:22:08,275 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:22:08,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:08,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:22:08,518 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:22:08,609 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:08,695 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:22:08,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:22:08,852 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:08,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:22:09,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:22:09,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:09,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
19:22:09,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
19:22:09,301 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:09,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:22:09,440 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:09,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:22:09,577 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:09,663 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:22:09,713 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:09,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:22:09,849 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:09,935 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 25%]
gossip_test.py::TestGossip::test_assassinate_valid_node 
-------------------------------- live log call ---------------------------------
19:22:50,840 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:50,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:22:50,993 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:22:51,85 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:51,170 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:22:51,237 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:22:51,328 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:51,412 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:22:51,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:22:51,571 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:51,655 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:22:51,722 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:22:51,814 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:22:51,898 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
19:22:51,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
19:23:10,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:23:10,267 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:23:10,319 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:23:10,409 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:23:10,465 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:23:10,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:23:10,603 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:23:10,691 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:23:10,745 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:23:10,833 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 50%]
gossip_test.py::TestGossip::test_2dc_parallel_startup 
-------------------------------- live log call ---------------------------------
19:25:19,944 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:25:20,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:25:20,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:25:21,296 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:25:21,386 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:25:21,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:25:29,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:25:29,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:25:29,831 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:25:38,54 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:25:38,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:25:38,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 75%]
gossip_test.py::TestGossip::test_2dc_parallel_startup_one_seed 
-------------------------------- live log call ---------------------------------
19:27:24,944 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:27:25,30 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:27:25,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:27:26,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:27:26,409 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:27:26,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:27:34,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:27:34,765 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:27:34,836 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:27:44,56 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:27:44,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
19:27:44,228 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [100%]
===Flaky Test Report===

test_assassination_of_unknown_node passed 1 out of the required 1 times. Success!
test_assassinate_valid_node passed 1 out of the required 1 times. Success!
test_2dc_parallel_startup passed 1 out of the required 1 times. Success!
test_2dc_parallel_startup_one_seed passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 4 passed in 432.22 seconds ==========================
[msx] rc = 0
