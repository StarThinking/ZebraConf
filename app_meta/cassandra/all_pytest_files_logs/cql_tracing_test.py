cassandra cql_tracing_test.py true true
the_test is cql_tracing_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

cql_tracing_test.py::TestCqlTracing::test_tracing_simple 
-------------------------------- live log call ---------------------------------
04:25:07,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:07,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:25:07,384 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:07,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:25:07,453 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:07,544 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:07,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:25:07,630 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:07,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:25:07,696 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:07,787 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:07,872 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:25:07,872 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:07,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:25:07,938 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
cql_tracing_test.py::TestCqlTracing::test_tracing_unknown_impl 
-------------------------------- live log call ---------------------------------
04:25:30,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:30,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:25:30,389 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:30,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:25:30,455 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:30,551 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:30,637 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:25:30,638 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:30,706 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:25:30,706 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:30,797 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:30,881 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:25:30,882 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:30,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:25:30,947 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
cql_tracing_test.py::TestCqlTracing::test_tracing_default_impl 
-------------------------------- live log call ---------------------------------
04:25:53,325 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:53,412 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:25:53,412 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:53,478 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:25:53,478 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:53,568 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:53,679 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:25:53,679 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:53,745 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:25:53,745 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:53,835 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:25:53,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:25:53,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:25:53,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:25:53,988 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_tracing_simple passed 1 out of the required 1 times. Success!
test_tracing_unknown_impl passed 1 out of the required 1 times. Success!
test_tracing_default_impl passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 69.61 seconds ===========================
[msx] rc = 0
