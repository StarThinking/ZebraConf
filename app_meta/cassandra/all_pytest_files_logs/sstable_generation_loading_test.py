cassandra sstable_generation_loading_test.py true true
the_test is sstable_generation_loading_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 14 items

sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_none_to_none SKIPPED [  7%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_none_to_snappy SKIPPED [ 14%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_none_to_deflate SKIPPED [ 21%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_snappy_to_none SKIPPED [ 28%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_snappy_to_snappy SKIPPED [ 35%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_snappy_to_deflate SKIPPED [ 42%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_deflate_to_none SKIPPED [ 50%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_deflate_to_snappy SKIPPED [ 57%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_compression_deflate_to_deflate SKIPPED [ 64%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_uppercase_keyspace_name 
-------------------------------- live log call ---------------------------------
11:45:38,483 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:45:38,569 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:45:38,569 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:45:38,638 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:45:38,638 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:45:38,731 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:45:38,816 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:45:38,816 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:45:38,883 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:45:38,883 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:46:24,713 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:46:24,713 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
11:46:24,716 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:46:25,719 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:46:25,719 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:46:27,729 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:28,846 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:29,865 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:30,968 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:32,171 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:33,374 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:34,480 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:35,585 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:36,684 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:37,787 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:38,990 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:40,94 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:46:41,196 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
PASSED                                                                   [ 71%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_incompressible_data_in_compressed_table 
-------------------------------- live log call ---------------------------------
11:47:51,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:47:51,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:47:51,183 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:47:51,250 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:47:51,250 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 78%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_remove_index_file 
-------------------------------- live log call ---------------------------------
11:48:02,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:48:02,410 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:48:02,410 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:48:02,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:48:02,477 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 85%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_with_mv 
-------------------------------- live log call ---------------------------------
11:48:40,617 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:48:40,706 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:48:40,706 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:48:40,773 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:48:40,773 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:48:40,864 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:48:40,950 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:48:40,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:48:41,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:48:41,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:49:26,867 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:49:26,868 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
11:49:26,872 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:49:27,876 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:49:27,985 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:29,193 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:30,80 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:49:30,295 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:31,397 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:32,500 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:33,603 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:34,694 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
11:49:34,727 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:35,810 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:36,913 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:38,15 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:39,118 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:40,221 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
11:49:41,425 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'Keyspace1' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'Keyspace1\' does not exist"',)
PASSED                                                                   [ 92%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_with_failing_2i 
-------------------------------- live log call ---------------------------------
11:50:50,733 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:50:50,820 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:50:50,820 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:50:50,889 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:50:50,889 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:51:27,756 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
11:51:27,758 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
11:51:28,764 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_sstableloader_uppercase_keyspace_name passed 1 out of the required 1 times. Success!
test_incompressible_data_in_compressed_table passed 1 out of the required 1 times. Success!
test_remove_index_file passed 1 out of the required 1 times. Success!
test_sstableloader_with_mv passed 1 out of the required 1 times. Success!
test_sstableloader_with_failing_2i passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 5 passed, 9 skipped in 356.55 seconds =====================
[msx] rc = 0
