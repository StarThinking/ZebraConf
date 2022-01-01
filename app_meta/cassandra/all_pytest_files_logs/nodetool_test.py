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
07:50:30,246 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:30,332 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:50:30,333 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:30,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:50:30,401 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:30,491 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:30,576 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:50:30,576 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:30,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:50:30,642 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:30,732 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:30,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:50:30,817 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:30,883 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:50:30,883 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  7%]
nodetool_test.py::TestNodetool::test_correct_dc_rack_in_nodetool_info 
-------------------------------- live log call ---------------------------------
07:50:54,507 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:54,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:50:54,593 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:54,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:50:54,659 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:54,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:54,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:50:54,835 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:54,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:50:54,901 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:54,992 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:55,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:50:55,77 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:50:55,143 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,234 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:55,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:50:55,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:50:55,385 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,439 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:55,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:50:55,527 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,576 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:55,663 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:50:55,663 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,713 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:55,803 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:50:55,804 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:50:55,855 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:50:55,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:50:55,940 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 15%]
nodetool_test.py::TestNodetool::test_nodetool_timeout_commands 
-------------------------------- live log call ---------------------------------
07:51:23,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:51:23,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:51:23,588 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:51:23,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:51:23,654 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 23%]
nodetool_test.py::TestNodetool::test_cleanup_when_no_replica_with_index 
-------------------------------- live log call ---------------------------------
07:51:58,58 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:51:58,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:51:58,143 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:51:58,209 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:51:58,209 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:51:58,299 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:51:58,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:51:58,384 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:51:58,450 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:51:58,450 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 30%]
nodetool_test.py::TestNodetool::test_cleanup_when_no_replica_without_index 
-------------------------------- live log call ---------------------------------
07:52:25,964 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:52:26,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:52:26,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:26,117 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:52:26,117 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:26,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:52:26,291 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:52:26,291 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:26,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:52:26,357 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 38%]
nodetool_test.py::TestNodetool::test_meaningless_notice_in_status 
-------------------------------- live log call ---------------------------------
07:52:53,123 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:52:53,209 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:52:53,210 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:53,276 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:52:53,276 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:53,368 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:52:53,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:52:53,453 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:53,519 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:52:53,519 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:53,610 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:52:53,695 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:52:53,696 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:52:53,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:52:53,762 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 46%]
nodetool_test.py::TestNodetool::test_set_get_batchlog_replay_throttle 
-------------------------------- live log call ---------------------------------
07:53:20,144 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:53:20,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:53:20,231 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:53:20,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:53:20,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:53:20,390 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:53:20,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:53:20,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:53:20,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:53:20,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
nodetool_test.py::TestNodetool::test_reloadlocalschema 
-------------------------------- live log call ---------------------------------
07:53:41,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:53:41,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:53:41,100 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:53:41,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:53:41,169 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:53:47,96 cassandra.protocol WARNING Server warning: Your replication factor 2 for keyspace test is higher than the number of nodes 1 for datacenter datacenter1
PASSED                                                                   [ 61%]
nodetool_test.py::TestNodetool::test_refresh_size_estimates_clears_invalid_entries 
-------------------------------- live log call ---------------------------------
07:53:52,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:53:52,347 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:53:52,347 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:53:52,414 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:53:52,414 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 69%]
nodetool_test.py::TestNodetool::test_set_get_concurrent_view_builders 
-------------------------------- live log call ---------------------------------
07:54:00,202 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:00,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:54:00,288 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:00,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:54:00,354 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:00,447 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:00,533 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:54:00,533 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:00,599 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:54:00,600 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 76%]
nodetool_test.py::TestNodetool::test_describecluster_more_information_three_datacenters 
-------------------------------- live log call ---------------------------------
07:54:22,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:22,671 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:54:22,672 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:22,738 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:54:22,738 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:22,829 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:22,914 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:54:22,914 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:22,980 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:54:22,980 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:23,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:23,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:54:23,159 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:23,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:54:23,225 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:23,316 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:23,400 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:54:23,400 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:23,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:54:23,467 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:40,981 cassandra.protocol WARNING Server warning: Your replication factor 5 for keyspace ks1 is higher than the number of nodes 2 for datacenter dc2
07:54:40,982 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks1 is higher than the number of nodes 1 for datacenter dc1
07:54:41,858 cassandra.protocol WARNING Server warning: Your replication factor 5 for keyspace ks2 is higher than the number of nodes 2 for datacenter dc2
07:54:41,859 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks2 is higher than the number of nodes 1 for datacenter dc1
PASSED                                                                   [ 84%]
nodetool_test.py::TestNodetool::test_sjk 
-------------------------------- live log call ---------------------------------
07:54:49,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:54:49,843 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:54:49,843 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:54:49,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:54:49,910 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

==================== 12 passed, 1 skipped in 270.63 seconds ====================
[msx] rc = 0
