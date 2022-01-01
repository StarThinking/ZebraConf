cassandra transient_replication_ring_test.py true true
the_test is transient_replication_ring_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 8 items

transient_replication_ring_test.py::TestTransientReplicationRing::test_bootstrap_and_cleanup 
-------------------------------- live log setup --------------------------------
12:33:10,709 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:33:10,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:33:10,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:33:10,867 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:33:10,868 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:33:10,962 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:33:11,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:33:11,47 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:33:11,116 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:33:11,116 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:33:11,210 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:33:11,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:33:11,295 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:33:11,364 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:33:11,365 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:33:39,462 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:33:40,671 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:33:42,778 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:33:47,91 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:33:56,319 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:34:01,509 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:34:01,510 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:34:03,3 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:34:03,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:34:03,101 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:34:03,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:34:03,178 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 12%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_forwards_between_and_cleanup 
-------------------------------- live log setup --------------------------------
12:35:23,320 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:35:23,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:35:23,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:35:23,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:35:23,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:35:23,573 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:35:23,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:35:23,659 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:35:23,729 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:35:23,729 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:35:23,825 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:35:23,910 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:35:23,910 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:35:24,16 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:35:24,16 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:35:43,659 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:35:43,754 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:35:43,755 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:35:43,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:35:43,830 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:36:50,620 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:36:51,627 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:36:53,933 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:36:58,45 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:37:05,69 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 25%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_forwards_and_cleanup 
-------------------------------- live log setup --------------------------------
12:38:10,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:38:10,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:38:10,160 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:38:10,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:38:10,230 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:38:10,324 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:38:10,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:38:10,410 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:38:10,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:38:10,479 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:38:10,574 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:38:10,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:38:10,660 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:38:10,730 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:38:10,730 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:38:30,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:38:30,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:38:30,435 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:38:30,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:38:30,517 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:39:37,264 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:39:38,373 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:39:40,380 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:39:44,192 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:39:52,318 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 37%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_backwards_between_and_cleanup 
-------------------------------- live log setup --------------------------------
12:40:56,682 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:40:56,768 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:40:56,768 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:40:56,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:40:56,838 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:40:56,934 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:40:57,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:40:57,19 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:40:57,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:40:57,89 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:40:57,183 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:40:57,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:40:57,269 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:40:57,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:40:57,339 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:41:16,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:41:16,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:41:16,288 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:41:16,365 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:41:16,365 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:42:23,51 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:42:24,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:42:26,167 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:42:30,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:42:39,308 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_backwards_and_cleanup 
-------------------------------- live log setup --------------------------------
12:43:42,758 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:43:42,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:43:42,844 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:43:42,914 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:43:42,914 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:43:43,10 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:43:43,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:43:43,95 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:43:43,165 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:43:43,165 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:43:43,260 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:43:43,345 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:43:43,345 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:43:43,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:43:43,415 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:44:03,86 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:44:03,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:44:03,182 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:44:03,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:44:03,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:45:09,984 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:45:11,192 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:45:13,99 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:45:17,212 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:45:25,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 62%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_decommission 
-------------------------------- live log setup --------------------------------
12:46:29,763 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:46:29,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:46:29,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:46:29,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:46:29,920 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:46:30,16 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:46:30,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:46:30,101 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:46:30,171 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:46:30,171 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:46:30,266 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:46:30,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:46:30,352 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:46:30,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:46:30,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:46:50,307 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:46:50,403 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:46:50,403 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:46:50,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:46:50,479 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:47:57,210 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:47:58,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:48:00,625 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:48:04,336 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:48:12,663 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 75%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_remove 
-------------------------------- live log setup --------------------------------
12:49:42,612 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:49:42,699 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:49:42,699 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:49:42,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:49:42,769 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:49:42,865 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:49:42,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:49:42,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:49:43,21 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:49:43,21 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:49:43,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:49:43,207 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:49:43,207 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:49:43,277 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:49:43,277 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:50:03,985 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:50:04,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:50:04,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:50:04,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
12:50:04,163 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:51:02,475 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
12:51:03,482 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
12:51:05,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
12:51:09,915 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
12:51:17,740 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
12:51:36,190 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 87%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_replace 
-------------------------------- live log setup --------------------------------
12:52:13,929 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:52:14,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:52:14,16 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:14,87 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
12:52:14,87 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:14,182 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:52:14,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:52:14,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:14,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
12:52:14,338 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:14,434 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:52:14,519 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:52:14,519 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:14,589 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
12:52:14,589 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
12:52:33,617 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
12:52:34,725 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:52:36,835 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:52:41,449 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:52:42,17 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
12:52:42,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
12:52:42,110 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:42,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
12:52:42,184 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
12:52:49,384 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
12:53:04,326 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_bootstrap_and_cleanup passed 1 out of the required 1 times. Success!
test_move_forwards_between_and_cleanup passed 1 out of the required 1 times. Success!
test_move_forwards_and_cleanup passed 1 out of the required 1 times. Success!
test_move_backwards_between_and_cleanup passed 1 out of the required 1 times. Success!
test_move_backwards_and_cleanup passed 1 out of the required 1 times. Success!
test_decommission passed 1 out of the required 1 times. Success!
test_remove passed 1 out of the required 1 times. Success!
test_replace passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================= 8 passed in 1222.30 seconds ==========================
[msx] rc = 0
