cassandra rebuild_test.py true true
the_test is rebuild_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 6 items

rebuild_test.py::TestRebuild::test_simple_rebuild 
-------------------------------- live log call ---------------------------------
22:52:27,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:52:27,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:52:27,331 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:53:08,460 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:53:08,547 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:53:08,639 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:54:43,213 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
22:54:43,701 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 16%]
rebuild_test.py::TestRebuild::test_resumable_rebuild 
-------------------------------- live log call ---------------------------------
22:54:51,231 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:54:51,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:54:51,407 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:54:51,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:54:51,559 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:54:51,628 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:56:11,90 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:56:11,192 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:56:11,277 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:56:53,897 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
22:56:54,395 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 33%]
rebuild_test.py::TestRebuild::test_rebuild_ranges 
-------------------------------- live log call ---------------------------------
22:57:58,135 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:57:58,221 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:57:58,274 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:57:58,359 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:57:58,425 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:58:06,186 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:58:06,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:58:06,337 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:58:06,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:58:06,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:59:22,16 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
22:59:23,144 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
22:59:25,995 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
22:59:27,105 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
22:59:29,311 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
22:59:33,626 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
rebuild_test.py::TestRebuild::test_disallow_rebuild_nonlocal_range 
-------------------------------- live log call ---------------------------------
22:59:41,22 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:59:41,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:59:41,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:59:41,266 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:59:41,350 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:59:41,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:59:41,508 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:59:41,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:59:41,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:59:41,712 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:59:41,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:59:41,847 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:59:41,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:59:41,982 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:59:42,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 66%]
rebuild_test.py::TestRebuild::test_disallow_rebuild_from_nonreplica 
-------------------------------- live log call ---------------------------------
23:00:04,858 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:04,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:00:05,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:00:05,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:05,188 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:00:05,254 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:00:05,346 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:05,430 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:00:05,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:00:05,549 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:05,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:00:05,684 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:05,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:00:05,819 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:05,905 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 83%]
rebuild_test.py::TestRebuild::test_rebuild_with_specific_sources 
-------------------------------- live log call ---------------------------------
23:00:28,437 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:28,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:00:28,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
23:00:28,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:28,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:00:28,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
23:00:49,296 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
23:00:49,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:00:49,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
23:02:06,17 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:02:07,144 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
23:02:10,217 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
23:02:11,224 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:02:13,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:02:17,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:02:24,459 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:02:40,399 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
23:03:15,689 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 59.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_simple_rebuild passed 1 out of the required 1 times. Success!
test_resumable_rebuild passed 1 out of the required 1 times. Success!
test_rebuild_ranges passed 1 out of the required 1 times. Success!
test_disallow_rebuild_nonlocal_range passed 1 out of the required 1 times. Success!
test_disallow_rebuild_from_nonreplica passed 1 out of the required 1 times. Success!
test_rebuild_with_specific_sources passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 6 passed in 661.77 seconds ==========================
[msx] rc = 0
