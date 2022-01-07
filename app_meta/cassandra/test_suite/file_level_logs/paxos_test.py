cassandra paxos_test.py true true
the_test is paxos_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 4 items

paxos_test.py::TestPaxos::test_replica_availability 
-------------------------------- live log call ---------------------------------
22:25:49,582 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:25:49,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:25:49,736 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:25:49,829 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:25:49,912 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:25:49,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:25:50,71 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:25:50,155 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:25:50,222 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:26:09,343 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
22:26:10,449 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:26:12,657 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:26:16,499 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
22:26:16,669 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:26:17,671 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:26:19,576 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:26:23,386 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:26:24,992 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:26:32,412 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:26:39,332 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 25%]
paxos_test.py::TestPaxos::test_cluster_availability 
-------------------------------- live log call ---------------------------------
22:26:54,746 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:26:54,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:26:54,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:26:55,10 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:26:55,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:26:55,160 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:26:55,252 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:26:55,336 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:26:55,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:27:15,406 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
22:27:16,612 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:27:18,619 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:27:22,563 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
22:27:23,133 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:27:23,634 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:27:25,439 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:27:29,650 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:27:31,457 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
22:27:37,574 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
22:27:48,606 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
paxos_test.py::TestPaxos::test_contention_multi_iterations SKIPPED       [ 75%]
paxos_test.py::TestPaxos::test_contention_many_threads 
-------------------------------- live log call ---------------------------------
22:28:00,989 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:28:01,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:28:01,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:28:01,233 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:28:01,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:28:01,383 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:28:01,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:28:01,559 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:28:01,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:28:20,938 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but load-balancing policies are not specified in some ExecutionProfiles. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.1'], EPs without explicit LBPs = ('EXEC_PROFILE_DEFAULT',))
22:28:20,951 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.1:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
22:28:20,956 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.1:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
PASSED                                                                   [100%]
===Flaky Test Report===

test_replica_availability passed 1 out of the required 1 times. Success!
test_cluster_availability passed 1 out of the required 1 times. Success!
test_contention_many_threads passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 3 passed, 1 skipped in 168.63 seconds =====================
[msx] rc = 0
