cassandra streaming_test.py true true
the_test is streaming_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 2 items

streaming_test.py::TestStreaming::test_zerocopy_streaming 
-------------------------------- live log call ---------------------------------
02:08:15,383 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:15,468 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:08:15,537 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:08:15,628 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:15,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:08:15,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:08:15,832 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:15,917 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:08:15,967 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:16,52 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
PASSED                                                                   [ 50%]
streaming_test.py::TestStreaming::test_zerocopy_streaming_no_replication 
-------------------------------- live log call ---------------------------------
02:08:55,335 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:55,420 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:08:55,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:08:55,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:55,673 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:08:55,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:08:55,833 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:55,917 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:08:55,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
02:08:56,37 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:56,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:08:56,171 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:56,256 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:08:56,306 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:08:56,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [100%]
===Flaky Test Report===

test_zerocopy_streaming passed 1 out of the required 1 times. Success!
test_zerocopy_streaming_no_replication passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 2 passed in 82.87 seconds ===========================
[msx] rc = 0
