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
15:19:57,550 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:19:57,636 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:19:57,706 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 20%]
auditlog_test.py::TestAuditlog::test_fql_nodetool_options 
-------------------------------- live log call ---------------------------------
15:20:16,810 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:20:16,895 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:20:16,981 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
auditlog_test.py::TestAuditlog::test_archiving_fql 
-------------------------------- live log call ---------------------------------
15:20:37,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:20:37,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:20:37,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
auditlog_test.py::TestAuditlog::test_archive_on_startup 
-------------------------------- live log call ---------------------------------
15:20:58,325 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:20:58,411 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:20:58,479 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 80%]
auditlog_test.py::TestAuditlog::test_archive_on_shutdown 
-------------------------------- live log call ---------------------------------
15:21:06,522 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:21:06,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:21:06,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [100%]
===Flaky Test Report===

test_archiving passed 1 out of the required 1 times. Success!
test_fql_nodetool_options passed 1 out of the required 1 times. Success!
test_archiving_fql passed 1 out of the required 1 times. Success!
test_archive_on_startup passed 1 out of the required 1 times. Success!
test_archive_on_shutdown passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

========================== 5 passed in 79.27 seconds ===========================
[msx] rc = 0
