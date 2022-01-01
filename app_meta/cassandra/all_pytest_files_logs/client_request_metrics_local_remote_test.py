cassandra client_request_metrics_local_remote_test.py true true
the_test is client_request_metrics_local_remote_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

client_request_metrics_local_remote_test.py::TestClientRequestMetricsLocalRemote::test_write_and_read 
-------------------------------- live log call ---------------------------------
03:05:31,182 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:31,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:05:31,266 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:05:31,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:05:31,334 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:05:31,424 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:05:31,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:05:31,507 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:05:31,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:05:31,574 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
client_request_metrics_local_remote_test.py::TestClientRequestMetricsLocalRemote::test_batch_and_slice 
-------------------------------- live log call ---------------------------------
03:06:01,93 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:01,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:06:01,178 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:01,243 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:06:01,244 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:01,334 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:01,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:06:01,419 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:01,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:06:01,484 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:22,325 cassandra.protocol WARNING Server warning: Batch for [ks.test] is of size 46000, exceeding specified threshold of 5120 by 40880.
PASSED                                                                   [ 66%]
client_request_metrics_local_remote_test.py::TestClientRequestMetricsLocalRemote::test_paxos 
-------------------------------- live log call ---------------------------------
03:06:30,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:30,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:06:30,838 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:30,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:06:30,903 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:30,993 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:06:31,76 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:06:31,76 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:06:31,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:06:31,142 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_write_and_read passed 1 out of the required 1 times. Success!
test_batch_and_slice passed 1 out of the required 1 times. Success!
test_paxos passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 87.30 seconds ===========================
[msx] rc = 0
