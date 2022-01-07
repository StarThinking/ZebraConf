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
17:04:17,307 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:04:17,394 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:04:17,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:04:17,556 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:04:17,640 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:04:17,706 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 33%]
client_request_metrics_local_remote_test.py::TestClientRequestMetricsLocalRemote::test_batch_and_slice 
-------------------------------- live log call ---------------------------------
17:04:49,477 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:04:49,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:04:49,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:04:49,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:04:49,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:04:49,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:05:12,582 cassandra.protocol WARNING Server warning: Batch for [ks.test] is of size 46000, exceeding specified threshold of 5120 by 40880.
PASSED                                                                   [ 66%]
client_request_metrics_local_remote_test.py::TestClientRequestMetricsLocalRemote::test_paxos 
-------------------------------- live log call ---------------------------------
17:05:21,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:05:21,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:05:22,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:05:22,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:05:22,237 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:05:22,304 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [100%]
===Flaky Test Report===

test_write_and_read passed 1 out of the required 1 times. Success!
test_batch_and_slice passed 1 out of the required 1 times. Success!
test_paxos passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 92.83 seconds ===========================
[msx] rc = 0
