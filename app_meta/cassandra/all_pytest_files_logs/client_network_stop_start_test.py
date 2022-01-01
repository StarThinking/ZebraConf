cassandra client_network_stop_start_test.py true true
the_test is client_network_stop_start_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

client_network_stop_start_test.py::TestClientNetworkStopStart::test_defaults 
-------------------------------- live log call ---------------------------------
03:04:21,181 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
03:04:21,266 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:04:21,266 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
03:04:21,334 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
03:04:21,334 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
client_network_stop_start_test.py::TestClientNetworkStopStart::test_hsha_defaults SKIPPED [ 66%]
client_network_stop_start_test.py::TestClientNetworkStopStart::test_hsha_with_ssl SKIPPED [100%]
===Flaky Test Report===

test_defaults passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

===================== 1 passed, 2 skipped in 9.15 seconds ======================
[msx] rc = 0
