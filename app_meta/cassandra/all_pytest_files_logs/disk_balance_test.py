cassandra disk_balance_test.py true true
the_test is disk_balance_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 11 items

disk_balance_test.py::TestDiskBalance::test_disk_balance_stress 
-------------------------------- live log call ---------------------------------
04:30:12,156 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:30:12,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:30:12,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:12,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:30:12,317 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:12,409 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:30:12,497 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:30:12,497 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:12,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:30:12,565 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:12,657 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:30:12,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:30:12,744 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:12,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:30:12,811 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:12,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:30:12,992 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:30:12,992 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:30:13,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:30:13,60 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  9%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_bootstrap 
-------------------------------- live log call ---------------------------------
04:31:04,428 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:31:04,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:31:04,514 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:04,581 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:31:04,581 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:04,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:31:04,758 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:31:04,758 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:04,824 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:31:04,824 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:04,916 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:31:05,1 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:31:05,1 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:05,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:31:05,68 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:05,160 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:31:05,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:31:05,245 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:05,311 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:31:05,312 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:47,880 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:31:47,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:31:47,967 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:31:48,34 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:31:48,35 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 18%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_replace_same_address 
-------------------------------- live log call ---------------------------------
04:33:03,101 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:33:03,187 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:33:03,187 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:33:03,253 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,345 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:33:03,430 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:33:03,430 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:33:03,497 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,587 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:33:03,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:33:03,674 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,742 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:33:03,742 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,836 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:33:03,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:33:03,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:03,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:33:03,991 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:46,870 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:33:46,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:33:46,961 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:33:47,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:33:47,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 27%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_replace_different_address 
-------------------------------- live log call ---------------------------------
04:34:44,827 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:34:44,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:34:44,913 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:44,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:34:44,979 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:45,71 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:34:45,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:34:45,157 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:45,223 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:34:45,223 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:45,315 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:34:45,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:34:45,400 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:45,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:34:45,466 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:45,557 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:34:45,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:34:45,643 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:34:45,709 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:34:45,709 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:35:28,170 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:35:28,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:35:28,264 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:35:28,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
04:35:28,335 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_decommission 
-------------------------------- live log call ---------------------------------
04:37:28,318 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:37:28,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:37:28,404 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:28,471 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:37:28,471 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:28,562 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:37:28,647 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:37:28,647 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:28,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:37:28,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:28,805 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:37:28,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:37:28,890 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:28,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:37:28,957 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:29,49 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:37:29,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:37:29,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:37:29,200 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:37:29,201 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 45%]
disk_balance_test.py::TestDiskBalance::test_blacklisted_directory 
-------------------------------- live log call ---------------------------------
04:39:30,99 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:39:30,185 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:39:30,185 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:39:30,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:39:30,251 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 54%]
disk_balance_test.py::TestDiskBalance::test_alter_replication_factor 
-------------------------------- live log call ---------------------------------
04:41:06,347 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:41:06,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:41:06,433 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:41:06,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:41:06,500 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:41:06,591 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:41:06,676 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:41:06,676 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:41:06,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:41:06,743 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:41:06,834 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:41:06,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:41:06,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:41:06,986 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:41:06,986 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:41:39,126 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 63%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_boundary_change_stcs 
-------------------------------- live log call ---------------------------------
04:42:04,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:42:04,859 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:42:04,859 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:42:04,930 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:42:04,930 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:44:32,241 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:44:32,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:44:32,329 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:44:32,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:44:32,399 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:44:32,452 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:44:32,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:44:32,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 72%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_boundary_change_lcs 
-------------------------------- live log call ---------------------------------
04:48:52,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:48:53,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:48:53,39 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:48:53,107 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:48:53,107 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:51:20,677 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:51:20,768 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:51:20,768 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:51:20,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:51:20,837 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:51:20,890 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:51:20,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:51:20,976 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 81%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_joining_ring_stcs 
-------------------------------- live log call ---------------------------------
04:55:53,198 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:55:53,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:55:53,285 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:55:53,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:55:53,354 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:55:53,446 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:55:53,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:55:53,532 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:55:53,599 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:55:53,599 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:55:53,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:55:53,776 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:55:53,776 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:55:53,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:55:53,848 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 90%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_joining_ring_lcs 
-------------------------------- live log call ---------------------------------
05:00:26,904 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:00:26,993 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:00:26,993 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:00:27,61 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:00:27,61 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:00:27,153 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:00:27,241 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:00:27,241 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:00:27,308 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:00:27,308 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:00:27,401 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:00:27,487 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:00:27,487 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:00:27,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:00:27,554 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_disk_balance_stress passed 1 out of the required 1 times. Success!
test_disk_balance_bootstrap passed 1 out of the required 1 times. Success!
test_disk_balance_replace_same_address passed 1 out of the required 1 times. Success!
test_disk_balance_replace_different_address passed 1 out of the required 1 times. Success!
test_disk_balance_decommission passed 1 out of the required 1 times. Success!
test_blacklisted_directory passed 1 out of the required 1 times. Success!
test_alter_replication_factor passed 1 out of the required 1 times. Success!
test_disk_balance_after_boundary_change_stcs passed 1 out of the required 1 times. Success!
test_disk_balance_after_boundary_change_lcs passed 1 out of the required 1 times. Success!
test_disk_balance_after_joining_ring_stcs passed 1 out of the required 1 times. Success!
test_disk_balance_after_joining_ring_lcs passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 11 passed in 2090.82 seconds =========================
[msx] rc = 0
