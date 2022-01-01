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
08:48:03,995 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:48:04,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:48:04,80 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:48:04,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:48:04,150 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:48:44,976 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:48:45,68 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:48:45,69 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:48:45,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:48:45,162 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:50:19,620 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
08:50:20,323 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 16%]
rebuild_test.py::TestRebuild::test_resumable_rebuild 
-------------------------------- live log call ---------------------------------
08:50:28,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:50:28,363 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:50:28,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:50:28,453 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:50:28,539 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:50:28,539 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:50:28,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:50:28,607 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:50:28,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:50:28,675 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:51:47,538 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:51:47,638 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:51:47,639 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:51:47,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:51:47,721 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:52:28,114 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
08:52:28,818 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 33%]
------------------------------ live log teardown -------------------------------
08:53:28,591 conftest ERROR Unexpected error in node2 log, error: 
ERROR [Stream-Deserializer-/127.0.0.3:7000-0b8b0220] 2021-12-31 07:52:32,375 StreamSession.java:888 - [Stream #4848a500-6a49-11ec-9165-efad27ad149e] Remote peer /127.0.0.3:7000 failed stream session.

rebuild_test.py::TestRebuild::test_rebuild_ranges 
-------------------------------- live log call ---------------------------------
08:53:29,562 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:53:29,647 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:53:29,647 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:53:29,699 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:53:29,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:53:29,784 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:53:29,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:53:29,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:53:37,409 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:53:37,504 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:53:37,504 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:53:37,562 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:53:37,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:53:37,658 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:53:37,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:53:37,731 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:54:53,118 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
08:54:54,41 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
08:54:56,739 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
08:54:57,849 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:55:00,54 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:55:04,676 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
rebuild_test.py::TestRebuild::test_disallow_rebuild_nonlocal_range 
-------------------------------- live log call ---------------------------------
08:55:11,992 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:12,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:12,77 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:12,144 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,236 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:12,320 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:12,321 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,387 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:12,387 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,477 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:12,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:55:12,563 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:55:12,629 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,681 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:12,767 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:12,767 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,816 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:12,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:12,901 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:12,951 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:13,36 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:55:13,36 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
rebuild_test.py::TestRebuild::test_disallow_rebuild_from_nonreplica 
-------------------------------- live log call ---------------------------------
08:55:34,565 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:34,651 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:34,651 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:34,718 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:34,718 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:34,809 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:34,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:34,894 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:34,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:34,961 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:35,52 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:35,137 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:55:35,137 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:35,203 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:55:35,203 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:35,256 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:35,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:35,341 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:35,391 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:35,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:35,475 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:35,525 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:35,611 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:55:35,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 83%]
rebuild_test.py::TestRebuild::test_rebuild_with_specific_sources 
-------------------------------- live log call ---------------------------------
08:55:57,125 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:57,216 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:57,217 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:57,283 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:55:57,283 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:57,374 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:55:57,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:57,459 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:55:57,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:55:57,525 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:56:16,571 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:56:16,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:56:16,668 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:56:16,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:56:16,748 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:57:32,174 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
08:57:33,315 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
08:57:36,71 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
08:57:37,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:57:38,886 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:57:42,496 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:57:51,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_simple_rebuild passed 1 out of the required 1 times. Success!
test_resumable_rebuild passed 1 out of the required 1 times. Success!
test_rebuild_ranges passed 1 out of the required 1 times. Success!
test_disallow_rebuild_nonlocal_range passed 1 out of the required 1 times. Success!
test_disallow_rebuild_from_nonreplica passed 1 out of the required 1 times. Success!
test_rebuild_with_specific_sources passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 6 passed in 597.21 seconds ==========================
[msx] rc = 0
