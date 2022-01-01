cassandra snitch_test.py true true
the_test is snitch_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

snitch_test.py::TestGossipingPropertyFileSnitch::test_prefer_local_reconnect_on_listen_address 
-------------------------------- live log call ---------------------------------
11:32:18,456 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:32:18,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:32:18,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:18,609 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:32:18,609 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:18,700 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:32:18,785 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:32:18,785 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:18,851 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:32:18,851 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:18,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:32:18,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:32:18,990 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:19,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:32:19,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:32:19,124 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:19,173 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:32:19,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:32:19,259 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:32:19,308 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:32:19,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:32:19,395 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
snitch_test.py::TestDynamicEndpointSnitch::test_multidatacenter_local_quorum 
-------------------------------- live log call ---------------------------------
11:33:42,331 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:42,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:33:42,417 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:42,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:33:42,483 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:42,575 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:42,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:33:42,660 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:42,727 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:33:42,727 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:42,818 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:42,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:33:42,903 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:42,969 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:33:42,969 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:43,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:43,145 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
11:33:43,145 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:43,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
11:33:43,212 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:43,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:43,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
11:33:43,388 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:43,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
11:33:43,454 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:43,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:43,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
11:33:43,631 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
11:33:43,698 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
11:33:43,698 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
11:33:43,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:43,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:33:43,839 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:43,889 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:43,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:33:43,999 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:44,50 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:44,136 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:33:44,136 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:44,187 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:44,273 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
11:33:44,273 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:44,324 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:44,409 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
11:33:44,409 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:33:44,459 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:33:44,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node6
11:33:44,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 44
PASSED                                                                   [100%]
===Flaky Test Report===

test_prefer_local_reconnect_on_listen_address passed 1 out of the required 1 times. Success!
test_multidatacenter_local_quorum passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 154.45 seconds ==========================
[msx] rc = 0
