cassandra snitch_test.py true true
the_test is snitch_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

snitch_test.py::TestGossipingPropertyFileSnitch::test_prefer_local_reconnect_on_listen_address 
-------------------------------- live log call ---------------------------------
01:41:44,427 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:44,511 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:44,579 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:44,670 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:44,754 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:41:44,819 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:41:44,873 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:44,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:45,6 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:45,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:41:45,139 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:45,222 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:45,271 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:45,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 50%]
snitch_test.py::TestDynamicEndpointSnitch::test_multidatacenter_local_quorum 
-------------------------------- live log call ---------------------------------
01:43:10,50 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:10,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:10,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:10,292 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:10,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:43:10,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:43:10,532 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:10,615 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:43:10,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:43:10,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:10,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
01:43:10,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
01:43:11,13 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:11,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
01:43:11,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
01:43:11,254 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:11,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
01:43:11,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
01:43:11,459 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:11,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:11,592 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:11,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:43:11,725 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:11,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:43:11,858 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:11,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
01:43:11,993 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:12,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
01:43:12,156 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:12,239 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
PASSED                                                                   [100%]
===Flaky Test Report===

test_prefer_local_reconnect_on_listen_address passed 1 out of the required 1 times. Success!
test_multidatacenter_local_quorum passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 150.16 seconds ==========================
[msx] rc = 0
