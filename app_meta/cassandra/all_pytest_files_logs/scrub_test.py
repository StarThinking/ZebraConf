cassandra scrub_test.py true true
the_test is scrub_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 7 items

scrub_test.py::TestScrubIndexes::test_scrub_static_table 
-------------------------------- live log call ---------------------------------
10:52:19,695 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:52:19,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:52:19,780 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:52:19,848 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:52:19,848 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:52:55,720 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
10:52:55,724 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 14%]
scrub_test.py::TestScrubIndexes::test_standalone_scrub 
-------------------------------- live log call ---------------------------------
10:52:57,517 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:52:57,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:52:57,603 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:52:57,670 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:52:57,670 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:53:33,504 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [ 28%]
scrub_test.py::TestScrubIndexes::test_scrub_collections_table 
-------------------------------- live log call ---------------------------------
10:53:34,576 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:53:34,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:53:34,661 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:53:34,727 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:53:34,727 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 42%]
scrub_test.py::TestScrub::test_nodetool_scrub 
-------------------------------- live log call ---------------------------------
10:53:51,317 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:53:51,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:53:51,404 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:53:51,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:53:51,470 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 57%]
scrub_test.py::TestScrub::test_standalone_scrub 
-------------------------------- live log call ---------------------------------
10:54:17,592 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:54:17,678 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:54:17,678 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:54:17,745 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:54:17,745 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 71%]
scrub_test.py::TestScrub::test_standalone_scrub_essential_files_only 
-------------------------------- live log call ---------------------------------
10:54:41,857 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:54:41,942 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:54:41,942 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:54:42,10 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:54:42,10 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 85%]
scrub_test.py::TestScrub::test_scrub_with_UDT 
-------------------------------- live log call ---------------------------------
10:55:05,110 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
10:55:05,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:55:05,195 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
10:55:05,261 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
10:55:05,261 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_scrub_static_table passed 1 out of the required 1 times. Success!
test_standalone_scrub passed 1 out of the required 1 times. Success!
test_scrub_collections_table passed 1 out of the required 1 times. Success!
test_nodetool_scrub passed 1 out of the required 1 times. Success!
test_standalone_scrub passed 1 out of the required 1 times. Success!
test_standalone_scrub_essential_files_only passed 1 out of the required 1 times. Success!
test_scrub_with_UDT passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 7 passed in 176.72 seconds ==========================
[msx] rc = 0
