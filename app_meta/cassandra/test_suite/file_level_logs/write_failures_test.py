cassandra write_failures_test.py true true
the_test is write_failures_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 13 items

write_failures_test.py::TestWriteFailures::test_mutation_v2 SKIPPED      [  7%]
write_failures_test.py::TestWriteFailures::test_mutation_v3 
-------------------------------- live log call ---------------------------------
03:48:53,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:48:53,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:48:53,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:48:53,873 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:48:53,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:48:54,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:48:54,114 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:48:54,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:48:54,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:49:36,129 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 15%]
write_failures_test.py::TestWriteFailures::test_mutation_v4 
-------------------------------- live log call ---------------------------------
03:49:59,48 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:59,136 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:49:59,205 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:49:59,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:59,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:49:59,449 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:49:59,542 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:49:59,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:49:59,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 23%]
write_failures_test.py::TestWriteFailures::test_mutation_v5 
-------------------------------- live log call ---------------------------------
03:51:04,973 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:51:05,58 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:51:05,125 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:51:05,217 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:51:05,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:51:05,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:51:05,462 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:51:05,546 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:51:05,613 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:51:47,65 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 30%]
write_failures_test.py::TestWriteFailures::test_mutation_any 
-------------------------------- live log call ---------------------------------
03:52:09,892 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:09,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:52:10,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:52:10,136 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:10,221 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:52:10,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:52:10,378 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:52:10,462 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:52:10,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:52:29,889 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:52:30,895 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:52:32,900 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:52:37,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:52:44,837 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 38%]
write_failures_test.py::TestWriteFailures::test_mutation_one 
-------------------------------- live log call ---------------------------------
03:53:35,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:53:35,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:53:35,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:53:35,919 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:53:36,36 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:53:36,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:53:36,194 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:53:36,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:53:36,347 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:53:55,899 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:53:57,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:53:58,885 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:54:03,3 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:54:10,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 46%]
write_failures_test.py::TestWriteFailures::test_mutation_quorum 
-------------------------------- live log call ---------------------------------
03:55:01,694 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:55:01,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:55:01,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:55:01,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:55:02,25 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:55:02,94 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:55:02,187 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:55:02,271 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:55:02,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:55:21,755 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 53%]
write_failures_test.py::TestWriteFailures::test_batch 
-------------------------------- live log call ---------------------------------
03:55:44,531 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:55:44,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:55:44,684 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:55:44,779 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:55:44,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:55:44,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:55:45,23 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:55:45,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:55:45,175 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:56:27,897 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 61%]
write_failures_test.py::TestWriteFailures::test_counter 
-------------------------------- live log call ---------------------------------
03:56:50,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:51,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:56:51,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:56:51,202 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:51,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:56:51,353 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:56:51,445 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:56:51,530 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:56:51,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 69%]
write_failures_test.py::TestWriteFailures::test_paxos 
-------------------------------- live log call ---------------------------------
03:57:56,390 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:56,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:57:56,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:57:56,636 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:56,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:57:56,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:57:56,879 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:57:56,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:57:57,55 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 76%]
write_failures_test.py::TestWriteFailures::test_paxos_any 
-------------------------------- live log call ---------------------------------
03:59:01,576 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:59:01,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:59:01,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:59:01,821 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:59:01,905 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:59:01,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:59:02,64 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:59:02,149 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:59:02,216 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
03:59:43,730 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 84%]
write_failures_test.py::TestWriteFailures::test_thrift SKIPPED           [ 92%]
write_failures_test.py::TestMultiDCWriteFailures::test_oversized_mutation 
-------------------------------- live log call ---------------------------------
04:00:06,813 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:06,899 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:00:06,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:00:07,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:07,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:00:07,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:00:07,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:07,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:00:07,456 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:00:07,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:07,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:00:07,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:00:07,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:07,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:00:07,923 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:08,7 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:00:08,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:08,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:00:08,191 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:00:08,276 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [100%]
===Flaky Test Report===

test_mutation_v3 passed 1 out of the required 1 times. Success!
test_mutation_v4 passed 1 out of the required 1 times. Success!
test_mutation_v5 passed 1 out of the required 1 times. Success!
test_mutation_any passed 1 out of the required 1 times. Success!
test_mutation_one passed 1 out of the required 1 times. Success!
test_mutation_quorum passed 1 out of the required 1 times. Success!
test_batch passed 1 out of the required 1 times. Success!
test_counter passed 1 out of the required 1 times. Success!
test_paxos passed 1 out of the required 1 times. Success!
test_paxos_any passed 1 out of the required 1 times. Success!
test_oversized_mutation passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 11 passed, 2 skipped in 701.03 seconds ====================
[msx] rc = 0
