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
08:21:33,519 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:21:33,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:21:33,604 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:21:33,676 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:21:33,676 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:21:33,768 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:21:33,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:21:33,853 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:21:33,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:21:33,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:21:34,11 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:21:34,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:21:34,95 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:21:34,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:21:34,162 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:21:52,699 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
08:21:53,705 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:21:55,912 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:21:59,832 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
08:22:00,426 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:22:00,927 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:22:02,932 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:22:06,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:22:08,751 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:22:14,565 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:22:22,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 25%]
paxos_test.py::TestPaxos::test_cluster_availability 
-------------------------------- live log call ---------------------------------
08:22:37,684 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:22:37,770 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:22:37,770 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:22:37,842 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:22:37,843 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:22:37,935 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:22:38,20 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:22:38,20 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:22:38,86 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:22:38,86 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:22:38,177 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:22:38,261 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:22:38,261 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:22:38,327 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:22:38,327 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:22:56,622 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
08:22:57,631 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:22:59,639 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:23:03,742 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
08:23:03,951 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:23:04,854 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:23:07,60 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:23:10,870 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:23:11,973 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
08:23:18,790 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
08:23:28,819 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
paxos_test.py::TestPaxos::test_contention_multi_iterations SKIPPED       [ 75%]
paxos_test.py::TestPaxos::test_contention_many_threads 
-------------------------------- live log call ---------------------------------
08:23:49,937 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:23:50,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:23:50,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:23:50,90 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:23:50,90 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:23:50,183 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:23:50,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:23:50,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:23:50,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:23:50,335 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:23:50,426 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:23:50,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:23:50,512 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:23:50,578 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:23:50,578 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:24:09,471 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but load-balancing policies are not specified in some ExecutionProfiles. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.1'], EPs without explicit LBPs = ('EXEC_PROFILE_DEFAULT',))
08:24:09,485 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.1:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
08:24:09,489 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.1:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
PASSED                                                                   [100%]
===Flaky Test Report===

test_replica_availability passed 1 out of the required 1 times. Success!
test_cluster_availability passed 1 out of the required 1 times. Success!
test_contention_many_threads passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 3 passed, 1 skipped in 173.76 seconds =====================
[msx] rc = 0
