cassandra seed_test.py true true
the_test is seed_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

seed_test.py::TestGossiper::test_startup_no_live_seeds 
-------------------------------- live log call ---------------------------------
11:12:21,4 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:12:21,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:12:21,92 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:21,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:12:21,160 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:21,214 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:12:21,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:12:21,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
seed_test.py::TestGossiper::test_startup_non_seed_with_peers 
-------------------------------- live log call ---------------------------------
11:12:48,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:12:48,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:12:48,335 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:48,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:12:48,402 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:48,492 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:12:48,577 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:12:48,577 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:48,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:12:48,643 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:48,733 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:12:48,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:12:48,817 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:12:48,883 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:12:48,883 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:13:19,224 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:13:19,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:13:19,317 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:13:19,369 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:13:19,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:13:19,454 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:13:19,504 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:13:19,589 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
11:13:19,589 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
seed_test.py::TestGossiper::test_startup_after_ring_delay 
-------------------------------- live log call ---------------------------------
11:14:42,414 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:14:42,499 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:14:42,499 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:14:42,565 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
11:14:42,565 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:14:42,656 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
11:14:42,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:14:42,741 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
11:14:42,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
11:14:42,807 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_startup_no_live_seeds passed 1 out of the required 1 times. Success!
test_startup_non_seed_with_peers passed 1 out of the required 1 times. Success!
test_startup_after_ring_delay passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 3 passed in 172.35 seconds ==========================
[msx] rc = 0
