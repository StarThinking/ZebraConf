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
18:30:04,294 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:04,380 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:30:04,449 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:30:04,541 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:04,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:30:04,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:30:04,784 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:04,869 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:30:04,936 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:30:05,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:05,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:30:05,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [  9%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_bootstrap 
-------------------------------- live log call ---------------------------------
18:30:58,324 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:58,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:30:58,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:30:58,569 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:58,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:30:58,721 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:30:58,813 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:58,898 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:30:58,995 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:30:59,91 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:30:59,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:30:59,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:31:41,960 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:31:42,49 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
18:31:42,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 18%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_replace_same_address 
-------------------------------- live log call ---------------------------------
18:32:59,330 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:32:59,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:32:59,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:32:59,576 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:32:59,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:32:59,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:32:59,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:32:59,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:32:59,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:33:00,66 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:33:00,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:33:00,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:33:44,145 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:33:44,232 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
18:33:44,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 27%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_replace_different_address 
-------------------------------- live log call ---------------------------------
18:34:43,309 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:34:43,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:34:43,462 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:34:43,555 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:34:43,640 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:34:43,707 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:34:43,800 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:34:43,884 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:34:43,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:34:44,44 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:34:44,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:34:44,197 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:35:27,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:35:27,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
18:35:28,13 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 36%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_decommission 
-------------------------------- live log call ---------------------------------
18:37:29,1 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:37:29,86 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:37:29,153 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:37:29,245 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:37:29,330 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:37:29,397 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:37:29,489 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:37:29,573 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:37:29,640 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:37:29,732 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:37:29,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
18:37:29,884 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 45%]
disk_balance_test.py::TestDiskBalance::test_blacklisted_directory 
-------------------------------- live log call ---------------------------------
18:39:32,306 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:39:32,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:39:32,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 54%]
disk_balance_test.py::TestDiskBalance::test_alter_replication_factor 
-------------------------------- live log call ---------------------------------
18:41:06,889 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:41:06,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:41:07,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:41:07,136 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:41:07,222 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:41:07,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:41:07,381 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:41:07,467 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:41:07,534 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:41:41,422 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 63%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_boundary_change_stcs 
-------------------------------- live log call ---------------------------------
18:42:07,61 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:42:07,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:42:07,217 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:44:38,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:44:38,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:44:38,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:44:38,512 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:44:38,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 72%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_boundary_change_lcs 
-------------------------------- live log call ---------------------------------
18:49:04,36 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:49:04,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:49:04,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:51:34,711 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:51:34,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:51:34,867 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:51:34,919 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:51:35,7 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 81%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_joining_ring_stcs 
-------------------------------- live log call ---------------------------------
18:56:13,777 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:56:13,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:56:13,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:56:14,30 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:56:14,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:56:14,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:56:14,277 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:56:14,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:56:14,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 90%]
disk_balance_test.py::TestDiskBalance::test_disk_balance_after_joining_ring_lcs 
-------------------------------- live log call ---------------------------------
19:00:50,968 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:00:51,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:00:51,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:00:51,215 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:00:51,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:00:51,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:00:51,464 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:00:51,550 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:00:51,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
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

========================= 11 passed in 2128.48 seconds =========================
[msx] rc = 0
