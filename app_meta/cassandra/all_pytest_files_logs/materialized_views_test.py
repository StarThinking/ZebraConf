cassandra materialized_views_test.py true true
the_test is materialized_views_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 60 items

materialized_views_test.py::TestMaterializedViews::test_view_metadata_cleanup 
-------------------------------- live log call ---------------------------------
05:55:28,572 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:55:28,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:55:28,657 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:55:28,725 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:55:28,725 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:55:28,816 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:55:28,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:55:28,900 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:55:28,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:55:28,967 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:55:46,707 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:55:48,513 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:55:50,519 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:55:52,468 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:55:54,403 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:55:58,636 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
05:55:58,666 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
05:56:03,668 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:56:05,470 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:56:07,346 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:56:08,387 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:56:10,385 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:56:14,430 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
05:56:14,441 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  1%]
materialized_views_test.py::TestMaterializedViews::test_create 
-------------------------------- live log call ---------------------------------
05:56:21,557 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:56:21,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:56:21,644 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:21,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:56:21,711 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:21,803 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:56:21,887 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:56:21,887 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:21,954 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:56:21,955 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:22,57 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:56:22,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:56:22,142 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:22,209 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:56:22,210 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:41,142 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [  3%]
materialized_views_test.py::TestMaterializedViews::test_gcgs_validation 
-------------------------------- live log call ---------------------------------
05:56:42,806 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:56:42,891 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:56:42,891 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:42,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:56:42,959 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:43,76 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:56:43,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:56:43,235 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:43,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:56:43,303 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:43,393 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:56:43,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:56:43,477 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:56:43,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:56:43,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:01,963 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [  5%]
materialized_views_test.py::TestMaterializedViews::test_insert 
-------------------------------- live log call ---------------------------------
05:57:06,338 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:57:06,427 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:57:06,427 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:06,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:57:06,495 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:06,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:57:06,670 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:57:06,670 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:06,736 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:57:06,736 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:06,827 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:57:06,912 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:57:06,912 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:06,978 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:57:06,978 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:25,262 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [  6%]
materialized_views_test.py::TestMaterializedViews::test_populate_mv_after_insert 
-------------------------------- live log call ---------------------------------
05:57:37,385 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:57:37,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:57:37,470 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:37,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:57:37,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:37,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:57:37,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:57:37,713 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:37,779 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:57:37,779 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:37,870 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:57:37,954 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:57:37,954 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:57:38,20 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:57:38,20 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:58:01,348 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
05:58:05,505 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
05:58:07,75 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
05:58:08,633 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  8%]
materialized_views_test.py::TestMaterializedViews::test_populate_mv_after_insert_wide_rows_version40 
-------------------------------- live log call ---------------------------------
05:58:14,752 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:58:14,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:58:14,837 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:58:14,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
05:58:14,904 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:58:14,996 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:58:15,82 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:58:15,82 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:58:15,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
05:58:15,149 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:58:15,240 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
05:58:15,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:58:15,325 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
05:58:15,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
05:58:15,392 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:00:07,262 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:00:12,368 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:00:14,11 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:00:15,635 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
XPASS                                                                    [ 10%]
materialized_views_test.py::TestMaterializedViews::test_populate_mv_after_insert_wide_rows SKIPPED [ 11%]
materialized_views_test.py::TestMaterializedViews::test_crc_check_chance 
-------------------------------- live log call ---------------------------------
06:03:09,677 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:09,763 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:03:09,763 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:09,830 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:03:09,830 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:09,921 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:10,5 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:03:10,5 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:10,71 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:03:10,72 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:10,163 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:10,247 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:03:10,247 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:10,314 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:03:10,314 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:29,623 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 13%]
materialized_views_test.py::TestMaterializedViews::test_prepared_statement 
-------------------------------- live log call ---------------------------------
06:03:32,702 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:32,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:03:32,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:32,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:03:32,855 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:32,946 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:33,31 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:03:33,31 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:33,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:03:33,98 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:33,188 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:33,273 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:03:33,273 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:33,339 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:03:33,339 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:51,543 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 15%]
materialized_views_test.py::TestMaterializedViews::test_immutable 
-------------------------------- live log call ---------------------------------
06:03:53,466 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:53,552 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:03:53,552 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:53,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:03:53,619 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:53,711 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:53,796 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:03:53,796 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:53,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:03:53,863 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:53,954 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:03:54,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:03:54,75 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:03:54,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:03:54,143 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:12,672 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 16%]
materialized_views_test.py::TestMaterializedViews::test_drop_mv 
-------------------------------- live log call ---------------------------------
06:04:13,989 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:14,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:04:14,73 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:14,140 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:04:14,140 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:14,231 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:14,315 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:04:14,315 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:14,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:04:14,381 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:14,472 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:14,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:04:14,556 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:14,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:04:14,622 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:33,75 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:04:34,64 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 18%]
materialized_views_test.py::TestMaterializedViews::test_drop_column 
-------------------------------- live log call ---------------------------------
06:04:37,755 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:37,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:04:37,841 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:37,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:04:37,908 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:37,999 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:38,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:04:38,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:38,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:04:38,150 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:38,241 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:38,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:04:38,325 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:38,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:04:38,392 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:56,848 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 20%]
materialized_views_test.py::TestMaterializedViews::test_drop_table 
-------------------------------- live log call ---------------------------------
06:04:58,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:58,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:04:58,608 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:58,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:04:58,675 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:58,766 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:58,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:04:58,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:58,915 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:04:58,916 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:59,6 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:04:59,90 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:04:59,90 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:04:59,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:04:59,156 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:17,605 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 21%]
materialized_views_test.py::TestMaterializedViews::test_clustering_column 
-------------------------------- live log call ---------------------------------
06:05:23,56 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:05:23,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:05:23,141 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:23,208 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:05:23,208 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:23,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:05:23,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:05:23,384 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:23,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:05:23,451 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:23,542 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:05:23,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:05:23,627 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:23,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:05:23,693 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:42,117 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 23%]
materialized_views_test.py::TestMaterializedViews::test_add_dc_after_mv_simple_replication 
-------------------------------- live log call ---------------------------------
06:05:53,870 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:05:53,957 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:05:53,957 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:54,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:05:54,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:54,114 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:05:54,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:05:54,198 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:54,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:05:54,264 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:54,355 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:05:54,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:05:54,439 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:05:54,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:05:54,505 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:06:12,969 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:06:29,508 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:06:29,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:06:29,603 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:06:29,678 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:06:29,678 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:07:42,898 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:07:42,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
06:07:42,989 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:07:43,63 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
06:07:43,63 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
materialized_views_test.py::TestMaterializedViews::test_add_dc_after_mv_network_replication 
-------------------------------- live log call ---------------------------------
06:09:04,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:09:04,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:09:04,182 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:04,248 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:09:04,248 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:04,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:09:04,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:09:04,423 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:04,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:09:04,489 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:04,580 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:09:04,664 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:09:04,665 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:04,731 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:09:04,731 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:23,855 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:09:40,692 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:09:40,789 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:09:40,789 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:09:40,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:09:40,865 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:10:55,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:10:55,185 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
06:10:55,185 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:10:55,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
06:10:55,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:07,460 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
06:12:09,189 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 26%]
materialized_views_test.py::TestMaterializedViews::test_add_node_after_mv 
-------------------------------- live log call ---------------------------------
06:12:22,939 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:12:23,25 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:12:23,25 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:23,91 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:12:23,91 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:23,183 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:12:23,267 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:12:23,267 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:23,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:12:23,340 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:23,431 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:12:23,515 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:12:23,515 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:23,582 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:12:23,582 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:41,949 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:12:53,806 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:12:53,899 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:12:53,899 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:12:53,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:12:53,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 28%]
materialized_views_test.py::TestMaterializedViews::test_insert_during_range_movement_rf1 
-------------------------------- live log call ---------------------------------
06:14:13,470 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:14:13,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:14:13,556 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:13,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:14:13,623 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:13,715 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:14:13,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:14:13,799 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:13,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:14:13,866 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:13,957 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:14:14,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:14:14,42 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:14,108 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:14:14,108 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:32,954 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:14:33,462 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:14:33,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:14:33,556 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:14:33,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:14:33,632 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:15:54,440 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:15:56,141 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:15:57,688 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:16:14,189 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 30%]
materialized_views_test.py::TestMaterializedViews::test_insert_during_range_movement_rf2 
-------------------------------- live log call ---------------------------------
06:16:20,858 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:16:20,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:16:20,944 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:21,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:16:21,11 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:21,102 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:16:21,187 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:16:21,188 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:21,254 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:16:21,254 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:21,345 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:16:21,429 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:16:21,429 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:21,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:16:21,496 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:39,994 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:16:40,922 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:16:41,42 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:16:41,49 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:16:41,140 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:16:41,140 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:02,523 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:18:04,106 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:18:05,635 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:18:07,287 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 31%]
materialized_views_test.py::TestMaterializedViews::test_insert_during_range_movement_rf3 
-------------------------------- live log call ---------------------------------
06:18:13,647 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:18:13,733 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:18:13,733 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:13,801 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:18:13,801 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:13,893 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:18:13,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:18:13,979 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:14,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:18:14,46 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:14,137 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:18:14,222 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:18:14,222 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:14,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:18:14,289 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:32,928 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:18:33,867 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:18:33,966 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:18:33,966 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:18:34,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:18:34,45 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:19:57,225 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:19:58,847 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:20:00,505 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:20:02,58 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 33%]
materialized_views_test.py::TestMaterializedViews::test_add_node_after_wide_mv_with_range_deletions 
-------------------------------- live log call ---------------------------------
06:20:08,214 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:20:08,299 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:20:08,299 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:20:08,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:20:08,366 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:20:08,468 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:20:08,552 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:20:08,552 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:20:08,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:20:08,619 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:20:08,710 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:20:08,794 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:20:08,794 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:20:08,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:20:08,860 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:20:27,282 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:21:03,621 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:21:03,716 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:21:03,717 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:21:03,793 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:21:03,793 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:21:03,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:21:03,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:21:03,945 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 35%]
materialized_views_test.py::TestMaterializedViews::test_add_node_after_very_wide_mv 
-------------------------------- live log call ---------------------------------
06:22:37,49 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:22:37,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:22:37,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:22:37,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:22:37,202 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:22:37,294 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:22:37,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:22:37,379 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:22:37,445 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:22:37,445 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:22:37,537 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:22:37,621 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:22:37,621 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:22:37,688 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:22:37,688 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:22:56,228 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:25:35,105 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:25:35,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:25:35,198 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:25:35,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:25:35,273 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:25:35,327 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:25:35,417 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:25:35,418 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
materialized_views_test.py::TestMaterializedViews::test_add_write_survey_node_after_mv 
-------------------------------- live log call ---------------------------------
06:31:03,292 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:31:03,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:31:03,377 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:03,444 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:31:03,444 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:03,535 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:31:03,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:31:03,619 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:03,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:31:03,685 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:03,776 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:31:03,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:31:03,860 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:03,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:31:03,926 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:22,179 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:31:33,980 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:31:34,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:31:34,75 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:31:34,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
06:31:34,151 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 38%]
materialized_views_test.py::TestMaterializedViews::test_allow_filtering 
-------------------------------- live log call ---------------------------------
06:32:52,553 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:32:52,665 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:32:52,665 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:32:52,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:32:52,732 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:32:52,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:32:52,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:32:52,907 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:32:52,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:32:52,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:32:53,62 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:32:53,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:32:53,146 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:32:53,212 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:32:53,212 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:11,446 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:33:13,235 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 40%]
materialized_views_test.py::TestMaterializedViews::test_secondary_index 
-------------------------------- live log call ---------------------------------
06:33:36,983 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:33:37,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:33:37,69 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:37,135 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:33:37,135 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:37,226 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:33:37,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:33:37,310 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:37,376 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:33:37,377 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:37,467 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:33:37,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:33:37,551 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:37,617 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:33:37,617 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:56,933 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 41%]
materialized_views_test.py::TestMaterializedViews::test_ttl 
-------------------------------- live log call ---------------------------------
06:33:58,744 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:33:58,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:33:58,829 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:58,896 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:33:58,896 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:58,987 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:33:59,71 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:33:59,71 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:59,138 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:33:59,138 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:59,229 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:33:59,313 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:33:59,313 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:33:59,379 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:33:59,379 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:34:17,649 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 43%]
materialized_views_test.py::TestMaterializedViews::test_query_all_new_column 
-------------------------------- live log call ---------------------------------
06:34:40,837 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:34:40,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:34:40,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:34:40,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:34:40,988 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:34:41,79 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:34:41,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:34:41,163 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:34:41,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:34:41,230 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:34:41,320 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:34:41,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:34:41,405 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:34:41,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:34:41,471 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:00,588 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 45%]
materialized_views_test.py::TestMaterializedViews::test_query_new_column 
-------------------------------- live log call ---------------------------------
06:35:14,148 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:35:14,233 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:35:14,234 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:14,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:35:14,300 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:14,391 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:35:14,475 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:35:14,475 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:14,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:35:14,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:14,632 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:35:14,719 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:35:14,719 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:14,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:35:14,787 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:33,219 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:35:34,652 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 46%]
materialized_views_test.py::TestMaterializedViews::test_rename_column 
-------------------------------- live log call ---------------------------------
06:35:47,965 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:35:48,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:35:48,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:48,118 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:35:48,118 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:48,209 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:35:48,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:35:48,297 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:48,363 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:35:48,363 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:48,454 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:35:48,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:35:48,538 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:35:48,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:35:48,605 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:07,35 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 48%]
materialized_views_test.py::TestMaterializedViews::test_rename_column_atomicity 
-------------------------------- live log call ---------------------------------
06:36:19,759 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:36:19,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:36:19,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:19,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:36:19,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:26,224 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:36:30,227 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
06:36:31,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:36:33,524 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:36:37,34 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
materialized_views_test.py::TestMaterializedViews::test_lwt 
-------------------------------- live log call ---------------------------------
06:36:44,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:36:44,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:36:44,112 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:44,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:36:44,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:44,271 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:36:44,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:36:44,355 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:44,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:36:44,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:44,517 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:36:44,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:36:44,602 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:36:44,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:36:44,668 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:37:02,887 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:37:17,484 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:19,166 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:20,814 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:35,161 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:36,575 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:38,70 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:50,677 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:52,140 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:37:53,595 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:38:05,565 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:38:07,59 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:38:08,517 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 51%]
materialized_views_test.py::TestMaterializedViews::test_interrupt_build_process 
-------------------------------- live log call ---------------------------------
06:38:13,380 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:38:13,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:38:13,467 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:13,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:38:13,536 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:13,629 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:38:13,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:38:13,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:13,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:38:13,782 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:13,874 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:38:13,959 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:38:13,959 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:14,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:38:14,27 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:14,84 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:38:14,169 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:38:14,169 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:14,220 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:38:14,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:38:14,305 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:38:14,356 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:38:14,441 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:38:14,441 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:39:41,750 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:39:43,814 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
06:39:44,920 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:39:46,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:39:50,639 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:39:57,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:40:11,195 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:40:45,183 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 62.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:40:46,701 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:40:47,792 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:40:49,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:40:54,108 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:41:02,530 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:41:02,897 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:41:02,898 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:41:04,35 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:41:06,240 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:41:09,950 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:41:17,273 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:41:18,379 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:41:33,117 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:41:35,855 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:41:58,47 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 53%]
materialized_views_test.py::TestMaterializedViews::test_drop_while_building SKIPPED [ 55%]
materialized_views_test.py::TestMaterializedViews::test_drop_with_stopped_build 
-------------------------------- live log call ---------------------------------
06:42:48,88 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:42:48,175 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:42:48,175 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:42:48,244 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,337 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:42:48,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:42:48,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:42:48,491 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,609 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:42:48,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:42:48,694 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,762 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:42:48,762 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,819 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:42:48,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:42:48,903 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:48,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:42:49,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:42:49,39 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:42:49,91 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:42:49,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:42:49,176 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:43:50,901 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:43:59,454 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:44:23,189 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 56%]
materialized_views_test.py::TestMaterializedViews::test_resume_stopped_build 
-------------------------------- live log call ---------------------------------
06:44:23,808 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:44:23,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:44:23,894 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:23,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:44:23,964 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,56 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:44:24,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:44:24,141 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,209 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:44:24,210 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:44:24,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:44:24,392 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,461 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:44:24,461 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,518 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:44:24,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:44:24,603 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,654 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:44:24,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:44:24,739 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:44:24,791 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:44:24,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:44:24,934 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:45:25,227 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:45:31,196 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:45:43,358 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
06:45:43,358 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:45:43,361 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:45:44,368 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:45:44,369 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:45:46,74 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:45:46,475 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:45:50,485 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:45:50,686 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:45:57,905 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:45:58,807 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:46:13,359 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:46:13,361 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:46:14,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
06:46:14,453 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:46:16,156 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:46:16,557 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:46:20,66 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:46:49,76 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 58%]
materialized_views_test.py::TestMaterializedViews::test_mv_with_default_ttl_with_flush 
-------------------------------- live log call ---------------------------------
06:46:49,917 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:46:50,2 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:46:50,2 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,71 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:46:50,71 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,163 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:46:50,303 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:46:50,303 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:46:50,371 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,462 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:46:50,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:46:50,546 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,611 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:46:50,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,666 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:46:50,749 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:46:50,750 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,798 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:46:50,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:46:50,883 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:46:50,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:46:51,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:46:51,15 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:47:12,12 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:47:14,336 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:15,922 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:17,513 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:24,191 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:25,646 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:27,172 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:33,223 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:34,696 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:36,180 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:42,79 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:43,528 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:44,995 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:56,713 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:58,138 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:47:59,560 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:05,650 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:07,71 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:08,500 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:14,361 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:15,784 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:17,207 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:23,24 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:24,461 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:25,841 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:41,531 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:48:43,825 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:45,271 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:46,680 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:52,823 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:54,235 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:48:55,639 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:01,296 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:02,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:04,112 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:15,498 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:16,905 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:18,338 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:24,275 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:25,667 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:27,93 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:32,787 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:34,169 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:49:35,656 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 60%]
materialized_views_test.py::TestMaterializedViews::test_mv_with_default_ttl_without_flush 
-------------------------------- live log call ---------------------------------
06:49:45,981 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:49:46,67 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:49:46,67 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,134 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:49:46,134 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,226 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:49:46,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:49:46,311 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:49:46,377 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,469 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:49:46,553 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:49:46,553 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:49:46,620 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,676 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:49:46,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:49:46,761 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,811 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:49:46,896 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:49:46,896 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:49:46,946 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:49:47,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:49:47,41 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:50:07,673 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:50:10,551 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:12,170 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:13,763 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:15,304 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:16,837 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:18,292 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:19,802 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:21,253 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:22,770 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:24,238 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:25,695 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:27,123 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:28,582 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:30,50 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:31,519 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:32,973 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:34,446 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:35,880 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:37,333 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:38,781 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:40,401 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:41,837 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:43,325 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:44,716 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:51,273 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:50:53,973 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:55,437 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:56,853 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:58,346 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:50:59,794 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:01,264 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:02,721 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:04,195 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:05,604 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:07,75 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:08,491 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:09,891 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:11,362 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:12,745 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:14,127 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:15,625 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:17,24 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:18,506 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 61%]
materialized_views_test.py::TestMaterializedViews::test_no_base_column_in_view_pk_complex_timestamp_with_flush 
-------------------------------- live log call ---------------------------------
06:51:19,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:51:19,178 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:51:19,178 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,245 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:51:19,245 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,337 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:51:19,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:51:19,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:51:19,490 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,581 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:51:19,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:51:19,667 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,739 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:51:19,739 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,795 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:51:19,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:51:19,880 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:19,931 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:51:20,15 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:51:20,15 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:20,66 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:51:20,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:51:20,151 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:51:41,888 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:51:44,665 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:46,282 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:47,918 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:54,596 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:56,93 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:51:57,550 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:03,716 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:05,179 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:06,639 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:12,572 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:14,10 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:15,466 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:21,523 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:23,13 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:24,478 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:30,537 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:31,970 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:33,417 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:39,471 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:40,974 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:42,550 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:48,438 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:49,879 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:51,265 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:57,194 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:52:58,642 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:00,86 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:05,769 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:07,188 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:08,596 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:14,371 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:15,791 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:17,257 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:23,200 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:24,634 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:26,87 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:31,909 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:33,369 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:34,776 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:40,494 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:41,896 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:53:43,304 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:54:09,313 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:54:10,932 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:54:12,353 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 63%]
materialized_views_test.py::TestMaterializedViews::test_no_base_column_in_view_pk_complex_timestamp_without_flush SKIPPED [ 65%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_complex_timestamp_with_flush 
-------------------------------- live log call ---------------------------------
06:54:37,567 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:54:37,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:54:37,653 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:37,722 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:54:37,722 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:37,815 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:54:37,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:54:37,900 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:37,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:54:37,967 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:38,59 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:54:38,144 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:54:38,144 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:38,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:54:38,212 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:38,267 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:54:38,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:54:38,352 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:38,402 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:54:38,487 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:54:38,487 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:38,537 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:54:38,623 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:54:38,623 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:54:59,194 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:55:02,110 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:03,762 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:05,379 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:11,971 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:13,411 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:14,889 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:20,998 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:22,440 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:23,917 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:29,944 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:31,381 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:32,847 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:38,856 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:40,306 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:41,775 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:53,562 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:55,71 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:55:56,533 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:02,735 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:04,342 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:05,808 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:11,695 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:13,154 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:14,583 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:20,230 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:21,694 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:23,80 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:29,58 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:30,467 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:31,911 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:37,766 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:39,154 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:40,546 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:56:44,876 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:56:45,887 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:48,195 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:51,681 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:56:51,683 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:52,208 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:52,434 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:56:52,435 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:52,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:52,883 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:56:52,888 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:56:52,889 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:56:52,892 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:56:53,441 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:53,905 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:53,991 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:53,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:54,14 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:54,895 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:55,61 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:56:55,62 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:55,647 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:55,803 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:55,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:55,996 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:56,68 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:56,120 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:56,524 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:56:56,525 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:57,630 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:57,873 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:58,405 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:59,156 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:56:59,535 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:56:59,914 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:00,7 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:00,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:00,459 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:00,460 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:00,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:00,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:01,373 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:01,375 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:01,666 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:01,788 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:02,328 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:57:02,383 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:02,839 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:02,841 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:03,739 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:03,741 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:03,949 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:03,950 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:03,973 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:04,332 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:04,337 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:04,589 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:04,849 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:05,287 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:57:05,347 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:05,357 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:05,358 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:05,798 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:05,800 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:05,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:05,954 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:06,565 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:06,807 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:06,845 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:06,856 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:07,152 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:08,48 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:08,387 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:08,571 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:08,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:08,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:08,716 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:08,902 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:08,921 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:09,145 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:09,146 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:09,152 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:09,865 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:10,252 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:10,299 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:10,300 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:10,535 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:10,537 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:10,861 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:11,305 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:11,467 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:11,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:11,767 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:11,769 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:12,57 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:12,682 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:12,772 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:12,774 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:13,144 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:13,146 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:13,228 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:13,404 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:57:13,406 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:13,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:13,748 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:14,252 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:14,418 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:14,572 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:14,575 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:14,881 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:57:14,882 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:15,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:15,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:15,679 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:16,57 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:16,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:16,169 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:16,308 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:16,724 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:17,24 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:17,485 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:17,584 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:17,925 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:17,959 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:17,992 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:18,983 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:19,89 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:19,492 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:19,967 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:20,735 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:57:21,47 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:21,193 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:21,807 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:22,205 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:22,286 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:23,289 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:23,602 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:25,92 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:27,196 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:28,625 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:28,717 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:29,620 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:31,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:57:31,633 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 66%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_complex_timestamp_without_flush 
-------------------------------- live log call ---------------------------------
06:57:42,265 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:57:42,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:57:42,351 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:42,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:57:42,418 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:42,525 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:57:42,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:57:42,611 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:42,678 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:57:42,678 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:42,769 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:57:42,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:57:42,856 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:42,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:57:42,924 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:42,979 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:57:43,64 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:57:43,64 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:43,114 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:57:43,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
06:57:43,200 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:57:43,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:57:43,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
06:57:43,335 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:58:03,914 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
06:58:06,932 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:08,557 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:10,185 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:11,735 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:13,233 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:14,752 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:16,293 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:17,802 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:19,274 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:20,797 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:22,268 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:23,724 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:25,246 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:26,822 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:28,347 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:35,114 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:36,568 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:38,104 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:39,606 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:41,69 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:42,468 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:44,4 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:45,423 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:46,819 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:48,237 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:49,690 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:51,119 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:52,521 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:54,8 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:55,421 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:56,889 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:58,316 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:59,765 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:58:59,824 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:00,834 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:02,741 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:06,558 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:06,560 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:07,355 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:07,667 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:07,832 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:08,93 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:08,95 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:08,531 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:08,532 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:08,860 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:09,200 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:09,371 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:09,738 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:10,159 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:10,160 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:10,905 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:11,58 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:11,60 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:11,167 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:11,266 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:11,544 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:12,164 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:12,458 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:12,459 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:13,171 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:13,221 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:13,223 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:13,565 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:13,582 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:14,270 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:14,429 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:14,740 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:14,741 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:15,412 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:15,413 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:15,417 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:15,570 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:15,678 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:15,746 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:15,857 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:16,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:16,419 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:16,434 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:16,579 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:16,808 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:16,810 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:17,316 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:59:17,794 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:17,797 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:17,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:17,961 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:18,425 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:18,482 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:18,741 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
06:59:18,806 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:19,272 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:19,274 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:19,681 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:19,682 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:20,125 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:20,188 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:20,481 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:20,690 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:20,712 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:20,876 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:21,107 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:21,108 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:22,115 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:22,206 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:22,258 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:22,259 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:22,278 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:22,339 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:22,486 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:22,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:22,594 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:23,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:23,365 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:23,705 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:23,715 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:23,716 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:23,734 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:23,997 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:23,999 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:24,20 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:24,606 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:24,721 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:25,104 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:25,323 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:25,410 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:25,412 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:25,472 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:26,606 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:26,617 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:26,813 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:26,814 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:26,899 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:26,907 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:27,9 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:27,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:27,819 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:27,931 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:28,306 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
06:59:28,308 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:28,334 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:28,336 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:28,395 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:28,809 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:28,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:29,413 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:29,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:29,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:29,724 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:29,756 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
06:59:29,757 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:29,783 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:29,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:30,763 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:30,853 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:31,19 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:31,318 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:31,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:31,346 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:32,425 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
06:59:32,668 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:33,35 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:34,328 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:35,991 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:36,589 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:36,589 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:37,193 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:39,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:40,296 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:40,401 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:41,706 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:45,117 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:45,209 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:46,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:47,122 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:48,219 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
06:59:48,424 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 68%]
materialized_views_test.py::TestMaterializedViews::test_expired_liveness_with_limit_rf1_nodes1 
-------------------------------- live log call ---------------------------------
06:59:54,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:59:54,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:59:54,337 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:59:54,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:59:54,404 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
06:59:54,460 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
06:59:54,545 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
06:59:54,545 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:00,824 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 70%]
materialized_views_test.py::TestMaterializedViews::test_expired_liveness_with_limit_rf1_nodes3 
-------------------------------- live log call ---------------------------------
07:00:02,464 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:02,550 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:02,550 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:02,618 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:02,618 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:02,711 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:02,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:02,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:02,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:02,863 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:02,954 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:03,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:03,39 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:03,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:03,106 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:03,161 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:03,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:03,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:03,296 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:03,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:03,381 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:03,431 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:03,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:03,517 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:24,557 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 71%]
materialized_views_test.py::TestMaterializedViews::test_expired_liveness_with_limit_rf3 
-------------------------------- live log call ---------------------------------
07:00:28,293 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:28,380 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:28,380 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:28,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:28,453 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:28,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:28,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:28,632 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:28,699 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:28,699 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:28,801 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:28,885 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:28,886 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:28,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:28,952 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:29,8 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:29,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:29,93 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:29,143 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:29,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:29,351 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:29,402 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:29,486 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:29,486 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:50,23 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 73%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_commutative_tombstone_with_flush 
-------------------------------- live log call ---------------------------------
07:00:53,889 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:53,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:53,974 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:54,40 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,131 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:54,216 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:54,216 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:54,287 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,379 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:54,465 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:54,465 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:54,531 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:54,671 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:00:54,671 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,721 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:54,805 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:00:54,806 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:00:54,855 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:00:54,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:00:54,940 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:01:16,535 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:01:24,446 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:25,989 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:27,511 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:34,193 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:35,690 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:37,188 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:43,266 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:44,719 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:46,232 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:52,172 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:53,642 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:01:55,113 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:01,17 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:02,490 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:03,956 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:15,702 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:17,172 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:18,757 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 75%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_commutative_tombstone_without_flush 
-------------------------------- live log call ---------------------------------
07:02:24,71 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:02:24,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:02:24,158 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:02:24,225 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,316 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:02:24,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:02:24,402 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,468 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:02:24,468 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,560 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:02:24,645 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:02:24,645 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,712 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:02:24,712 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:02:24,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:02:24,853 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:24,903 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:02:24,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:02:24,988 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:25,38 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:02:25,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:02:25,123 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:02:45,723 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:02:53,162 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:54,683 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:56,228 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:57,734 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:02:59,229 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:00,698 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:02,276 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:03,725 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:05,188 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:06,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:08,248 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:09,665 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:11,160 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:12,651 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:14,108 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:15,602 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:17,138 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:18,654 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 76%]
materialized_views_test.py::TestMaterializedViews::test_view_tombstone 
-------------------------------- live log call ---------------------------------
07:03:19,333 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:03:19,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:03:19,420 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:19,487 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:03:19,487 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:19,580 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:03:19,665 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:03:19,665 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:19,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:03:19,732 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:19,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:03:19,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:03:19,909 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:20,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:03:20,58 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:20,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:03:20,202 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:03:20,202 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:20,253 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:03:20,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:03:20,338 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:20,388 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:03:20,471 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:03:20,472 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:03:41,756 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:03:45,89 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:46,698 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:48,261 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:49,717 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:51,179 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:52,623 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:54,100 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:55,600 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:57,32 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:03:57,72 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:03:58,182 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:00,289 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:03,700 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:06,513 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:04:08,36 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:04:12,140 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:16,673 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:04:16,675 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:17,780 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:19,986 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:21,166 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:04:21,167 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:22,373 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 78%]
materialized_views_test.py::TestMaterializedViews::test_simple_repair_by_base 
-------------------------------- live log call ---------------------------------
07:04:24,352 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:04:24,437 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:04:24,438 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:24,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:04:24,505 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:24,597 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:04:24,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:04:24,682 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:24,750 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:04:24,750 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:24,843 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:04:24,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:04:24,927 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:24,996 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:04:24,997 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:25,52 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:04:25,137 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:04:25,138 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:25,188 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:04:25,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:04:25,272 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:25,322 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:04:25,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:04:25,408 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:04:45,770 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:04:46,899 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:04:48,104 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:50,11 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:04:53,622 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:05:00,61 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:05:01,553 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:05:01,735 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:05:19,888 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 80%]
materialized_views_test.py::TestMaterializedViews::test_simple_repair_by_view 
-------------------------------- live log call ---------------------------------
07:05:54,397 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:05:54,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:05:54,483 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:54,549 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:05:54,550 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:54,640 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:05:54,724 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:05:54,724 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:54,791 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:05:54,791 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:54,899 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:05:54,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:05:54,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:55,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:05:55,50 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:55,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:05:55,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:05:55,190 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:55,239 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:05:55,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:05:55,324 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:05:55,374 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:05:55,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:05:55,458 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:06:16,853 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:06:17,985 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:06:19,91 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:06:21,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:06:25,311 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:06:31,223 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:06:32,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:06:32,823 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:06:49,835 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 81%]
materialized_views_test.py::TestMaterializedViews::test_base_replica_repair 
-------------------------------- live log call ---------------------------------
07:07:25,114 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:07:25,200 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:07:25,201 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:07:25,267 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:07:25,268 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:07:25,359 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:07:25,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:07:25,443 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:07:25,509 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:07:25,509 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:07:25,601 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:07:25,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:07:25,686 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:07:25,752 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:07:25,752 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:07:43,930 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:07:49,666 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:07:51,278 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:07:52,815 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:08:12,209 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:08:12,210 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:08:12,214 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:12,989 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:08:13,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:15,136 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:19,349 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:19,642 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:08:21,245 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:08:21,246 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:22,251 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:22,788 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:08:22,790 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:23,795 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:24,256 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:26,1 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:26,872 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:28,878 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:30,336 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:35,927 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:38,472 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:42,210 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:08:42,212 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:43,254 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:43,255 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:08:45,61 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:48,674 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:55,15 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:08:56,998 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 83%]
materialized_views_test.py::TestMaterializedViews::test_base_replica_repair_with_contention 
-------------------------------- live log call ---------------------------------
07:09:09,660 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:09:09,745 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:09:09,745 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:09,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:09:09,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:09,914 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:09:09,998 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:09:09,998 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:10,64 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:09:10,64 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:10,155 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:09:10,240 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:09:10,240 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:10,307 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:09:10,307 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:29,304 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:09:34,751 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:09:36,419 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:09:38,70 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:09:51,94 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:09:51,204 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:09:51,204 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:09:56,798 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:09:56,802 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:09:57,766 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:09:57,896 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1439, in cassandra.connection.Connection.set_keyspace_blocking
  File "cassandra/connection.py", line 1029, in cassandra.connection.Connection.wait_for_response
  File "cassandra/connection.py", line 1076, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1071, in cassandra.connection.Connection.wait_for_responses
  File "cassandra/connection.py", line 1570, in cassandra.connection.ResponseWaiter.deliver
cassandra.InvalidRequest: Error from server: code=2200 [Invalid query] message="Keyspace 'ks' does not exist"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 405, in cassandra.pool.HostConnection.__init__
  File "cassandra/connection.py", line 1447, in cassandra.connection.Connection.set_keyspace_blocking
cassandra.connection.ConnectionException: Problem while setting keyspace: InvalidRequest('Error from server: code=2200 [Invalid query] message="Keyspace \'ks\' does not exist"',)
07:09:58,305 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:09:59,310 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:01,418 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:04,725 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:10:05,30 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:06,393 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:10:06,395 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:07,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:08,43 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:10:08,44 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:09,150 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:09,406 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:10,955 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:13,16 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:13,353 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:15,476 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:20,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:23,426 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:26,799 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:10:26,801 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:27,853 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:29,257 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:10:29,858 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:33,875 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:40,476 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:10:42,205 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 85%]
materialized_views_test.py::TestMaterializedViews::test_complex_repair 
-------------------------------- live log call ---------------------------------
07:11:00,882 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:00,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:11:00,967 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,34 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:11:01,34 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,125 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:01,209 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:11:01,209 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,275 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:11:01,275 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,366 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:01,450 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:11:01,450 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:11:01,517 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,608 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:01,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:11:01,692 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,758 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:11:01,758 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:01,849 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:01,933 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:11:01,933 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:02,0 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:11:02,0 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:02,55 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:02,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:11:02,139 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:02,190 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:02,295 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:11:02,295 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:02,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:02,430 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:11:02,430 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:02,480 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:02,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:11:02,564 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:02,613 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:11:02,698 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:11:02,699 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:11:26,17 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:11:28,655 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:11:29,660 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:11:31,668 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:11:35,762 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:11:35,781 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:11:36,783 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:11:38,789 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:11:43,201 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:11:44,204 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:11:51,860 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:13:26,419 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:13:26,423 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:13:26,425 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:13:26,426 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:13:26,427 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:13:26,428 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:13:27,439 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:13:27,542 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:13:27,542 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:13:29,553 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:13:29,753 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:13:29,854 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:13:33,775 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:13:33,775 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:13:34,74 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:13:41,128 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:13:42,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:13:42,331 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:13:56,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:13:56,880 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 34.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:13:59,287 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:14:29,371 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 56.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
PASSED                                                                   [ 86%]
materialized_views_test.py::TestMaterializedViews::test_throttled_partition_update 
-------------------------------- live log call ---------------------------------
07:14:54,162 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:54,248 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:14:54,248 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:54,315 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:14:54,315 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:54,407 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:54,491 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:14:54,492 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:54,602 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:14:54,602 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:54,694 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:54,778 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:14:54,778 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:54,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:14:54,845 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:54,935 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:14:55,19 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,85 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:14:55,85 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,175 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,260 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:14:55,260 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,326 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:14:55,326 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,381 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,465 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:14:55,465 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,514 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:14:55,598 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,648 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:14:55,732 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,781 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:14:55,865 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:14:55,914 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:14:55,998 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:14:55,998 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:15:27,989 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:15:29,603 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:15:30,645 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:15:32,953 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:15:37,366 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:15:37,610 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:15:38,671 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:15:40,877 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:15:44,787 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:15:44,988 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:15:53,422 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:15:54,905 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:15:56,463 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:15:58,7 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:15:59,763 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:16:11,223 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:16:20,905 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:16:21,927 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:24,133 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:26,442 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:16:26,443 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:27,649 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:28,144 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:28,921 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:16:29,654 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:29,948 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:16:31,853 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 58.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:16:31,954 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:16:33,263 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:36,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:16:36,565 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:40,855 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:16:41,193 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:43,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:16:45,203 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:16:53,123 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:56,933 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:16:57,981 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:16:57,982 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:16:58,988 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:16:59,39 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:17:01,193 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:17:05,605 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:17:13,836 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:17:26,408 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 64.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:17:27,210 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 63.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:17:27,470 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:17:32,826 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 72.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:00,157 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:18:02,534 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:04,196 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:05,796 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:07,436 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:09,207 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:14,553 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:16,58 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:17,555 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:19,39 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:20,526 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:18:24,880 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:18:24,882 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:25,986 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:28,191 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:32,526 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:18:32,527 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:32,804 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:33,632 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:34,168 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:18:34,170 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:35,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:35,774 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:18:35,775 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:35,838 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:36,881 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:37,583 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:38,888 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:40,451 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:40,847 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:18:40,848 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:41,954 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:42,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:42,94 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:43,300 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:43,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:44,544 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:18:44,545 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:45,550 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:45,885 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 138.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:46,46 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:18:46,47 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:46,522 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:18:46,522 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:18:46,524 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:18:46,525 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:18:46,527 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:47,59 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:47,539 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:18:47,540 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:47,628 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:47,628 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:47,728 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:47,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:47,758 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:48,372 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:48,646 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:48,964 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:49,27 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:18:49,28 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:49,174 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:49,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:49,641 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:49,842 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:49,942 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:50,37 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:50,516 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:18:50,517 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:18:50,551 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:51,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:51,224 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:51,523 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:18:51,869 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:52,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:52,874 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:53,628 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:18:53,652 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:53,653 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:53,654 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:53,853 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:18:54,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:18:56,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:18:56,793 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:18:57,839 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:18:58,987 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:00,174 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:01,697 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:01,874 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:02,376 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:02,376 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:02,777 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:03,85 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:05,59 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:05,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:05,424 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:06,165 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:07,166 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:07,415 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:19:07,417 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:08,622 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:09,177 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:19:09,179 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:09,959 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 139.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:10,384 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:10,728 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:12,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:12,824 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:14,747 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:15,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:16,10 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:16,99 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:16,311 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:16,522 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:19:16,524 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:17,615 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:17,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:18,417 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:18,818 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:19,208 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:19,721 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:19,795 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:21,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:23,662 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:24,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:24,422 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:31,50 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:32,261 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 67.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:33,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 64.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:38,948 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 71.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:39,601 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:39,851 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:40,965 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:42,306 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 70.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:43,622 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 67.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:19:45,389 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:46,781 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 72.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:46,793 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 60.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:49,270 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 67.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:49,826 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:51,448 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:51,451 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:51,454 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:51,455 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:51,456 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:19:51,458 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:19:51,460 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:19:51,461 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:19:52,469 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:52,570 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:52,570 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:52,574 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:52,813 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 67.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:54,289 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:54,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:54,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:54,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:54,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:19:55,331 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 56.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:58,22 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:19:58,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:19:58,122 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:19:59,160 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:20:06,26 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:20:06,532 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:20:06,936 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:20:07,643 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:20:08,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 60.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:20:16,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 63.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:20:16,524 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:20:16,525 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:17,624 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:19,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:20,331 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:20:21,446 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:20:21,447 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:22,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:20:22,632 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:23,534 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:20:23,740 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:24,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:20:24,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:20:24,838 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:28,648 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:32,466 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:36,670 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:36,872 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 140.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:20:38,289 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 145.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:39,511 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 140.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:47,603 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 130.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:20:49,620 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 135.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:20:49,808 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:50,634 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 144.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:20:50,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 133.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:51,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 130.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:20:52,712 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 120.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:53,613 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 55.68 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:20:53,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:20:54,816 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:20:56,525 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 147.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:20:57,323 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 72.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:20:57,724 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 62.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:20:59,755 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 108.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:00,35 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 119.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:03,477 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 143.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:21:04,139 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 284.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:08,758 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 145.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:19,498 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 142.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:20,888 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 64.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:26,851 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:26,854 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:26,857 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:26,857 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:26,859 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:21:26,861 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:21:26,863 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:21:26,865 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:21:27,818 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 71.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:27,870 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:28,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:28,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:28,77 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:29,522 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 225.28 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:29,786 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:29,988 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:30,138 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 133.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:30,192 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:30,398 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:33,526 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:34,133 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:34,133 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:34,438 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:42,107 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:42,310 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:42,911 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:43,516 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:21:49,320 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 134.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:51,448 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:21:51,449 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:21:52,632 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:21:54,838 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:21:55,804 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:21:56,849 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:21:56,852 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:21:57,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:21:58,15 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:21:59,17 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:21:59,452 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:00,19 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:00,320 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 34.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:00,454 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 108.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:04,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:08,575 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:10,380 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 147.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:22:12,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:23,80 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 64.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:24,912 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 139.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:26,22 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:26,890 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 55.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:22:30,600 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:31,703 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 72.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:22:34,611 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:38,955 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 126.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:48,603 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 245.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:52,865 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:52,868 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:52,871 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:22:52,871 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:52,873 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:22:52,875 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:22:52,877 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:22:52,878 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:22:53,93 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 276.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:53,884 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:22:53,885 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:54,86 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:54,87 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:55,904 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:56,105 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:22:56,208 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:22:56,312 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:57,767 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 220.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:22:58,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 217.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:22:59,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:22:59,959 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 58.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:00,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:00,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:00,354 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:00,383 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 263.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:02,283 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 281.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:02,373 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 70.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:04,93 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 240.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:04,290 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 235.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:07,321 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:08,29 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:08,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:23:09,344 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:16,529 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:23:16,531 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:17,199 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:17,544 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:23:17,545 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:17,641 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:18,603 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:19,747 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:19,804 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:20,608 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:22,642 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 121.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:22,864 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:23:22,865 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:22,941 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:23,143 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:23,744 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 232.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:23:24,45 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:24,58 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:24,118 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:24,346 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:24,446 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:23:26,50 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:26,927 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 240.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:27,154 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 147.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:29,961 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:30,947 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:33,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:34,768 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 266.24 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:23:35,58 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:35,782 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:23:35,783 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:36,964 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:37,680 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:38,870 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:41,620 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 276.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:42,479 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:43,307 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 286.72 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:23:44,401 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 140.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:44,702 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 144.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:23:48,793 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:49,314 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 261.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:49,624 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:50,198 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:51,516 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 58.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:55,828 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:23:55,928 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:23:57,633 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 62.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:23:58,940 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 117.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:23:59,36 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 55.68 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:03,752 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 217.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:06,843 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:12,877 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 145.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:16,664 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:17,496 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 60.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:26,246 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:26,248 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:26,251 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:26,251 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:26,253 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:24:26,254 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:24:26,257 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:24:26,258 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:24:27,367 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:27,372 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:27,376 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:27,380 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:29,192 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:29,391 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:29,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:29,593 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:31,152 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:33,116 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:33,117 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:33,318 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:33,523 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:37,616 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 271.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:40,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 72.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:40,795 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:41,495 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:41,997 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:42,500 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:44,476 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 245.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:45,697 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 248.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:49,839 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 113.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:54,768 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 113.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:56,244 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:24:56,245 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:24:57,196 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:24:57,296 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:24:58,98 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:24:58,800 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:24:59,302 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:24:59,602 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:25:00,382 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 131.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:25:03,814 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:25:05,595 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 126.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:25:11,334 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:25:13,705 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 113.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:25:14,843 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 537.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:25:17,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 111.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:25:24,331 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 284.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:25:26,373 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 71.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:25:28,780 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:25:30,484 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 57.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:25:30,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 66.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:25:33,994 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:25:36,474 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 113.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:25:48,391 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 471.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:25:52,882 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 121.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:25:54,411 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 284.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:25:56,714 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 281.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:25:59,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 58.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:02,768 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:02,771 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:26:02,774 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:26:02,775 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:02,776 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:26:02,777 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:26:02,779 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:26:02,781 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:26:03,790 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:26:03,888 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:03,888 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:03,890 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:26:05,252 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 243.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:05,703 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:05,804 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:26:05,907 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:26:06,108 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:09,955 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:26:09,955 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:10,564 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:26:10,767 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:17,350 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:17,450 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:26:18,561 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:19,166 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:26:28,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 122.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:32,766 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:26:32,768 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:26:33,783 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:26:33,783 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:26:34,484 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:26:35,287 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:26:35,893 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 547.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:26:35,989 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
PASSED                                                                   [ 88%]
------------------------------ live log teardown -------------------------------
07:26:36,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 34.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused

materialized_views_test.py::TestMaterializedViews::test_really_complex_repair 
-------------------------------- live log call ---------------------------------
07:26:37,818 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:37,902 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:26:37,903 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:37,969 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:26:37,969 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:38,145 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:26:38,145 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,211 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:26:38,211 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,304 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:38,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:26:38,388 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:26:38,455 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:38,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:26:38,634 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:26:38,701 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,793 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:38,878 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:26:38,878 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:38,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:26:38,945 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:39,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:39,85 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:26:39,85 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:39,135 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:39,219 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:26:39,219 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:39,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:39,353 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:26:39,354 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:39,404 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:39,488 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
07:26:39,488 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:26:39,538 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:26:39,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
07:26:39,623 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:27:04,190 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:27:05,983 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:27:06,989 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:27:08,896 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:27:13,9 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:27:13,998 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:27:15,16 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:27:16,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:27:21,232 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:27:21,233 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:27:23,621 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:27:25,253 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:27:26,879 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:27:28,69 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:27:28,325 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:27:29,828 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:27:31,298 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:27:31,321 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:27:32,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:34,696 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:38,454 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:27:39,108 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:39,509 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:39,509 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:27:41,614 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:45,425 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:27:45,726 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:47,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:53,566 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:27:53,594 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:27:53,595 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:54,601 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:54,649 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:27:54,849 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:55,227 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:27:55,228 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:56,334 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:56,454 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:27:56,707 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:56,861 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:27:56,862 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:27:58,68 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:27:58,139 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:27:58,314 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:27:58,316 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:59,321 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:27:59,808 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:27:59,810 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:00,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:00,74 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:00,517 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:00,816 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:01,228 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:01,289 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:28:01,290 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:01,751 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:02,398 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:03,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:04,504 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:04,604 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:05,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:05,538 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:07,435 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:08,514 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:08,639 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:09,200 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:09,301 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:09,671 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:10,2 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 60.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
07:28:12,625 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:12,957 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:14,754 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:15,918 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 58.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
07:28:16,435 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:23,77 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:25,543 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:25,713 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:26,260 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:29,493 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:30,602 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:31,375 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:32,662 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:42,287 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 58.88 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:56,65 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 56.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:56,985 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:56,987 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:56,988 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:56,990 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:28:56,991 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
07:28:56,992 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
07:28:57,628 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:58,80 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:28:58,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:28:58,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:28:58,865 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:29:00,31 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:00,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:00,433 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:29:00,519 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:29:01,322 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:02,28 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 61.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:29:02,37 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:29:02,429 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:03,512 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:29:03,953 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:04,52 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:04,353 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:29:05,1 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:29:05,340 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 62.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:06,506 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:29:06,648 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:10,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:12,276 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:13,477 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:29:27,813 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 34.24 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:28,415 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:41,268 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 124.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
07:29:54,605 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 110.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
07:29:56,884 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 133.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
PASSED                                                                   [ 90%]
materialized_views_test.py::TestMaterializedViews::test_complex_mv_select_statements 
-------------------------------- live log call ---------------------------------
07:30:03,104 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:30:03,193 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:30:03,193 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:30:03,263 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:30:03,264 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:30:03,355 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:30:03,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:30:03,440 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:30:03,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:30:03,506 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:30:03,597 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:30:03,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:30:03,682 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:30:03,748 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:30:03,749 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:30:22,174 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:30:32,30 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:30:41,396 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:30:48,995 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:30:56,903 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 91%]
materialized_views_test.py::TestMaterializedViews::test_base_view_consistency_on_failure_after_mv_apply 
-------------------------------- live log call ---------------------------------
07:31:04,847 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:31:04,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:31:04,934 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:31:05,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:31:05,3 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:31:05,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:31:05,181 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:31:05,182 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:31:05,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:31:05,251 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:31:05,344 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:31:05,429 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:31:05,429 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:31:05,497 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:31:05,498 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:31:24,997 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:31:52,43 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:31:52,46 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:31:53,258 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:31:53,842 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:31:53,844 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:31:54,950 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:31:55,165 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:31:57,155 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:31:59,578 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:32:00,765 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:32:02,361 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:32:49,42 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:32:50,634 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:32:52,229 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 93%]
materialized_views_test.py::TestMaterializedViews::test_base_view_consistency_on_failure_before_mv_apply 
-------------------------------- live log call ---------------------------------
07:33:02,450 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:33:02,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:33:02,536 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:33:02,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:33:02,604 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:33:02,698 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:33:02,783 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:33:02,783 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:33:02,851 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:33:02,851 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:33:02,944 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:33:03,29 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:33:03,29 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:33:03,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:33:03,97 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:33:23,769 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:33:50,585 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:33:50,588 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:51,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:52,393 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:33:52,394 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:53,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:53,906 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:55,505 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:58,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:33:59,116 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
07:34:00,211 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:34:46,887 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:34:48,510 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
07:34:50,146 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 95%]
materialized_views_test.py::TestMaterializedViewsConsistency::test_single_partition_consistent_reads_after_write SKIPPED [ 96%]
materialized_views_test.py::TestMaterializedViewsConsistency::test_multi_partition_consistent_reads_after_write 
-------------------------------- live log call ---------------------------------
07:35:00,283 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:35:00,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:35:00,369 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:35:00,436 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:35:00,436 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:35:00,527 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:35:00,612 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:35:00,612 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:35:00,679 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
07:35:00,679 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:35:00,770 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:35:00,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:35:00,854 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:35:00,921 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
07:35:00,921 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:35:21,793 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:35:47,545 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
07:35:47,546 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
07:35:47,547 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
07:35:47,548 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
07:35:47,565 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,566 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,567 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,567 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,571 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,574 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,575 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
07:35:47,579 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
PASSED                                                                   [ 98%]
materialized_views_test.py::TestMaterializedViewsLockcontention::test_mutations_dontblock 
-------------------------------- live log call ---------------------------------
07:40:08,931 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:40:09,18 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:40:09,19 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:40:09,86 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:40:09,86 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:40:09,142 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:40:09,227 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:40:09,227 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:40:09,279 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
07:40:09,364 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
07:40:09,364 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
07:40:15,878 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
07:40:17,718 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:40:17,719 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:40:17,722 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:40:17,755 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:40:17,755 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:40:17,764 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:40:17,764 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:40:17,765 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
07:40:17,766 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
07:40:17,769 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:40:17,792 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
07:40:17,826 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
PASSED                                                                   [100%]
===Flaky Test Report===

test_view_metadata_cleanup passed 1 out of the required 1 times. Success!
test_create passed 1 out of the required 1 times. Success!
test_gcgs_validation passed 1 out of the required 1 times. Success!
test_insert passed 1 out of the required 1 times. Success!
test_populate_mv_after_insert passed 1 out of the required 1 times. Success!
test_populate_mv_after_insert_wide_rows_version40 passed 1 out of the required 1 times. Success!
test_crc_check_chance passed 1 out of the required 1 times. Success!
test_prepared_statement passed 1 out of the required 1 times. Success!
test_immutable passed 1 out of the required 1 times. Success!
test_drop_mv passed 1 out of the required 1 times. Success!
test_drop_column passed 1 out of the required 1 times. Success!
test_drop_table passed 1 out of the required 1 times. Success!
test_clustering_column passed 1 out of the required 1 times. Success!
test_add_dc_after_mv_simple_replication passed 1 out of the required 1 times. Success!
test_add_dc_after_mv_network_replication passed 1 out of the required 1 times. Success!
test_add_node_after_mv passed 1 out of the required 1 times. Success!
test_insert_during_range_movement_rf1 passed 1 out of the required 1 times. Success!
test_insert_during_range_movement_rf2 passed 1 out of the required 1 times. Success!
test_insert_during_range_movement_rf3 passed 1 out of the required 1 times. Success!
test_add_node_after_wide_mv_with_range_deletions passed 1 out of the required 1 times. Success!
test_add_node_after_very_wide_mv passed 1 out of the required 1 times. Success!
test_add_write_survey_node_after_mv passed 1 out of the required 1 times. Success!
test_allow_filtering passed 1 out of the required 1 times. Success!
test_secondary_index passed 1 out of the required 1 times. Success!
test_ttl passed 1 out of the required 1 times. Success!
test_query_all_new_column passed 1 out of the required 1 times. Success!
test_query_new_column passed 1 out of the required 1 times. Success!
test_rename_column passed 1 out of the required 1 times. Success!
test_rename_column_atomicity passed 1 out of the required 1 times. Success!
test_lwt passed 1 out of the required 1 times. Success!
test_interrupt_build_process passed 1 out of the required 1 times. Success!
test_drop_with_stopped_build passed 1 out of the required 1 times. Success!
test_resume_stopped_build passed 1 out of the required 1 times. Success!
test_mv_with_default_ttl_with_flush passed 1 out of the required 1 times. Success!
test_mv_with_default_ttl_without_flush passed 1 out of the required 1 times. Success!
test_no_base_column_in_view_pk_complex_timestamp_with_flush passed 1 out of the required 1 times. Success!
test_base_column_in_view_pk_complex_timestamp_with_flush passed 1 out of the required 1 times. Success!
test_base_column_in_view_pk_complex_timestamp_without_flush passed 1 out of the required 1 times. Success!
test_expired_liveness_with_limit_rf1_nodes1 passed 1 out of the required 1 times. Success!
test_expired_liveness_with_limit_rf1_nodes3 passed 1 out of the required 1 times. Success!
test_expired_liveness_with_limit_rf3 passed 1 out of the required 1 times. Success!
test_base_column_in_view_pk_commutative_tombstone_with_flush passed 1 out of the required 1 times. Success!
test_base_column_in_view_pk_commutative_tombstone_without_flush passed 1 out of the required 1 times. Success!
test_view_tombstone passed 1 out of the required 1 times. Success!
test_simple_repair_by_base passed 1 out of the required 1 times. Success!
test_simple_repair_by_view passed 1 out of the required 1 times. Success!
test_base_replica_repair passed 1 out of the required 1 times. Success!
test_base_replica_repair_with_contention passed 1 out of the required 1 times. Success!
test_complex_repair passed 1 out of the required 1 times. Success!
test_throttled_partition_update passed 1 out of the required 1 times. Success!
test_really_complex_repair passed 1 out of the required 1 times. Success!
test_complex_mv_select_statements passed 1 out of the required 1 times. Success!
test_base_view_consistency_on_failure_after_mv_apply passed 1 out of the required 1 times. Success!
test_base_view_consistency_on_failure_before_mv_apply passed 1 out of the required 1 times. Success!
test_multi_partition_consistent_reads_after_write passed 1 out of the required 1 times. Success!
test_mutations_dontblock passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

============== 55 passed, 4 skipped, 1 xpassed in 6293.64 seconds ==============
[msx] rc = 0
