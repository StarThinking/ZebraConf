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
05:41:49,415 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:41:49,501 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:41:49,501 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:41:49,569 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:41:49,569 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:41:49,659 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:41:49,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:41:49,744 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:41:49,809 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:41:49,809 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:41:49,899 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:41:49,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:41:49,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:41:50,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:41:50,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 11%]
jmx_test.py::TestJMX::test_table_metric_mbeans 
-------------------------------- live log call ---------------------------------
05:42:52,678 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:42:52,764 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:42:52,764 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:42:52,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:42:52,830 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:42:52,920 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:42:53,5 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:42:53,5 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:42:53,71 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:42:53,71 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:42:53,161 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:42:53,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:42:53,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:42:53,311 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:42:53,311 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
jmx_test.py::TestJMX::test_mv_metric_mbeans_release 
-------------------------------- live log call ---------------------------------
05:43:24,746 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:43:24,833 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:43:24,833 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:43:24,898 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:43:24,898 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
jmx_test.py::TestJMX::test_compactionstats 
-------------------------------- live log call ---------------------------------
05:43:35,942 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:43:36,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:43:36,27 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:43:36,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:43:36,93 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 44%]
jmx_test.py::TestJMX::test_phi 
-------------------------------- live log call ---------------------------------
05:44:40,330 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:44:40,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:44:40,415 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:40,480 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:44:40,480 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:40,570 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:44:40,655 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:44:40,655 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:40,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:44:40,720 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:40,810 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:44:40,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:44:40,894 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:40,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:44:40,959 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 55%]
jmx_test.py::TestJMX::test_set_get_batchlog_replay_throttle 
-------------------------------- live log call ---------------------------------
05:44:59,54 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:44:59,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:44:59,139 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:59,204 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:44:59,204 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:59,293 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:44:59,378 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:44:59,378 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:44:59,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:44:59,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
jmx_test.py::TestJMX::test_bloom_filter_false_ratio 
-------------------------------- live log call ---------------------------------
05:45:16,160 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:45:16,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:45:16,245 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:45:16,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:45:16,310 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 77%]
jmx_test.py::TestJMXSSL::test_jmx_connection 
-------------------------------- live log call ---------------------------------
05:45:51,575 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:45:51,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:45:51,663 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:45:51,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:45:51,729 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 88%]
jmx_test.py::TestJMXSSL::test_require_client_auth 
-------------------------------- live log call ---------------------------------
05:46:03,305 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:46:03,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:46:03,390 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:46:03,456 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:46:03,456 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

========================== 9 passed in 268.22 seconds ==========================
[msx] rc = 0
