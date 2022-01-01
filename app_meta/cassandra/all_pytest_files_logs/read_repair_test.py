cassandra read_repair_test.py true true
the_test is read_repair_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 15 items

read_repair_test.py::TestReadRepair::test_alter_rf_and_run_read_repair SKIPPED [  6%]
read_repair_test.py::TestReadRepair::test_read_repair_chance SKIPPED     [ 13%]
read_repair_test.py::TestReadRepair::test_range_slice_query_with_tombstones SKIPPED [ 20%]
read_repair_test.py::TestReadRepair::test_gcable_tombstone_resurrection_on_range_slice_query SKIPPED [ 26%]
read_repair_test.py::TestReadRepair::test_tracing_does_not_interfere_with_digest_calculation 
-------------------------------- live log call ---------------------------------
08:44:11,77 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:11,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:44:11,162 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:44:11,231 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:11,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:44:11,408 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:44:11,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,565 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:11,650 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:44:11,650 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,716 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:44:11,717 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,771 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:11,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:44:11,856 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:11,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:11,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:44:11,990 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:12,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:12,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:44:12,129 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
read_repair_test.py::TestSpeculativeReadRepair::test_failed_read_repair 
-------------------------------- live log setup --------------------------------
08:44:34,650 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:34,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:44:34,737 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:34,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:44:34,807 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:34,900 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:34,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:44:34,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:35,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:44:35,53 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:35,146 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:44:35,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:44:35,231 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:44:35,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:44:35,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
read_repair_test.py::TestSpeculativeReadRepair::test_normal_read_repair 
-------------------------------- live log setup --------------------------------
08:44:59,918 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:00,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:45:00,4 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:00,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:45:00,73 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:00,167 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:00,252 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:45:00,253 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:00,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:45:00,325 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:00,419 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:00,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:45:00,505 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:00,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:45:00,602 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 46%]
read_repair_test.py::TestSpeculativeReadRepair::test_speculative_data_request 
-------------------------------- live log setup --------------------------------
08:45:24,688 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:24,773 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:45:24,773 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:24,843 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:45:24,843 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:24,940 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:25,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:45:25,28 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:25,96 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:45:25,96 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:25,189 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:25,274 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:45:25,274 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:25,343 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:45:25,343 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
read_repair_test.py::TestSpeculativeReadRepair::test_speculative_write 
-------------------------------- live log setup --------------------------------
08:45:49,204 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:49,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:45:49,294 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:49,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:45:49,367 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:49,462 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:49,547 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:45:49,547 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:49,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:45:49,616 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:49,710 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:45:49,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:45:49,796 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:45:49,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:45:49,865 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
read_repair_test.py::TestSpeculativeReadRepair::test_quorum_requirement 
-------------------------------- live log setup --------------------------------
08:46:12,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:46:12,810 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:46:12,810 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:12,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:46:12,880 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:12,973 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:46:13,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:46:13,59 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:13,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:46:13,128 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:13,221 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:46:13,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:46:13,307 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:13,376 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:46:13,376 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
read_repair_test.py::TestSpeculativeReadRepair::test_quorum_requirement_on_speculated_read 
-------------------------------- live log setup --------------------------------
08:46:36,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:46:36,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:46:36,839 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:36,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:46:36,910 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:37,4 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:46:37,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:46:37,89 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:37,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:46:37,159 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:37,253 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:46:37,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:46:37,338 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:46:37,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:46:37,407 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 73%]
read_repair_test.py::TestReadRepairGuarantees::test_monotonic_reads[blocking] SKIPPED [ 80%]
read_repair_test.py::TestReadRepairGuarantees::test_monotonic_reads[none] SKIPPED [ 86%]
read_repair_test.py::TestReadRepairGuarantees::test_atomic_writes[blocking] SKIPPED [ 93%]
read_repair_test.py::TestReadRepairGuarantees::test_atomic_writes[none] SKIPPED [100%]
===Flaky Test Report===

test_tracing_does_not_interfere_with_digest_calculation passed 1 out of the required 1 times. Success!
test_failed_read_repair passed 1 out of the required 1 times. Success!
test_normal_read_repair passed 1 out of the required 1 times. Success!
test_speculative_data_request passed 1 out of the required 1 times. Success!
test_speculative_write passed 1 out of the required 1 times. Success!
test_quorum_requirement passed 1 out of the required 1 times. Success!
test_quorum_requirement_on_speculated_read passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 7 passed, 8 skipped in 173.10 seconds =====================
[msx] rc = 0
