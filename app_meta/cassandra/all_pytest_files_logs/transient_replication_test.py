cassandra transient_replication_test.py true true
the_test is transient_replication_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 26 items

transient_replication_test.py::TestTransientReplication::test_transient_noop_write 
-------------------------------- live log setup --------------------------------
12:54:33,897 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:54:33,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:54:33,983 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:54:34,56 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:54:34,56 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:54:34,151 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:54:34,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:54:34,235 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:54:34,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:54:34,305 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:54:34,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:54:34,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:54:34,484 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:54:34,553 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:54:34,554 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  3%]
transient_replication_test.py::TestTransientReplication::test_transient_write 
-------------------------------- live log setup --------------------------------
12:55:03,700 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:55:03,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:55:03,790 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:03,861 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:55:03,861 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:03,956 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:55:04,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:55:04,41 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:04,113 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:55:04,113 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:04,208 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:55:04,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:55:04,293 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:04,363 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:55:04,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  7%]
transient_replication_test.py::TestTransientReplication::test_transient_full_merge_read 
-------------------------------- live log setup --------------------------------
12:55:37,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:55:37,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:55:37,337 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:37,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:55:37,408 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:37,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:55:37,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:55:37,588 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:37,690 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:55:37,691 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:37,787 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:55:37,872 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:55:37,872 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:55:37,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:55:37,942 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 11%]
transient_replication_test.py::TestTransientReplication::test_srp 
-------------------------------- live log setup --------------------------------
12:56:21,729 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:56:21,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:56:21,815 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:56:21,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:56:21,886 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:56:21,983 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:56:22,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:56:22,68 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:56:22,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:56:22,139 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:56:22,235 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:56:22,321 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:56:22,321 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:56:22,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:56:22,392 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 15%]
transient_replication_test.py::TestTransientReplication::test_transient_full_merge_read_with_delete_transient_coordinator 
-------------------------------- live log setup --------------------------------
12:57:05,700 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:57:05,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:57:05,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:05,859 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:57:05,859 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:05,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:57:06,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:57:06,40 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:06,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:57:06,111 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:06,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:57:06,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:57:06,292 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:06,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:57:06,368 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 19%]
transient_replication_test.py::TestTransientReplication::test_transient_full_merge_read_with_delete_full_coordinator 
-------------------------------- live log setup --------------------------------
12:57:49,935 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:57:50,21 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:57:50,21 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:50,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:57:50,93 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:50,188 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:57:50,314 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:57:50,314 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:50,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:57:50,385 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:50,479 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:57:50,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:57:50,563 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:57:50,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:57:50,633 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 23%]
transient_replication_test.py::TestTransientReplication::test_cheap_quorums 
-------------------------------- live log setup --------------------------------
12:58:34,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:58:35,2 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:58:35,2 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:58:35,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:58:35,75 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:58:35,196 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:58:35,282 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:58:35,282 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:58:35,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:58:35,354 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:58:35,450 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:58:35,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:58:35,535 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:58:35,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:58:35,606 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 26%]
transient_replication_test.py::TestTransientReplication::test_speculative_write 
-------------------------------- live log setup --------------------------------
12:58:59,952 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:59:00,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:59:00,40 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:00,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:59:00,111 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:00,208 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:59:00,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:59:00,293 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:00,364 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:59:00,364 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:00,460 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:59:00,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:59:00,546 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:00,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:59:00,617 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 30%]
transient_replication_test.py::TestTransientReplication::test_keyspace_rf_changes SKIPPED [ 34%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_speculative_write_repair_cycle 
-------------------------------- live log setup --------------------------------
12:59:28,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:59:29,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:59:29,85 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:29,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:59:29,157 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:29,254 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:59:29,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:59:29,339 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:29,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:59:29,410 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:29,506 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:59:29,591 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:59:29,591 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:59:29,662 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:59:29,662 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 38%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_primary_range_repair 
-------------------------------- live log setup --------------------------------
13:00:12,597 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:00:12,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:00:12,683 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:12,753 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:00:12,753 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:12,848 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:00:12,933 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:00:12,933 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:13,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:00:13,3 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:13,101 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:00:13,187 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:00:13,187 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:13,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:00:13,258 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 42%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_optimized_primary_range_repair 
-------------------------------- live log setup --------------------------------
13:00:57,212 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:00:57,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:00:57,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:57,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:00:57,370 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:57,466 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:00:57,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:00:57,552 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:57,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:00:57,622 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:57,718 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:00:57,803 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:00:57,803 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:00:57,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:00:57,874 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 46%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_optimized_primary_range_repair_with_lcs 
-------------------------------- live log setup --------------------------------
13:01:41,63 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:01:41,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:01:41,150 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:01:41,223 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:01:41,223 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:01:41,319 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:01:41,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:01:41,404 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:01:41,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:01:41,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:01:41,570 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:01:41,655 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:01:41,655 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:01:41,725 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:01:41,725 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_transient_incremental_repair 
-------------------------------- live log setup --------------------------------
13:02:27,182 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:02:27,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:02:27,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:02:27,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:02:27,339 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:02:27,435 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:02:27,521 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:02:27,522 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:02:27,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:02:27,592 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:02:27,694 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:02:27,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:02:27,781 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:02:27,851 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:02:27,851 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_full_repair_from_full_replica 
-------------------------------- live log setup --------------------------------
13:03:12,41 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:03:12,133 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:03:12,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:12,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:03:12,245 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:12,341 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:03:12,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:03:12,426 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:12,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:03:12,496 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:12,591 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:03:12,676 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:03:12,676 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:12,745 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:03:12,746 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 57%]
transient_replication_test.py::TestTransientReplicationRepairStreamEntireSSTable::test_full_repair_from_transient_replica 
-------------------------------- live log setup --------------------------------
13:03:44,870 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:03:44,956 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:03:44,956 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:45,26 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:03:45,26 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:45,120 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:03:45,205 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:03:45,206 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:45,277 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:03:45,277 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:45,372 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:03:45,457 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:03:45,457 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:03:45,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:03:45,527 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 61%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_speculative_write_repair_cycle 
-------------------------------- live log setup --------------------------------
13:04:17,439 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:04:17,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:04:17,525 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:04:17,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:04:17,597 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:04:17,693 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:04:17,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:04:17,780 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:04:17,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:04:17,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:04:17,949 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:04:18,36 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:04:18,36 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:04:18,107 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:04:18,108 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 65%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_primary_range_repair 
-------------------------------- live log setup --------------------------------
13:05:01,803 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:05:01,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:05:01,890 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:01,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:05:01,961 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:02,61 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:05:02,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:05:02,147 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:02,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:05:02,218 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:02,314 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:05:02,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:05:02,399 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:02,469 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:05:02,469 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 69%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_optimized_primary_range_repair 
-------------------------------- live log setup --------------------------------
13:05:45,921 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:05:46,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:05:46,8 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:46,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:05:46,79 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:46,176 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:05:46,261 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:05:46,262 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:46,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:05:46,333 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:46,429 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:05:46,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:05:46,514 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:05:46,585 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:05:46,586 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 73%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_optimized_primary_range_repair_with_lcs 
-------------------------------- live log setup --------------------------------
13:06:30,286 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:06:30,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:06:30,372 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:06:30,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:06:30,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:06:30,538 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:06:30,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:06:30,624 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:06:30,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:06:30,694 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:06:30,792 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:06:30,878 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:06:30,878 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:06:30,949 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:06:30,949 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 76%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_transient_incremental_repair 
-------------------------------- live log setup --------------------------------
13:07:15,664 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:07:15,751 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:07:15,751 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:07:15,822 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:07:15,822 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:07:15,922 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:07:16,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:07:16,8 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:07:16,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:07:16,80 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:07:16,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:07:16,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:07:16,262 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:07:16,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:07:16,333 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_full_repair_from_full_replica 
-------------------------------- live log setup --------------------------------
13:07:59,778 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:07:59,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:07:59,865 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:07:59,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:07:59,938 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:00,34 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:08:00,119 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:08:00,119 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:00,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:08:00,191 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:00,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:08:00,372 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:08:00,372 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:00,442 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:08:00,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 84%]
transient_replication_test.py::TestTransientReplicationRepairLegacyStreaming::test_full_repair_from_transient_replica 
-------------------------------- live log setup --------------------------------
13:08:33,845 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:08:33,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:08:33,932 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:34,2 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:08:34,2 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:34,98 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:08:34,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:08:34,184 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:34,256 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:08:34,256 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:34,353 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:08:34,442 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:08:34,442 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:08:34,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:08:34,514 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 88%]
transient_replication_test.py::TestTransientReplicationSpeculativeQueries::test_always_speculate 
-------------------------------- live log setup --------------------------------
13:09:06,909 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:09:06,996 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:09:06,996 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:07,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:09:07,68 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:07,164 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:09:07,252 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:09:07,253 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:07,326 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:09:07,326 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:07,422 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:09:07,552 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:09:07,553 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:07,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:09:07,624 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 92%]
transient_replication_test.py::TestTransientReplicationSpeculativeQueries::test_custom_speculate 
-------------------------------- live log setup --------------------------------
13:09:37,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:09:37,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:09:37,308 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:37,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:09:37,379 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:37,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:09:37,560 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:09:37,560 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:37,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:09:37,630 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:37,725 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:09:37,810 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:09:37,810 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:09:37,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:09:37,881 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 96%]
transient_replication_test.py::TestMultipleTransientNodes::test_transient_full_merge_read 
-------------------------------- live log setup --------------------------------
13:10:07,260 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:10:07,347 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:10:07,347 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:07,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:10:07,418 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:07,514 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:10:07,599 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:10:07,599 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:07,670 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:10:07,670 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:07,766 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:10:07,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:10:07,852 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:07,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:10:07,923 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:08,19 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:10:08,104 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
13:10:08,104 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:08,175 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
13:10:08,175 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:08,282 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:10:08,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
13:10:08,367 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:10:08,438 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
13:10:08,438 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_transient_noop_write passed 1 out of the required 1 times. Success!
test_transient_write passed 1 out of the required 1 times. Success!
test_transient_full_merge_read passed 1 out of the required 1 times. Success!
test_srp passed 1 out of the required 1 times. Success!
test_transient_full_merge_read_with_delete_transient_coordinator passed 1 out of the required 1 times. Success!
test_transient_full_merge_read_with_delete_full_coordinator passed 1 out of the required 1 times. Success!
test_cheap_quorums passed 1 out of the required 1 times. Success!
test_speculative_write passed 1 out of the required 1 times. Success!
test_speculative_write_repair_cycle passed 1 out of the required 1 times. Success!
test_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair_with_lcs passed 1 out of the required 1 times. Success!
test_transient_incremental_repair passed 1 out of the required 1 times. Success!
test_full_repair_from_full_replica passed 1 out of the required 1 times. Success!
test_full_repair_from_transient_replica passed 1 out of the required 1 times. Success!
test_speculative_write_repair_cycle passed 1 out of the required 1 times. Success!
test_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair passed 1 out of the required 1 times. Success!
test_optimized_primary_range_repair_with_lcs passed 1 out of the required 1 times. Success!
test_transient_incremental_repair passed 1 out of the required 1 times. Success!
test_full_repair_from_full_replica passed 1 out of the required 1 times. Success!
test_full_repair_from_transient_replica passed 1 out of the required 1 times. Success!
test_always_speculate passed 1 out of the required 1 times. Success!
test_custom_speculate passed 1 out of the required 1 times. Success!
test_transient_full_merge_read passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 25 passed, 1 skipped in 983.23 seconds ====================
[msx] rc = 0
