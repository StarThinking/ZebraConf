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
01:55:04,317 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:04,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:04,471 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:04,562 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:04,646 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:55:04,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:55:51,912 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:55:51,913 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
01:55:51,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:55:52,920 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:55:53,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:55:55,326 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:55:55,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:55:56,348 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:55:57,451 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:55:58,552 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:55:59,672 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:00,759 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:01,962 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:03,65 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:04,268 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:05,371 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:06,474 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:56:07,577 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:57:17,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:57:18,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:57:18,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 78%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_remove_index_file 
-------------------------------- live log call ---------------------------------
01:57:29,663 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:57:29,749 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:57:29,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 85%]
sstable_generation_loading_test.py::TestSSTableGenerationAndLoading::test_sstableloader_with_mv 
-------------------------------- live log call ---------------------------------
01:58:08,727 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:58:08,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:58:08,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:58:08,971 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:58:09,56 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:58:09,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:58:55,295 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:58:55,296 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
01:58:55,300 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:58:56,403 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:58:56,605 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:58:57,823 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:58:58,508 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:58:58,924 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:00,27 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:01,129 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:02,237 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:02,419 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
01:59:03,336 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:04,440 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:05,540 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:06,644 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:07,848 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:08,951 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:10,53 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:11,155 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
01:59:11,585 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
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
02:00:21,346 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:00:21,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:00:21,501 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:00:58,80 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
02:00:58,83 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:00:59,89 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
02:01:00,894 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [100%]
===Flaky Test Report===

test_sstableloader_uppercase_keyspace_name passed 1 out of the required 1 times. Success!
test_incompressible_data_in_compressed_table passed 1 out of the required 1 times. Success!
test_remove_index_file passed 1 out of the required 1 times. Success!
test_sstableloader_with_mv passed 1 out of the required 1 times. Success!
test_sstableloader_with_failing_2i passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

==================== 5 passed, 9 skipped in 361.56 seconds =====================
[msx] rc = 0
