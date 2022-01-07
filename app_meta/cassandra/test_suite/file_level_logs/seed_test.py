cassandra seed_test.py true true
the_test is seed_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

seed_test.py::TestGossiper::test_startup_no_live_seeds 
-------------------------------- live log call ---------------------------------
01:21:02,943 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:21:03,30 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:21:03,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:21:03,154 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:21:03,239 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
seed_test.py::TestGossiper::test_startup_non_seed_with_peers 
-------------------------------- live log call ---------------------------------
01:21:29,689 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:21:29,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:21:29,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:21:29,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:21:30,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:21:30,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:21:30,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:21:30,259 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:21:30,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:22:09,297 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:22:09,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:22:09,442 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:22:09,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:22:09,577 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:22:09,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 66%]
seed_test.py::TestGossiper::test_startup_after_ring_delay 
-------------------------------- live log call ---------------------------------
01:23:32,581 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:23:32,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:32,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:32,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:23:32,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:23:32,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [100%]
===Flaky Test Report===

test_startup_no_live_seeds passed 1 out of the required 1 times. Success!
test_startup_non_seed_with_peers passed 1 out of the required 1 times. Success!
test_startup_after_ring_delay passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 181.10 seconds ==========================
[msx] rc = 0
