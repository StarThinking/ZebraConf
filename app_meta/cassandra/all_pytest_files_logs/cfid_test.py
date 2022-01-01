cassandra cfid_test.py true true
the_test is cfid_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 1 item

cfid_test.py::TestCFID::test_cfid 
-------------------------------- live log call ---------------------------------
03:03:03,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:03:03,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:03:03,854 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:03:03,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:03:03,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_cfid passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 1 passed in 16.58 seconds ===========================
[msx] rc = 0
