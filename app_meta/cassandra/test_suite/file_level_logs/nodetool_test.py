cassandra nodetool_test.py true true
the_test is nodetool_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 13 items

nodetool_test.py::TestNodetool::test_decommission_after_drain_is_invalid 
-------------------------------- live log call ---------------------------------
21:53:55,970 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:53:56,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:53:56,126 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:53:56,219 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:53:56,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:53:56,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:53:56,463 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:53:56,550 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:53:56,617 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  7%]
nodetool_test.py::TestNodetool::test_correct_dc_rack_in_nodetool_info 
-------------------------------- live log call ---------------------------------
21:54:21,231 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:21,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:54:21,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:54:21,477 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:21,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:54:21,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:54:21,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:21,810 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:54:21,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:54:21,969 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:22,55 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:54:22,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:54:22,178 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:22,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:54:22,315 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:22,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:54:22,452 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:22,544 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:54:22,596 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:22,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 15%]
nodetool_test.py::TestNodetool::test_nodetool_timeout_commands 
-------------------------------- live log call ---------------------------------
21:54:51,499 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:54:51,586 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:54:51,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 23%]
nodetool_test.py::TestNodetool::test_cleanup_when_no_replica_with_index 
-------------------------------- live log call ---------------------------------
21:55:29,805 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:55:29,892 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:55:29,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:55:30,53 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:55:30,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:55:30,206 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 30%]
nodetool_test.py::TestNodetool::test_cleanup_when_no_replica_without_index 
-------------------------------- live log call ---------------------------------
21:55:58,961 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:55:59,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:55:59,116 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:55:59,208 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:55:59,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:55:59,363 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 38%]
nodetool_test.py::TestNodetool::test_meaningless_notice_in_status 
-------------------------------- live log call ---------------------------------
21:56:27,123 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:56:27,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:56:27,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:56:27,371 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:56:27,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:56:27,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:56:27,618 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:56:27,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:56:27,772 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 46%]
nodetool_test.py::TestNodetool::test_set_get_batchlog_replay_throttle 
-------------------------------- live log call ---------------------------------
21:56:54,162 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:56:54,249 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:56:54,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:56:54,410 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:56:54,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:56:54,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 53%]
nodetool_test.py::TestNodetool::test_reloadlocalschema 
-------------------------------- live log call ---------------------------------
21:57:17,37 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:57:17,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:57:17,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:57:23,338 cassandra.protocol WARNING Server warning: Your replication factor 2 for keyspace test is higher than the number of nodes 1 for datacenter datacenter1
PASSED                                                                   [ 61%]
nodetool_test.py::TestNodetool::test_refresh_size_estimates_clears_invalid_entries 
-------------------------------- live log call ---------------------------------
21:57:29,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:57:29,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:57:29,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 69%]
nodetool_test.py::TestNodetool::test_set_get_concurrent_view_builders 
-------------------------------- live log call ---------------------------------
21:57:37,228 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:57:37,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:57:37,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:57:37,478 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:57:37,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:57:37,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 76%]
nodetool_test.py::TestNodetool::test_describecluster_more_information_three_datacenters 
-------------------------------- live log call ---------------------------------
21:58:01,884 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:58:01,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:58:02,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:58:02,135 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:58:02,222 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:58:02,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:58:02,381 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:58:02,468 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:58:02,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:58:02,627 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:58:02,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:58:02,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:58:21,144 cassandra.protocol WARNING Server warning: Your replication factor 5 for keyspace ks1 is higher than the number of nodes 2 for datacenter dc2
21:58:21,146 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks1 is higher than the number of nodes 1 for datacenter dc1
21:58:23,115 cassandra.protocol WARNING Server warning: Your replication factor 5 for keyspace ks2 is higher than the number of nodes 2 for datacenter dc2
21:58:23,116 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks2 is higher than the number of nodes 1 for datacenter dc1
PASSED                                                                   [ 84%]
nodetool_test.py::TestNodetool::test_sjk 
-------------------------------- live log call ---------------------------------
21:58:32,543 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:58:32,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:58:32,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 92%]
nodetool_test.py::TestNodetool::test_jobs_option_warning SKIPPED         [100%]
===Flaky Test Report===

test_decommission_after_drain_is_invalid passed 1 out of the required 1 times. Success!
test_correct_dc_rack_in_nodetool_info passed 1 out of the required 1 times. Success!
test_nodetool_timeout_commands passed 1 out of the required 1 times. Success!
test_cleanup_when_no_replica_with_index passed 1 out of the required 1 times. Success!
test_cleanup_when_no_replica_without_index passed 1 out of the required 1 times. Success!
test_meaningless_notice_in_status passed 1 out of the required 1 times. Success!
test_set_get_batchlog_replay_throttle passed 1 out of the required 1 times. Success!
test_reloadlocalschema passed 1 out of the required 1 times. Success!
test_refresh_size_estimates_clears_invalid_entries passed 1 out of the required 1 times. Success!
test_set_get_concurrent_view_builders passed 1 out of the required 1 times. Success!
test_describecluster_more_information_three_datacenters passed 1 out of the required 1 times. Success!
test_sjk passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 12 passed, 1 skipped in 288.19 seconds ====================
[msx] rc = 0
