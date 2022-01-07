cassandra jmx_auth_test.py true true
the_test is jmx_auth_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

jmx_auth_test.py::TestJMXAuth::test_basic_auth 
-------------------------------- live log call ---------------------------------
19:40:56,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:40:56,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:40:56,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
jmx_auth_test.py::TestJMXAuth::test_revoked_jmx_access 
-------------------------------- live log call ---------------------------------
19:41:26,548 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:41:26,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:41:26,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_basic_auth passed 1 out of the required 1 times. Success!
test_revoked_jmx_access passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 61.62 seconds ===========================
[msx] rc = 0
