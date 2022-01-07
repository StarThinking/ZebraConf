cassandra stress_tool_test.py true true
the_test is stress_tool_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

stress_tool_test.py::TestStressSparsenessRatio::test_uniform_ratio 
-------------------------------- live log call ---------------------------------
02:10:39,99 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:10:39,184 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:10:39,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:10:53,864 cassandra.protocol WARNING Server warning: Read 1000 live rows and 40026 tombstone cells for query SELECT * FROM keyspace1.standard1 LIMIT 5000 ALLOW FILTERING; token 9209855756710953272 (see tombstone_warn_threshold)
PASSED                                                                   [ 33%]
stress_tool_test.py::TestStressSparsenessRatio::test_fixed_ratio 
-------------------------------- live log call ---------------------------------
02:10:54,358 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:10:54,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:10:54,509 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:11:09,88 cassandra.protocol WARNING Server warning: Read 1000 live rows and 34000 tombstone cells for query SELECT * FROM keyspace1.standard1 LIMIT 5000 ALLOW FILTERING; token 9209855756710953272 (see tombstone_warn_threshold)
PASSED                                                                   [ 66%]
stress_tool_test.py::TestStressWrite::test_quick_write 
-------------------------------- live log call ---------------------------------
02:11:09,335 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:11:09,420 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:11:09,487 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_uniform_ratio passed 1 out of the required 1 times. Success!
test_fixed_ratio passed 1 out of the required 1 times. Success!
test_quick_write passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 70.11 seconds ===========================
[msx] rc = 0
