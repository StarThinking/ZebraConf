cassandra auditlog_test.py true true
the_test is auditlog_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 5 items

auditlog_test.py::TestAuditlog::test_archiving 
-------------------------------- live log call ---------------------------------
01:22:23,636 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:22:23,723 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:22:23,723 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:22:23,792 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:22:23,792 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
auditlog_test.py::TestAuditlog::test_fql_nodetool_options 
-------------------------------- live log call ---------------------------------
01:22:42,132 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:22:42,216 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:22:42,216 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:22:42,282 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:22:42,283 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
auditlog_test.py::TestAuditlog::test_archiving_fql 
-------------------------------- live log call ---------------------------------
01:23:02,387 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:23:02,472 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:02,472 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:23:02,539 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:02,539 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
auditlog_test.py::TestAuditlog::test_archive_on_startup 
-------------------------------- live log call ---------------------------------
01:23:22,637 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:23:22,721 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:22,721 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:23:22,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:22,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
auditlog_test.py::TestAuditlog::test_archive_on_shutdown 
-------------------------------- live log call ---------------------------------
01:23:30,340 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:23:30,425 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:30,426 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:23:30,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:23:30,492 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_archiving passed 1 out of the required 1 times. Success!
test_fql_nodetool_options passed 1 out of the required 1 times. Success!
test_archiving_fql passed 1 out of the required 1 times. Success!
test_archive_on_startup passed 1 out of the required 1 times. Success!
test_archive_on_shutdown passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 5 passed in 76.49 seconds ===========================
[msx] rc = 0
