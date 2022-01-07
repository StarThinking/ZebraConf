cassandra ttl_test.py true true
the_test is ttl_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 25 items

ttl_test.py::TestTTL::test_default_ttl 
-------------------------------- live log setup --------------------------------
03:22:57,843 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:22:57,930 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:22:57,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:23:07,318 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  4%]
ttl_test.py::TestTTL::test_insert_ttl_has_priority_on_defaut_ttl 
-------------------------------- live log setup --------------------------------
03:23:07,813 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:23:07,899 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:07,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:23:16,301 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:23:21,284 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  8%]
ttl_test.py::TestTTL::test_insert_ttl_works_without_default_ttl 
-------------------------------- live log setup --------------------------------
03:23:21,536 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:23:21,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:21,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:23:31,12 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 12%]
ttl_test.py::TestTTL::test_default_ttl_can_be_removed 
-------------------------------- live log setup --------------------------------
03:23:31,497 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:23:31,583 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:31,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:23:39,483 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 16%]
ttl_test.py::TestTTL::test_removing_default_ttl_does_not_affect_existing_rows 
-------------------------------- live log setup --------------------------------
03:23:39,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:23:40,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:23:40,110 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:23:51,565 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:23:58,545 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:24:06,541 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 20%]
ttl_test.py::TestTTL::test_update_single_column_ttl 
-------------------------------- live log setup --------------------------------
03:24:06,959 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:07,46 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:07,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 24%]
ttl_test.py::TestTTL::test_update_multiple_columns_ttl 
-------------------------------- live log setup --------------------------------
03:24:18,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:19,25 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:19,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 28%]
ttl_test.py::TestTTL::test_update_column_ttl_with_default_ttl 
-------------------------------- live log setup --------------------------------
03:24:29,904 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:29,996 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:30,65 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:24:46,409 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 32%]
ttl_test.py::TestTTL::test_remove_column_ttl 
-------------------------------- live log setup --------------------------------
03:24:46,897 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:46,986 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:47,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 36%]
ttl_test.py::TestTTL::test_set_ttl_to_zero_to_default_ttl 
-------------------------------- live log setup --------------------------------
03:24:57,849 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:24:57,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:24:58,5 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
ttl_test.py::TestTTL::test_remove_column_ttl_with_default_ttl SKIPPED    [ 44%]
ttl_test.py::TestTTL::test_collection_list_ttl 
-------------------------------- live log setup --------------------------------
03:25:09,885 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:25:09,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:25:10,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:25:28,543 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 48%]
ttl_test.py::TestTTL::test_collection_set_ttl 
-------------------------------- live log setup --------------------------------
03:25:28,889 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:25:28,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:25:29,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:25:47,442 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 52%]
ttl_test.py::TestTTL::test_collection_map_ttl 
-------------------------------- live log setup --------------------------------
03:25:47,876 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:25:47,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:25:48,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:26:02,516 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 56%]
ttl_test.py::TestTTL::test_delete_with_ttl_expired 
-------------------------------- live log setup --------------------------------
03:26:02,856 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:26:02,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:26:03,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:26:11,414 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 60%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_cap 
-------------------------------- live log setup --------------------------------
03:26:11,819 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:26:11,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:26:11,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:26:19,765 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:26:20,774 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:22,679 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:26,697 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:31,919 cassandra.protocol WARNING Server warning: Request on table ks.ttl_table with ttl of 630720000 seconds exceeds maximum supported expiration date of 2038-01-19T03:14:06+00:00 and will have its expiration capped to that date. In order to avoid this use a lower TTL or upgrade to a version where this limitation is fixed. See CASSANDRA-14092 for more details.
03:26:33,960 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 64%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_cap_default_ttl 
-------------------------------- live log setup --------------------------------
03:26:34,333 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:26:34,420 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:26:34,487 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:26:42,502 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:26:43,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:45,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:49,327 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:26:54,465 cassandra.protocol WARNING Server warning: Request on table ks.ttl_table with default ttl of 630720000 seconds exceeds maximum supported expiration date of 2038-01-19T03:14:06+00:00 and will have its expiration capped to that date. In order to avoid this use a lower TTL or upgrade to a version where this limitation is fixed. See CASSANDRA-14092 for more details.
03:26:56,474 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 68%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_capnowarn 
-------------------------------- live log setup --------------------------------
03:26:56,857 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:26:56,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:26:57,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:27:04,43 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:27:05,250 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:07,556 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:11,271 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:19,143 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 72%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_capnowarn_default_ttl 
-------------------------------- live log setup --------------------------------
03:27:19,622 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:27:19,710 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:27:19,777 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:27:26,470 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:27:27,576 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:29,681 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:33,899 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:41,860 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 76%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_reject 
-------------------------------- live log setup --------------------------------
03:27:42,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:27:42,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:27:42,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:27:49,54 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:27:50,60 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:52,266 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:27:55,976 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:04,507 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 80%]
ttl_test.py::TestTTL::test_expiration_overflow_policy_reject_default_ttl 
-------------------------------- live log setup --------------------------------
03:28:04,891 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:04,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:05,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
03:28:12,442 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:28:13,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:15,655 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:19,268 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:28:27,20 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 84%]
ttl_test.py::TestDistributedTTL::test_ttl_is_replicated 
-------------------------------- live log setup --------------------------------
03:28:27,405 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:27,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:27,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:27,668 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:27,754 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:28:27,823 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 88%]
ttl_test.py::TestDistributedTTL::test_ttl_is_respected_on_delayed_replication 
-------------------------------- live log setup --------------------------------
03:28:53,524 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:53,612 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:53,679 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:28:53,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:28:53,859 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:28:53,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
-------------------------------- live log call ---------------------------------
03:29:11,901 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
03:29:13,27 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:29:14,834 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:29:18,546 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:29:25,766 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:29:40,639 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:29:40,640 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:29:41,715 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:29:42,817 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:29:43,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:29:47,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:29:55,551 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:30:13,798 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:30:16,103 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
03:30:26,605 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
03:30:40,684 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 92%]
ttl_test.py::TestDistributedTTL::test_ttl_is_respected_on_repair 
-------------------------------- live log setup --------------------------------
03:30:41,168 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:30:41,255 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:30:41,323 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:30:41,417 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:30:41,503 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
03:30:41,571 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
-------------------------------- live log call ---------------------------------
03:31:26,440 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
03:31:27,287 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:31:29,866 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:31:29,868 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
03:31:30,874 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:31:32,881 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
03:31:36,991 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 96%]
ttl_test.py::TestRecoverNegativeExpirationDate::test_recover_negative_expiration_date_sstables_with_scrub 
-------------------------------- live log call ---------------------------------
03:31:37,566 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:31:37,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:31:37,721 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:31:45,701 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [100%]
===Flaky Test Report===

test_default_ttl passed 1 out of the required 1 times. Success!
test_insert_ttl_has_priority_on_defaut_ttl passed 1 out of the required 1 times. Success!
test_insert_ttl_works_without_default_ttl passed 1 out of the required 1 times. Success!
test_default_ttl_can_be_removed passed 1 out of the required 1 times. Success!
test_removing_default_ttl_does_not_affect_existing_rows passed 1 out of the required 1 times. Success!
test_update_single_column_ttl passed 1 out of the required 1 times. Success!
test_update_multiple_columns_ttl passed 1 out of the required 1 times. Success!
test_update_column_ttl_with_default_ttl passed 1 out of the required 1 times. Success!
test_remove_column_ttl passed 1 out of the required 1 times. Success!
test_set_ttl_to_zero_to_default_ttl passed 1 out of the required 1 times. Success!
test_collection_list_ttl passed 1 out of the required 1 times. Success!
test_collection_set_ttl passed 1 out of the required 1 times. Success!
test_collection_map_ttl passed 1 out of the required 1 times. Success!
test_delete_with_ttl_expired passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_cap passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_cap_default_ttl passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_capnowarn passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_capnowarn_default_ttl passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_reject passed 1 out of the required 1 times. Success!
test_expiration_overflow_policy_reject_default_ttl passed 1 out of the required 1 times. Success!
test_ttl_is_replicated passed 1 out of the required 1 times. Success!
test_ttl_is_respected_on_delayed_replication passed 1 out of the required 1 times. Success!
test_ttl_is_respected_on_repair passed 1 out of the required 1 times. Success!
test_recover_negative_expiration_date_sstables_with_scrub passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 24 passed, 1 skipped in 545.07 seconds ====================
[msx] rc = 0
