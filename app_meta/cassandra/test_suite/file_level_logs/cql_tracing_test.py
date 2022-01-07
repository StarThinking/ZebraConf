cassandra cql_tracing_test.py true true
the_test is cql_tracing_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

cql_tracing_test.py::TestCqlTracing::test_tracing_simple 
-------------------------------- live log call ---------------------------------
18:24:51,513 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:24:51,600 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:24:51,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:24:51,760 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:24:51,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:24:51,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:24:52,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:24:52,85 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:24:52,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
cql_tracing_test.py::TestCqlTracing::test_tracing_unknown_impl 
-------------------------------- live log call ---------------------------------
18:25:15,800 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:25:15,885 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:25:15,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:25:16,49 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:25:16,136 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:25:16,203 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:25:16,295 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:25:16,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:25:16,446 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 66%]
cql_tracing_test.py::TestCqlTracing::test_tracing_default_impl 
-------------------------------- live log call ---------------------------------
18:25:40,58 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:25:40,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:25:40,210 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
18:25:40,301 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:25:40,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:25:40,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
18:25:40,542 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
18:25:40,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
18:25:40,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_tracing_simple passed 1 out of the required 1 times. Success!
test_tracing_unknown_impl passed 1 out of the required 1 times. Success!
test_tracing_default_impl passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 73.13 seconds ===========================
[msx] rc = 0
