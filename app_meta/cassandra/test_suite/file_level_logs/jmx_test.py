cassandra jmx_test.py true true
the_test is jmx_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 9 items

jmx_test.py::TestJMX::test_netstats 
-------------------------------- live log call ---------------------------------
19:42:58,762 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:42:58,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:42:58,916 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:42:59,8 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:42:59,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:42:59,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:42:59,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:42:59,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:42:59,400 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 11%]
jmx_test.py::TestJMX::test_table_metric_mbeans 
-------------------------------- live log call ---------------------------------
19:44:04,573 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:44:04,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:44:04,726 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:44:04,818 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:44:04,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:44:04,968 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:44:05,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:44:05,145 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:44:05,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 22%]
jmx_test.py::TestJMX::test_mv_metric_mbeans_release 
-------------------------------- live log call ---------------------------------
19:44:38,877 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:44:38,962 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:44:39,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
jmx_test.py::TestJMX::test_compactionstats 
-------------------------------- live log call ---------------------------------
19:44:50,603 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:44:50,688 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:44:50,754 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 44%]
jmx_test.py::TestJMX::test_phi 
-------------------------------- live log call ---------------------------------
19:45:55,970 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:45:56,56 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:45:56,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:45:56,213 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:45:56,297 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:45:56,363 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:45:56,454 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:45:56,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:45:56,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 55%]
jmx_test.py::TestJMX::test_set_get_batchlog_replay_throttle 
-------------------------------- live log call ---------------------------------
19:46:15,712 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:46:15,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:46:15,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:46:15,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:46:16,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:46:16,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 66%]
jmx_test.py::TestJMX::test_bloom_filter_false_ratio 
-------------------------------- live log call ---------------------------------
19:46:34,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:46:34,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:46:34,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 77%]
jmx_test.py::TestJMXSSL::test_jmx_connection 
-------------------------------- live log call ---------------------------------
19:47:10,988 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:47:11,74 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:47:11,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 88%]
jmx_test.py::TestJMXSSL::test_require_client_auth 
-------------------------------- live log call ---------------------------------
19:47:24,465 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:47:24,550 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:47:24,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_netstats passed 1 out of the required 1 times. Success!
test_table_metric_mbeans passed 1 out of the required 1 times. Success!
test_mv_metric_mbeans_release passed 1 out of the required 1 times. Success!
test_compactionstats passed 1 out of the required 1 times. Success!
test_phi passed 1 out of the required 1 times. Success!
test_set_get_batchlog_replay_throttle passed 1 out of the required 1 times. Success!
test_bloom_filter_false_ratio passed 1 out of the required 1 times. Success!
test_jmx_connection passed 1 out of the required 1 times. Success!
test_require_client_auth passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 9 passed in 280.52 seconds ==========================
[msx] rc = 0
