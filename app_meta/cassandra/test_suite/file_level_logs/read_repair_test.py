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
22:48:27,403 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:27,488 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:48:27,557 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:48:27,648 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:27,733 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:48:27,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:48:27,891 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:27,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:48:28,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:48:28,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:28,181 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:48:28,231 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:28,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:48:28,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:28,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
read_repair_test.py::TestSpeculativeReadRepair::test_failed_read_repair 
-------------------------------- live log setup --------------------------------
22:48:53,234 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:53,319 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:48:53,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:48:53,483 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:53,568 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:48:53,637 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:48:53,732 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:48:53,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:48:53,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 40%]
read_repair_test.py::TestSpeculativeReadRepair::test_normal_read_repair 
-------------------------------- live log setup --------------------------------
22:49:19,757 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:49:19,845 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:49:19,914 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:49:20,9 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:49:20,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:49:20,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:49:20,281 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:49:20,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:49:20,437 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 46%]
read_repair_test.py::TestSpeculativeReadRepair::test_speculative_data_request 
-------------------------------- live log setup --------------------------------
22:49:45,283 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:49:45,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:49:45,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:49:45,538 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:49:45,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:49:45,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:49:45,790 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:49:45,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:49:45,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 53%]
read_repair_test.py::TestSpeculativeReadRepair::test_speculative_write 
-------------------------------- live log setup --------------------------------
22:50:10,370 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:10,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:50:10,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:50:10,623 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:10,708 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:50:10,778 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:50:10,873 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:10,958 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:50:11,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 60%]
read_repair_test.py::TestSpeculativeReadRepair::test_quorum_requirement 
-------------------------------- live log setup --------------------------------
22:50:34,414 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:34,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:50:34,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:50:34,667 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:34,752 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:50:34,821 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:50:34,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:35,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:50:35,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 66%]
read_repair_test.py::TestSpeculativeReadRepair::test_quorum_requirement_on_speculated_read 
-------------------------------- live log setup --------------------------------
22:50:59,460 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:59,546 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:50:59,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:50:59,711 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:50:59,796 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:50:59,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:50:59,960 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:51:00,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:51:00,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
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

==================== 7 passed, 8 skipped in 179.63 seconds =====================
[msx] rc = 0
