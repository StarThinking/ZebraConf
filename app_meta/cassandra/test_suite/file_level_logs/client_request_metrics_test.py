cassandra client_request_metrics_test.py true true
the_test is client_request_metrics_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

client_request_metrics_test.py::TestClientRequestMetrics::test_client_request_metrics 
-------------------------------- live log call ---------------------------------
17:06:51,17 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:06:51,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:06:51,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
17:06:51,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
17:06:51,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:06:51,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
17:07:13,678 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [100%]
===Flaky Test Report===

test_client_request_metrics passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 110.03 seconds ==========================
[msx] rc = 0
