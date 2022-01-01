cassandra auth_join_ring_false_test.py true true
the_test is auth_join_ring_false_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 4 items

auth_join_ring_false_test.py::TestAuth::test_login_existing_node 
-------------------------------- live log call ---------------------------------
01:24:40,982 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:24:41,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:24:41,66 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:24:41,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:24:41,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:24:41,223 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:24:41,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:24:41,307 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:24:41,373 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:24:41,373 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:24:41,462 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:24:41,546 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:24:41,546 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:24:41,611 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:24:41,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:25:21,365 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:21,367 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:21,738 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:21,739 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:22,109 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:22,111 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:22,478 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:22,479 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:22,847 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:22,849 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:23,218 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:23,220 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:23,588 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:23,589 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:23,954 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:23,955 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:24,322 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:24,323 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:24,688 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:24,689 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:25,56 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:25,57 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:25,425 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:25,426 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:25,789 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:25,790 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:26,156 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:26,158 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:26,523 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:26,524 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:26,888 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:26,890 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:27,253 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:27,255 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:27,619 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:27,620 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:27,998 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:28,0 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:28,363 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:28,364 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:28,733 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:28,734 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:29,98 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:29,100 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:29,466 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:29,467 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:29,836 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:29,838 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:30,201 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:30,202 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:30,565 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:30,565 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:30,927 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:30,927 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:31,290 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:31,291 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:31,651 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:31,652 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:32,21 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:32,22 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:32,387 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:32,389 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:32,772 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:32,773 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:33,138 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:33,139 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:33,505 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:33,506 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:33,872 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:33,873 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:34,240 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:34,241 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:34,631 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:34,632 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:34,996 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:34,997 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:35,360 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:35,362 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:35,726 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:35,727 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:36,90 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:36,92 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:36,456 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:36,458 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:36,824 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:36,826 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:37,188 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:37,189 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:37,550 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:37,552 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:37,914 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:37,915 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:38,278 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:38,279 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:38,646 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:38,647 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:39,9 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:39,11 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:39,371 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:39,372 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:39,733 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:39,734 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:40,95 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:40,96 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:40,459 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:40,460 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:40,829 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:40,830 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:41,194 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:41,195 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:41,557 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:41,558 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:41,920 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:41,922 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:42,299 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:42,301 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:42,662 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:42,663 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:43,30 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:43,32 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:43,395 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:43,396 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:43,752 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:43,753 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:44,116 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:44,118 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:44,483 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:44,484 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:44,846 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:44,847 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:45,213 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:45,214 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:45,575 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:45,576 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:45,939 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:45,940 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:46,302 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:46,304 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:46,667 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:46,669 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:47,28 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:47,29 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:47,396 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:47,397 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:47,756 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:47,757 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:48,116 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:48,117 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:48,478 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:48,479 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:48,841 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:48,842 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:49,204 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:49,205 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:49,567 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:49,568 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:49,929 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:49,930 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:50,295 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:50,296 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:50,656 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:50,657 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:51,17 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:51,18 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:51,379 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:25:51,380 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:25:51,398 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:51,400 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:51,662 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:51,663 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:51,925 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:51,927 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:52,187 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:52,195 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:52,463 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:52,464 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:52,725 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:52,727 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:52,988 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:52,989 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:53,250 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:53,251 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:53,512 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:53,513 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:53,775 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:53,777 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:54,38 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:54,39 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:54,300 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:54,301 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:54,562 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:54,563 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:54,824 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:54,826 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:55,86 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:55,88 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:55,349 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:55,351 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:55,611 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:55,613 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:55,873 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:55,875 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:56,136 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:56,138 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:56,399 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:56,400 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:56,660 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:56,662 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:56,923 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:56,924 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:57,184 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:57,186 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:57,446 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:57,447 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:57,709 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:57,710 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:57,971 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:57,972 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:58,233 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:58,234 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:58,495 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:58,497 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:58,758 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:58,759 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:59,20 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:59,21 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:59,282 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:59,283 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:59,545 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:59,550 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:25:59,811 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:25:59,812 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:00,73 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:00,74 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:00,334 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:00,336 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:00,596 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:00,598 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:00,860 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:00,862 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:01,123 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:01,124 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:01,384 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:01,386 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:01,646 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:01,647 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:01,908 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:01,910 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:02,171 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:02,172 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:02,434 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:02,435 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:02,696 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:02,698 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:02,958 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:02,960 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:03,220 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:03,221 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:03,481 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:03,482 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:03,742 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:03,744 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:04,5 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:04,6 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:04,266 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:04,267 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:04,527 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:04,529 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:04,789 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:04,790 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:05,50 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:05,52 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:05,312 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:05,313 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:05,573 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:05,575 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:05,834 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:05,835 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:06,95 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:06,97 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:06,357 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:06,358 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:06,618 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:06,620 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:06,881 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:06,882 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:07,143 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:07,145 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:07,405 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:07,406 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:07,666 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:07,668 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:07,928 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:07,930 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:08,190 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:08,192 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:08,452 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:08,453 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:08,714 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:08,715 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:08,975 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:08,976 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:09,237 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:09,238 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:09,499 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:09,500 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:09,760 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:09,762 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:10,26 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:10,27 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:10,287 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:10,288 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:10,547 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:10,549 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:10,809 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:10,810 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:11,69 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:11,71 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:11,331 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:11,332 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:11,592 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:11,594 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:11,855 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:11,857 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:12,117 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:12,118 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:12,378 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:12,379 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:12,640 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:12,641 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:12,901 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:12,902 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:13,162 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:13,163 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:13,423 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:13,425 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:13,684 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:13,686 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:13,947 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:13,948 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:14,207 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:14,209 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:14,469 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:14,470 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:14,730 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:14,731 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:14,990 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:14,991 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:15,251 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:15,252 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:15,511 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:15,513 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:15,772 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:15,773 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:16,34 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:16,35 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:16,295 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:16,296 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:16,556 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:16,557 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:16,817 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:16,818 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:17,79 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:17,80 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:17,340 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:17,342 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:17,601 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:17,603 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:17,862 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:17,864 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:18,123 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:18,124 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:18,385 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:18,386 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:18,646 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:18,648 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:18,908 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:18,909 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:19,170 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:19,171 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:19,432 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:19,433 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:19,694 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:19,695 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:19,955 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:19,956 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:20,219 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:20,220 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:20,480 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:20,482 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:20,742 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:20,743 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:21,3 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:21,5 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:21,265 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:21,266 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:26:21,526 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:26:21,527 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
PASSED                                                                   [ 25%]
auth_join_ring_false_test.py::TestAuth::test_login_new_node 
-------------------------------- live log call ---------------------------------
01:26:22,12 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:26:22,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:26:22,98 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:26:22,165 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:26:22,165 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:26:22,256 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:26:22,341 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:26:22,341 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:26:22,409 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:26:22,409 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:26:38,632 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:26:38,724 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:26:38,724 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:26:38,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:26:38,799 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:26:54,477 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:54,479 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:54,846 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:54,847 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:55,213 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:55,215 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:55,582 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:55,583 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:55,947 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:55,949 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:56,322 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:56,324 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:56,689 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:56,690 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:57,56 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:57,57 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:57,422 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:57,423 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:57,790 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:57,791 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:58,154 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:58,156 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:58,530 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:58,531 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:58,899 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:58,900 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:59,270 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:59,271 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:26:59,636 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:26:59,637 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:00,0 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:00,2 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:00,363 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:00,364 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:00,733 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:00,735 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:01,97 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:01,98 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:01,460 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:01,461 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:01,822 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:01,823 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:02,188 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:02,189 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:02,550 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:02,552 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:02,945 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:02,946 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:03,375 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:03,376 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:03,740 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:03,741 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:04,105 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:04,107 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:04,468 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:04,469 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:04,832 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:04,834 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:05,223 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:05,225 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:05,586 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:05,587 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:05,950 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:05,951 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:06,320 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:06,321 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:06,683 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:06,684 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:07,47 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:07,49 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:07,419 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:07,420 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:07,781 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:07,782 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:08,142 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:08,143 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:08,506 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:08,507 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:08,866 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:08,867 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:09,234 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:09,235 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:09,602 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:09,603 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:09,965 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:09,966 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:10,327 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:10,328 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:10,691 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:10,692 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:11,51 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:11,53 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:11,414 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:11,415 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:11,786 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:11,788 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:12,156 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:12,157 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:12,522 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:12,523 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:12,892 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:12,893 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:13,261 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:13,262 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:13,627 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:13,628 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:14,0 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:14,2 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:14,363 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:14,365 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:14,724 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:14,725 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:15,93 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:15,94 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:15,458 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:15,459 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:15,821 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:15,822 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:16,191 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:16,193 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:16,556 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:16,557 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:16,918 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:16,919 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:17,282 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:17,283 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:17,647 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:17,649 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:18,13 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:18,15 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:18,383 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:18,384 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:18,747 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:18,748 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:19,110 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:19,111 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:19,479 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:19,480 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:19,842 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:19,843 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:20,207 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:20,208 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:20,580 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:20,581 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:20,945 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:20,947 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:21,306 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:21,307 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:21,666 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:21,668 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:22,29 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:22,30 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:22,391 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:22,392 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:22,763 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:22,765 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:23,126 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:23,127 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:23,489 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:23,491 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:23,851 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:23,852 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:24,211 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:24,213 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:24,574 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
01:27:24,575 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
01:27:24,596 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:24,597 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:24,858 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:24,860 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:25,122 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:25,124 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:25,386 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:25,387 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:25,649 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:25,651 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:25,912 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:25,914 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:26,176 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:26,178 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:26,439 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:26,440 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:26,701 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:26,703 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:26,963 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:26,965 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:27,226 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:27,228 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:27,488 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:27,490 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:27,750 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:27,752 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:28,13 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:28,14 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:28,275 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:28,277 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:28,538 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:28,540 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:28,800 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:28,802 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:29,64 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:29,65 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:29,327 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:29,328 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:29,589 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:29,591 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:29,855 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:29,857 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:30,118 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:30,119 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:30,380 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:30,382 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:30,643 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:30,644 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:30,906 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:30,907 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:31,168 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:31,169 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:31,430 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:31,431 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:31,693 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:31,694 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:31,956 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:31,957 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:32,218 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:32,219 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:32,480 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:32,482 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:32,742 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:32,743 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:33,4 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:33,5 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:33,265 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:33,267 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:33,527 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:33,528 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:33,790 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:33,791 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:34,53 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:34,54 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:34,315 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:34,316 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:34,576 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:34,578 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:34,839 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:34,840 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:35,101 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:35,102 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:35,362 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:35,364 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:35,624 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:35,625 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:35,887 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:35,888 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:36,148 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:36,149 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:36,410 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:36,411 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:36,673 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:36,674 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:36,934 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:36,935 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:37,195 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:37,197 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:37,457 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:37,458 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:37,718 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:37,720 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:37,980 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:37,981 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:38,242 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:38,243 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:38,503 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:38,504 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:38,764 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:38,765 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:39,25 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:39,27 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:39,287 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:39,289 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:39,548 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:39,550 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:39,810 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:39,811 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:40,72 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:40,76 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:40,339 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:40,340 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:40,600 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:40,602 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:40,862 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:40,863 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:41,124 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:41,126 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:41,386 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:41,388 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:41,648 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:41,649 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:41,909 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:41,911 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:42,172 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:42,173 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:42,434 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:42,435 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:42,695 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:42,697 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:42,956 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:42,958 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:43,217 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:43,218 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:43,478 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:43,479 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:43,738 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:43,739 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:43,999 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:44,0 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:44,260 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:44,261 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:44,521 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:44,522 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:44,782 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:44,783 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:45,43 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:45,44 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:45,305 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:45,306 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:45,566 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:45,567 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:45,826 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:45,827 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:46,88 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:46,89 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:46,348 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:46,350 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:46,609 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:46,610 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:46,870 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:46,871 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:47,131 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:47,132 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:47,393 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:47,394 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:47,654 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:47,655 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:47,914 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:47,916 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:48,175 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:48,176 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:48,435 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:48,437 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:48,696 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:48,697 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:48,957 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:48,958 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:49,221 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:49,222 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:49,483 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:49,484 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:49,744 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:49,745 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:50,24 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:50,25 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:50,287 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:50,288 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:50,550 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:50,552 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:50,811 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:50,813 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:51,72 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:51,73 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:51,333 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:51,334 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:51,594 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:51,595 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:51,854 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:51,855 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:52,114 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:52,116 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:52,376 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:52,377 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:52,638 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:52,639 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:52,899 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:52,900 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:53,160 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:53,162 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:53,421 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:53,423 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:53,682 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:53,684 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:53,944 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:53,945 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:54,205 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:54,206 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:54,466 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:54,467 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
01:27:54,726 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
01:27:54,727 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
PASSED                                                                   [ 50%]
auth_join_ring_false_test.py::TestAuth::test_list_users 
-------------------------------- live log call ---------------------------------
01:27:55,239 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:27:55,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:27:55,325 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:27:55,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:27:55,392 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:28:11,925 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:28:12,21 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:28:12,21 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:28:12,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:28:12,98 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
auth_join_ring_false_test.py::TestAuth::test_modify_and_select_auth 
-------------------------------- live log call ---------------------------------
01:28:28,663 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:28:28,749 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:28:28,749 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:28:28,816 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:28:28,816 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:28:45,79 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks is higher than the number of nodes 1
01:28:45,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:28:45,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:28:45,417 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:28:45,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:28:45,493 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:29:30,918 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
PASSED                                                                   [100%]
===Flaky Test Report===

test_login_existing_node passed 1 out of the required 1 times. Success!
test_login_new_node passed 1 out of the required 1 times. Success!
test_list_users passed 1 out of the required 1 times. Success!
test_modify_and_select_auth passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 4 passed in 299.43 seconds ==========================
[msx] rc = 0
