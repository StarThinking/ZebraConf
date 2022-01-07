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
02:42:59,25 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:59,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:42:59,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:42:59,278 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:59,383 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:42:59,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:42:59,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:42:59,631 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:42:59,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
02:43:29,293 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:43:30,500 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:43:32,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:43:36,520 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:43:43,543 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:43:50,956 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:43:50,957 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:43:51,963 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:43:53,55 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:43:53,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:43:53,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 12%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_forwards_between_and_cleanup 
-------------------------------- live log setup --------------------------------
02:45:14,380 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:45:14,465 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:45:14,537 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:45:14,660 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:45:14,746 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:45:14,818 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:45:14,914 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:45:14,998 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:45:15,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
02:45:35,734 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:45:35,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:45:35,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:46:43,283 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:46:44,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:46:46,497 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:46:50,409 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:46:59,238 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 25%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_forwards_and_cleanup 
-------------------------------- live log setup --------------------------------
02:48:04,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:04,771 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:48:04,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:48:04,936 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:05,21 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:48:05,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:48:05,186 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:05,271 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:48:05,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
02:48:26,379 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:48:26,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:48:26,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:49:35,238 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:49:36,344 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:49:38,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:49:43,165 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:49:51,492 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 37%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_backwards_between_and_cleanup 
-------------------------------- live log setup --------------------------------
02:50:56,962 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:50:57,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:50:57,116 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:50:57,211 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:50:57,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:50:57,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:50:57,460 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:50:57,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:50:57,615 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
02:51:17,601 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:51:17,697 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:51:17,773 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:52:25,274 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:52:26,381 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:52:28,87 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:52:31,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:52:40,728 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_move_backwards_and_cleanup 
-------------------------------- live log setup --------------------------------
02:53:47,10 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:53:47,96 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:53:47,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:53:47,261 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:53:47,346 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:53:47,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:53:47,511 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:53:47,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:53:47,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
02:54:07,477 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:54:07,571 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:54:07,649 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:55:14,129 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:55:15,135 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:55:17,245 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:55:20,956 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:55:28,883 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 62%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_decommission 
-------------------------------- live log setup --------------------------------
02:56:37,59 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:56:37,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:56:37,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:56:37,309 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:56:37,393 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:56:37,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:56:37,557 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:56:37,641 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:56:37,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
02:56:57,564 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:56:57,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:56:57,763 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
02:58:05,252 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
02:58:06,261 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:58:08,368 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:58:12,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
02:58:20,807 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 75%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_remove 
-------------------------------- live log setup --------------------------------
02:59:52,228 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:59:52,314 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:59:52,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:59:52,478 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:59:52,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:59:52,633 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:59:52,727 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:59:52,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:59:52,881 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
03:00:12,663 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:00:12,765 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:00:12,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
03:01:11,495 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
03:01:12,500 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:01:14,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:01:19,21 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:01:26,145 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
03:01:41,584 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 87%]
transient_replication_ring_test.py::TestTransientReplicationRing::test_replace 
-------------------------------- live log setup --------------------------------
03:02:25,297 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:02:25,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:02:25,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:02:25,568 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:02:25,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:02:25,723 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:02:25,818 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:02:25,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:02:25,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
-------------------------------- live log call ---------------------------------
03:02:46,186 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
03:02:47,392 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:02:49,299 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:02:52,810 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:02:54,545 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:02:54,637 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
03:02:54,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = replacement
03:03:00,345 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:03:17,691 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
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

========================= 8 passed in 1245.62 seconds ==========================
[msx] rc = 0
