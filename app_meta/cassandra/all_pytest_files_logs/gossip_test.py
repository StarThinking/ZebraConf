cassandra gossip_test.py true true
the_test is gossip_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 4 items

gossip_test.py::TestGossip::test_assassination_of_unknown_node 
-------------------------------- live log call ---------------------------------
05:21:30,323 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:30,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:21:30,410 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:30,478 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:21:30,478 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:30,568 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:30,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:21:30,653 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:30,719 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:21:30,719 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:30,809 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:30,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:21:30,894 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:30,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:21:30,959 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,49 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:31,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:21:31,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,200 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:21:31,200 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:31,374 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
05:21:31,374 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
05:21:31,440 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,494 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:31,579 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:21:31,579 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,631 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:31,715 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:21:31,716 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,765 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:31,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:21:31,849 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:31,898 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:31,982 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:21:31,982 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:21:32,31 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:21:32,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
05:21:32,115 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
gossip_test.py::TestGossip::test_assassinate_valid_node 
-------------------------------- live log call ---------------------------------
05:22:11,739 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:11,824 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:22:11,824 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:11,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:22:11,890 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:11,981 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:12,65 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:22:12,65 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,131 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:22:12,131 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,221 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:12,328 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:22:12,328 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:22:12,396 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,486 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:12,572 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:22:12,572 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,638 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:22:12,638 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,728 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:12,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
05:22:12,813 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:12,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
05:22:12,879 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:30,988 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:31,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:22:31,90 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:31,144 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:31,232 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:22:31,232 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:31,284 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:31,374 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:22:31,374 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:31,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:31,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:22:31,517 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:22:31,571 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:22:31,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
05:22:31,662 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
gossip_test.py::TestGossip::test_2dc_parallel_startup 
-------------------------------- live log call ---------------------------------
05:24:32,378 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:24:32,462 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:24:32,462 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:32,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:24:32,529 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:33,607 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:24:33,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:24:33,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:33,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:24:33,782 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:41,836 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:24:41,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:24:41,926 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:42,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:24:42,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:50,83 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:24:50,171 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:24:50,172 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:24:50,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:24:50,245 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
gossip_test.py::TestGossip::test_2dc_parallel_startup_one_seed 
-------------------------------- live log call ---------------------------------
05:26:35,271 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:26:35,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:26:35,355 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:35,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:26:35,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:36,478 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:26:36,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:26:36,563 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:36,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:26:36,631 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:44,649 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:26:44,735 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:26:44,736 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:44,805 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:26:44,806 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:52,882 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:26:52,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:26:52,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:26:53,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
05:26:53,44 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_assassination_of_unknown_node passed 1 out of the required 1 times. Success!
test_assassinate_valid_node passed 1 out of the required 1 times. Success!
test_2dc_parallel_startup passed 1 out of the required 1 times. Success!
test_2dc_parallel_startup_one_seed passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 4 passed in 419.43 seconds ==========================
[msx] rc = 0
