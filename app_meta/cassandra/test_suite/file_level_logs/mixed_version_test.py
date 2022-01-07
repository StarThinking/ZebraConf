cassandra mixed_version_test.py true true
the_test is mixed_version_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

mixed_version_test.py::TestSchemaChanges::test_friendly_unrecognized_table_handling 
-------------------------------- live log call ---------------------------------
21:45:44,904 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:45:44,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:45:45,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:45:45,150 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:45:45,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:45:45,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
SKIPPED                                                                  [100%]

========================== 1 skipped in 16.92 seconds ==========================
[msx] rc = 0
