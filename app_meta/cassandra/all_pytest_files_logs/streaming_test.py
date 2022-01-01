cassandra streaming_test.py true true
the_test is streaming_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

streaming_test.py::TestStreaming::test_zerocopy_streaming 
-------------------------------- live log call ---------------------------------
11:58:37,931 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:58:38,16 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:58:38,16 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:58:38,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:58:38,84 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:58:38,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:58:38,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:58:38,258 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:58:38,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:58:38,324 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:58:38,377 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:58:38,461 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:58:38,462 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:58:38,511 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:58:38,595 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:58:38,595 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
streaming_test.py::TestStreaming::test_zerocopy_streaming_no_replication 
-------------------------------- live log call ---------------------------------
11:59:18,902 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:59:18,987 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:59:18,987 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:59:19,59 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:59:19,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:59:19,236 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:59:19,302 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,392 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:59:19,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:59:19,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:59:19,542 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,594 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:59:19,678 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:59:19,679 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,728 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:59:19,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:59:19,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:59:19,862 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:59:19,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:59:19,946 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_zerocopy_streaming passed 1 out of the required 1 times. Success!
test_zerocopy_streaming_no_replication passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 82.71 seconds ===========================
[msx] rc = 0
