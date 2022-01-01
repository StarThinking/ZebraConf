cassandra delete_insert_test.py true true
the_test is delete_insert_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

delete_insert_test.py::TestDeleteInsert::test_delete_insert_search 
-------------------------------- live log call ---------------------------------
04:27:17,798 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:27:17,883 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:27:17,883 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:17,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
04:27:17,952 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:18,43 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:27:18,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:27:18,128 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:18,194 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
04:27:18,194 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:18,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:27:18,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:27:18,369 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:18,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
04:27:18,435 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:18,525 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
04:27:18,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:27:18,610 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
04:27:18,676 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
04:27:18,676 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_delete_insert_search passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 30.09 seconds ===========================
[msx] rc = 0
