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
13:37:30,927 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:37:31,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:37:31,12 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:37:31,80 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:37:31,81 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:37:31,172 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:37:31,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:37:31,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:37:31,323 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:37:31,323 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:37:31,414 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:37:31,498 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:37:31,498 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:37:31,565 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:37:31,565 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:38:12,231 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 15%]
write_failures_test.py::TestWriteFailures::test_mutation_v4 
-------------------------------- live log call ---------------------------------
13:38:35,93 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:38:35,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:38:35,183 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:38:35,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:38:35,251 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:38:35,342 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:38:35,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:38:35,427 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:38:35,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:38:35,493 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:38:35,584 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:38:35,669 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:38:35,670 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:38:35,735 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:38:35,736 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 23%]
write_failures_test.py::TestWriteFailures::test_mutation_v5 
-------------------------------- live log call ---------------------------------
13:39:39,773 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:39:39,857 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:39:39,858 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:39:39,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:39:39,925 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:39:40,18 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:39:40,102 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:39:40,102 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:39:40,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:39:40,169 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:39:40,261 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:39:40,345 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:39:40,345 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:39:40,411 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:39:40,411 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 30%]
write_failures_test.py::TestWriteFailures::test_mutation_any 
-------------------------------- live log call ---------------------------------
13:40:44,694 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:40:44,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:40:44,779 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:40:44,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:40:44,846 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:40:44,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:40:45,22 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:40:45,22 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:40:45,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:40:45,89 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:40:45,180 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:40:45,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:40:45,265 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:40:45,331 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:40:45,331 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:41:05,691 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:41:06,698 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:41:09,4 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:41:13,420 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:41:22,43 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 38%]
write_failures_test.py::TestWriteFailures::test_mutation_one 
-------------------------------- live log call ---------------------------------
13:42:09,720 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:42:09,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:42:09,839 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:42:09,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:42:09,906 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:42:09,999 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:42:10,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:42:10,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:42:10,149 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:42:10,149 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:42:10,240 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:42:10,327 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:42:10,328 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:42:10,394 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:42:10,394 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:42:30,714 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
13:42:31,720 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:42:33,825 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:42:38,45 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
13:42:46,868 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 46%]
write_failures_test.py::TestWriteFailures::test_mutation_quorum 
-------------------------------- live log call ---------------------------------
13:43:34,717 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:43:34,804 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:43:34,804 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:43:34,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:43:34,873 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:43:34,966 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:43:35,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:43:35,53 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:43:35,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:43:35,120 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:43:35,212 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:43:35,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:43:35,296 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:43:35,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:43:35,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
write_failures_test.py::TestWriteFailures::test_batch 
-------------------------------- live log call ---------------------------------
13:44:17,291 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:44:17,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:44:17,377 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:44:17,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:44:17,444 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:44:17,539 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:44:17,625 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:44:17,625 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:44:17,691 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:44:17,692 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:44:17,783 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:44:17,867 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:44:17,867 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:44:17,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:44:17,935 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 61%]
write_failures_test.py::TestWriteFailures::test_counter 
-------------------------------- live log call ---------------------------------
13:45:21,960 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:45:22,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:45:22,48 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:45:22,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:45:22,115 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:45:22,209 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:45:22,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:45:22,295 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:45:22,362 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:45:22,362 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:45:22,454 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:45:22,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:45:22,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:45:22,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:45:22,604 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:46:05,430 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
PASSED                                                                   [ 69%]
write_failures_test.py::TestWriteFailures::test_paxos 
-------------------------------- live log call ---------------------------------
13:46:28,140 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:46:28,226 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:46:28,226 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:46:28,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:46:28,293 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:46:28,386 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:46:28,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:46:28,470 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:46:28,536 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:46:28,536 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:46:28,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:46:28,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:46:28,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:46:28,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:46:28,780 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 76%]
write_failures_test.py::TestWriteFailures::test_paxos_any 
-------------------------------- live log call ---------------------------------
13:47:32,567 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:47:32,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:47:32,653 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:47:32,721 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:47:32,721 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:47:32,814 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:47:32,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:47:32,900 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:47:32,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:47:32,967 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:47:33,61 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:47:33,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:47:33,146 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:47:33,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:47:33,213 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 84%]
write_failures_test.py::TestWriteFailures::test_thrift SKIPPED           [ 92%]
write_failures_test.py::TestMultiDCWriteFailures::test_oversized_mutation 
-------------------------------- live log call ---------------------------------
13:48:38,552 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:38,637 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:48:38,637 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:38,704 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:48:38,704 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:38,796 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:38,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:48:38,881 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:38,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:48:38,947 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:39,127 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:48:39,128 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,228 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:48:39,228 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,321 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:39,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
13:48:39,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,472 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
13:48:39,472 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,527 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:39,611 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
13:48:39,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,661 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:39,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
13:48:39,745 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,795 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:39,878 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
13:48:39,878 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
13:48:39,928 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
13:48:40,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
13:48:40,12 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
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

==================== 11 passed, 2 skipped in 693.18 seconds ====================
[msx] rc = 0
