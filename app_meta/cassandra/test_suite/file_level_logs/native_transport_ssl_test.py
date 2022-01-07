cassandra native_transport_ssl_test.py true true
the_test is native_transport_ssl_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 4 items

native_transport_ssl_test.py::TestNativeTransportSSL::test_connect_to_ssl 
-------------------------------- live log call ---------------------------------
21:49:18,46 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:49:18,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:49:18,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 25%]
native_transport_ssl_test.py::TestNativeTransportSSL::test_connect_to_ssl_optional 
-------------------------------- live log call ---------------------------------
21:50:03,221 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:50:03,306 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:50:03,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
native_transport_ssl_test.py::TestNativeTransportSSL::test_use_custom_port 
-------------------------------- live log call ---------------------------------
21:50:21,757 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:50:21,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:50:21,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 75%]
native_transport_ssl_test.py::TestNativeTransportSSL::test_use_custom_ssl_port 
-------------------------------- live log call ---------------------------------
21:52:36,52 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:52:36,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:52:36,207 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_connect_to_ssl passed 1 out of the required 1 times. Success!
test_connect_to_ssl_optional passed 1 out of the required 1 times. Success!
test_use_custom_port passed 1 out of the required 1 times. Success!
test_use_custom_ssl_port passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=============================== warnings summary ===============================
native_transport_ssl_test.py::TestNativeTransportSSL::()::test_use_custom_port
  /users/masix/dtest/lib/python3.6/site-packages/ccmlib/node.py:694: UserWarning: Binary interface 127.0.0.1:9042 is not listening after 90 seconds, node may have failed to start.
    % (binary_itf[0], binary_itf[1], timeout))

-- Docs: http://doc.pytest.org/en/latest/warnings.html
==================== 4 passed, 1 warnings in 219.05 seconds ====================
[msx] rc = 0
