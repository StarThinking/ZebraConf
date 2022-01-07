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
15:22:17,653 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:22:17,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:22:17,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:22:17,900 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:22:17,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:22:18,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:22:18,142 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:22:18,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
15:22:18,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
15:22:58,723 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:22:58,725 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:22:59,93 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:22:59,95 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:22:59,466 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:22:59,467 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:22:59,834 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:22:59,835 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:00,197 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:00,199 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:00,565 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:00,566 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:00,928 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:00,929 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:01,293 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:01,294 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:01,655 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:01,656 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:02,17 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:02,18 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:02,378 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:02,380 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:02,741 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:02,742 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:03,103 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:03,104 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:03,465 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:03,466 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:03,829 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:03,831 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:04,191 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:04,193 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:04,552 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:04,553 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:04,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:04,919 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:05,279 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:05,280 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:05,649 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:05,651 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:06,11 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:06,12 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:06,373 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:06,374 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:06,737 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:06,738 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:07,99 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:07,100 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:07,461 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:07,463 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:07,823 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:07,824 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:08,184 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:08,185 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:08,547 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:08,548 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:08,909 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:08,910 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:09,275 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:09,277 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:09,640 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:09,641 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:10,2 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:10,3 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:10,366 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:10,367 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:10,730 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:10,732 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:11,93 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:11,95 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:11,457 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:11,459 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:11,820 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:11,821 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:12,182 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:12,183 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:12,543 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:12,545 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:12,906 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:12,907 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:13,267 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:13,269 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:13,631 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:13,632 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:13,993 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:13,994 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:14,354 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:14,356 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:14,727 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:14,729 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:15,89 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:15,90 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:15,452 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:15,454 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:15,814 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:15,816 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:16,175 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:16,177 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:16,540 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:16,541 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:16,901 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:16,902 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:17,263 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:17,264 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:17,625 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:17,627 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:17,991 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:17,992 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:18,360 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:18,361 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:18,725 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:18,727 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:19,90 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:19,91 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:19,454 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:19,456 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:19,817 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:19,818 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:20,189 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:20,190 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:20,553 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:20,555 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:20,916 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:20,918 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:21,278 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:21,280 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:21,640 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:21,641 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:22,2 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:22,3 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:22,367 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:22,368 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:22,730 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:22,732 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:23,97 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:23,98 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:23,458 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:23,460 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:23,823 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:23,824 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:24,186 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:24,187 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:24,551 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:24,553 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:24,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:24,919 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:25,285 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:25,286 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:25,650 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:25,651 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:26,15 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:26,16 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:26,380 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:26,381 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:26,745 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:26,746 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:27,109 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:27,110 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:27,474 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:27,475 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:27,840 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:27,841 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:28,203 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:28,205 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:28,566 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:28,567 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:28,928 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:23:28,930 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:23:28,951 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:28,952 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:29,215 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:29,216 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:29,490 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:29,494 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:29,757 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:29,758 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:30,20 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:30,21 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:30,282 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:30,283 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:30,544 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:30,545 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:30,805 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:30,807 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:31,67 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:31,68 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:31,328 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:31,329 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:31,590 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:31,591 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:31,851 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:31,853 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:32,112 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:32,114 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:32,374 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:32,375 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:32,641 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:32,642 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:32,903 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:32,904 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:33,165 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:33,167 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:33,428 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:33,429 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:33,690 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:33,691 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:33,952 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:33,953 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:34,214 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:34,215 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:34,477 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:34,478 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:34,739 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:34,740 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:35,0 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:35,1 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:35,262 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:35,263 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:35,524 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:35,525 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:35,786 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:35,787 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:36,47 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:36,49 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:36,309 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:36,310 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:36,571 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:36,572 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:36,832 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:36,833 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:37,93 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:37,94 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:37,354 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:37,356 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:37,617 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:37,618 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:37,879 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:37,880 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:38,141 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:38,143 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:38,403 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:38,404 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:38,665 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:38,666 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:38,926 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:38,928 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:39,188 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:39,189 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:39,451 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:39,453 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:39,714 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:39,716 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:39,978 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:39,979 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:40,240 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:40,241 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:40,502 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:40,503 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:40,763 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:40,764 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:41,24 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:41,25 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:41,285 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:41,287 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:41,547 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:41,548 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:41,808 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:41,810 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:42,69 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:42,71 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:42,330 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:42,332 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:42,591 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:42,592 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:42,852 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:42,853 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:43,116 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:43,117 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:43,377 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:43,378 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:43,638 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:43,639 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:43,899 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:43,900 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:44,160 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:44,162 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:44,422 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:44,423 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:44,683 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:44,684 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:44,944 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:44,945 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:45,205 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:45,206 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:45,466 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:45,468 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:45,728 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:45,729 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:45,989 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:45,990 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:46,249 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:46,250 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:46,510 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:46,512 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:46,772 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:46,773 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:47,33 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:47,34 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:47,293 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:47,295 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:47,554 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:47,555 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:47,814 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:47,816 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:48,75 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:48,76 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:48,335 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:48,337 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:48,596 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:48,597 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:48,856 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:48,857 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:49,117 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:49,118 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:49,378 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:49,379 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:49,639 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:49,640 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:49,900 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:49,901 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:50,161 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:50,162 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:50,421 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:50,422 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:50,682 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:50,683 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:50,943 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:50,944 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:51,204 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:51,206 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:51,465 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:51,467 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:51,726 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:51,727 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:51,987 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:51,988 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:52,247 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:52,248 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:52,507 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:52,509 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:52,768 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:52,769 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:53,28 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:53,29 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:53,293 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:53,294 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:53,554 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:53,555 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:53,815 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:53,816 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:54,76 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:54,77 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:54,336 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:54,338 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:54,597 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:54,599 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:54,858 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:54,860 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:55,120 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:55,121 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:55,381 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:55,382 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:55,642 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:55,643 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:55,903 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:55,904 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:56,163 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:56,165 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:56,425 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:56,426 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:56,686 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:56,687 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:56,947 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:56,948 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:57,207 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:57,209 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:57,469 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:57,470 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:57,729 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:57,731 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:57,989 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:57,991 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:58,250 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:58,251 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:58,511 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:58,512 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:58,772 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:58,773 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:23:59,32 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:23:59,34 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
PASSED                                                                   [ 25%]
auth_join_ring_false_test.py::TestAuth::test_login_new_node 
-------------------------------- live log call ---------------------------------
15:23:59,713 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:23:59,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:23:59,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:23:59,961 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:24:00,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:24:00,115 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:24:16,664 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:24:16,758 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
15:24:16,833 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
15:24:32,626 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:32,628 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:32,992 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:32,994 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:33,359 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:33,361 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:33,725 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:33,726 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:34,92 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:34,94 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:34,468 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:34,469 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:34,833 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:34,834 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:35,206 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:35,206 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:35,572 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:35,572 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:35,938 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:35,939 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:36,301 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:36,301 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:36,671 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:36,672 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:37,38 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:37,38 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:37,404 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:37,405 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:37,774 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:37,774 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:38,141 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:38,141 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:38,528 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:38,530 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:38,902 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:38,902 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:39,270 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:39,271 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:39,629 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:39,631 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:39,991 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:39,992 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:40,355 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:40,356 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:40,715 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:40,716 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:41,89 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:41,90 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:41,453 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:41,454 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:41,814 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:41,815 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:42,179 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:42,180 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:42,547 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:42,548 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:42,914 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:42,915 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:43,286 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:43,287 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:43,653 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:43,654 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:44,21 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:44,23 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:44,391 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:44,392 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:44,754 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:44,755 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:45,116 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:45,117 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:45,485 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:45,487 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:45,846 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:45,848 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:46,209 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:46,210 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:46,572 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:46,573 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:46,935 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:46,936 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:47,296 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:47,298 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:47,674 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:47,675 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:48,41 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:48,42 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:48,404 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:48,406 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:48,826 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:48,827 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:49,188 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:49,189 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:49,550 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:49,551 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:49,913 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:49,914 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:50,274 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:50,275 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:50,637 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:50,638 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:51,0 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:51,2 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:51,364 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:51,365 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:51,724 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:51,725 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:52,90 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:52,91 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:52,452 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:52,453 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:52,834 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:52,835 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:53,201 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:53,202 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:53,570 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:53,571 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:53,936 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:53,937 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:54,309 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:54,310 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:54,675 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:54,676 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:55,42 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:55,44 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:55,408 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:55,409 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:55,776 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:55,777 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:56,142 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:56,143 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:56,515 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:56,516 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:56,883 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:56,884 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:57,249 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:57,250 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:57,614 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:57,616 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:57,979 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:57,980 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:58,345 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:58,347 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:58,716 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:58,717 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:59,79 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:59,81 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:59,448 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:59,449 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:24:59,810 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:24:59,811 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:00,173 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:00,174 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:00,533 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:00,534 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:00,904 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:00,905 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:01,263 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:01,264 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:01,645 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:01,646 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:02,7 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:02,9 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:02,376 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:02,377 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:02,744 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"
15:25:02,746 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username cassandra and/or password are incorrect"',)})
15:25:02,763 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:02,764 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:03,29 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:03,30 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:03,293 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:03,294 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:03,555 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:03,557 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:03,819 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:03,822 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:04,91 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:04,93 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:04,354 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:04,355 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:04,617 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:04,618 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:04,879 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:04,880 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:05,142 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:05,143 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:05,404 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:05,406 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:05,666 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:05,668 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:05,929 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:05,930 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:06,191 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:06,192 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:06,453 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:06,455 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:06,715 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:06,716 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:06,976 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:06,977 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:07,239 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:07,240 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:07,501 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:07,502 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:07,763 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:07,765 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:08,26 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:08,27 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:08,287 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:08,289 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:08,550 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:08,551 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:08,811 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:08,813 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:09,74 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:09,75 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:09,337 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:09,338 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:09,599 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:09,600 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:09,864 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:09,865 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:10,127 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:10,128 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:10,390 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:10,391 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:10,654 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:10,655 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:10,917 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:10,919 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:11,180 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:11,181 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:11,444 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:11,445 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:11,706 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:11,707 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:11,969 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:11,970 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:12,232 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:12,233 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:12,494 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:12,496 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:12,757 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:12,758 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:13,19 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:13,20 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:13,284 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:13,286 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:13,546 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:13,548 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:13,809 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:13,811 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:14,73 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:14,75 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:14,336 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:14,337 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:14,597 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:14,599 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:14,859 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:14,860 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:15,121 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:15,123 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:15,384 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:15,385 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:15,646 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:15,647 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:15,907 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:15,909 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:16,168 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:16,170 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:16,430 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:16,431 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:16,691 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:16,692 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:16,952 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:16,953 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:17,213 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:17,214 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:17,474 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:17,475 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:17,734 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:17,736 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:17,995 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:17,996 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:18,256 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:18,258 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:18,518 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:18,519 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:18,778 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:18,780 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:19,41 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:19,42 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:19,304 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:19,305 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:19,565 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:19,566 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:19,826 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:19,827 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:20,87 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:20,88 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:20,348 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:20,350 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:20,609 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:20,610 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:20,870 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:20,872 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:21,132 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:21,133 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:21,392 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:21,394 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:21,653 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:21,654 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:21,914 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:21,915 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:22,175 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:22,176 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:22,436 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:22,437 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:22,697 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:22,698 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:22,957 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:22,958 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:23,218 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:23,220 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:23,482 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:23,483 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:23,743 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:23,744 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:24,4 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:24,5 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:24,265 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:24,266 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:24,525 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:24,527 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:24,788 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:24,790 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:25,50 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:25,52 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:25,312 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:25,314 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:25,574 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:25,575 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:25,835 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:25,836 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:26,96 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:26,97 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:26,357 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:26,358 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:26,617 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:26,618 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:26,879 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:26,881 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:27,140 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:27,142 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:27,401 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:27,403 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:27,663 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:27,664 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:27,925 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:27,926 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:28,186 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:28,187 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:28,447 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:28,448 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:28,708 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:28,709 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:28,970 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:28,971 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:29,232 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:29,233 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:29,494 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:29,495 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:29,755 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:29,757 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:30,16 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:30,18 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:30,277 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:30,279 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:30,539 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:30,540 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:30,801 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:30,802 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:31,62 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:31,64 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:31,324 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:31,325 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:31,584 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:31,586 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:31,845 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:31,847 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:32,105 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:32,107 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:32,369 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:32,370 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:32,630 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:32,632 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
15:25:32,891 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 837, in cassandra.connection.Connection.factory
  File "cassandra/connection.py", line 600, in cassandra.connection.defunct_on_error.wrapper
  File "cassandra/connection.py", line 1421, in cassandra.connection.Connection._handle_auth_response
cassandra.AuthenticationFailed: Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"
15:25:32,893 cassandra.cluster ERROR Control connection failed to connect, shutting down Cluster:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 1690, in cassandra.cluster.Cluster.connect
  File "cassandra/cluster.py", line 3488, in cassandra.cluster.ControlConnection.connect
  File "cassandra/cluster.py", line 3533, in cassandra.cluster.ControlConnection._reconnect_internal
cassandra.cluster.NoHostAvailable: ('Unable to connect to any servers', {'127.0.0.3:9042': AuthenticationFailed('Failed to authenticate to 127.0.0.3:9042: Error from server: code=0100 [Bad credentials] message="Provided username doesntexist and/or password are incorrect"',)})
PASSED                                                                   [ 50%]
auth_join_ring_false_test.py::TestAuth::test_list_users 
-------------------------------- live log call ---------------------------------
15:25:33,479 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:25:33,566 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:25:33,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:25:50,374 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:25:50,468 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:25:50,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 75%]
auth_join_ring_false_test.py::TestAuth::test_modify_and_select_auth 
-------------------------------- live log call ---------------------------------
15:26:07,395 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:26:07,480 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:26:07,548 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:26:24,44 cassandra.protocol WARNING Server warning: Your replication factor 3 for keyspace ks is higher than the number of nodes 1
15:26:24,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:26:24,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:26:24,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:27:10,49 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
PASSED                                                                   [100%]
===Flaky Test Report===

test_login_existing_node passed 1 out of the required 1 times. Success!
test_login_new_node passed 1 out of the required 1 times. Success!
test_list_users passed 1 out of the required 1 times. Success!
test_modify_and_select_auth passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 4 passed in 302.12 seconds ==========================
[msx] rc = 0
