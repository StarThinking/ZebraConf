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
19:56:55,692 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:56:55,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:56:55,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:56:55,941 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:56:56,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:56:56,94 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:57:15,826 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:17,490 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:19,460 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:21,391 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:22,509 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:26,823 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
19:57:26,862 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
19:57:32,761 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:34,475 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:36,427 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:37,465 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:39,512 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:57:43,576 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
19:57:43,587 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  1%]
materialized_views_test.py::TestMaterializedViews::test_create 
-------------------------------- live log call ---------------------------------
19:57:50,442 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:57:50,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:57:50,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:57:50,701 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:57:50,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:57:50,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:57:50,948 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:57:51,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:57:51,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:58:09,721 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [  3%]
materialized_views_test.py::TestMaterializedViews::test_gcgs_validation 
-------------------------------- live log call ---------------------------------
19:58:11,451 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:58:11,538 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:58:11,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:58:11,703 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:58:11,790 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:58:11,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:58:11,951 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:58:12,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:58:12,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:58:31,775 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [  5%]
materialized_views_test.py::TestMaterializedViews::test_insert 
-------------------------------- live log call ---------------------------------
19:58:37,230 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:58:37,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:58:37,390 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:58:37,485 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:58:37,571 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:58:37,639 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:58:37,733 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:58:37,821 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:58:37,889 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:58:57,391 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [  6%]
materialized_views_test.py::TestMaterializedViews::test_populate_mv_after_insert 
-------------------------------- live log call ---------------------------------
19:59:10,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:59:10,127 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:59:10,198 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:59:10,290 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:59:10,376 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:59:10,444 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:59:10,537 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:59:10,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:59:10,690 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:59:36,95 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
19:59:40,268 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
19:59:42,8 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
19:59:43,710 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [  8%]
materialized_views_test.py::TestMaterializedViews::test_populate_mv_after_insert_wide_rows_version40 
-------------------------------- live log call ---------------------------------
19:59:49,746 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:59:49,832 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:59:49,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
19:59:49,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:59:50,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:59:50,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
19:59:50,240 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
19:59:50,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
19:59:50,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:01:40,966 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:01:46,94 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:01:47,903 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:01:49,629 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
XPASS                                                                    [ 10%]
materialized_views_test.py::TestMaterializedViews::test_populate_mv_after_insert_wide_rows SKIPPED [ 11%]
materialized_views_test.py::TestMaterializedViews::test_crc_check_chance 
-------------------------------- live log call ---------------------------------
20:04:37,792 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:04:37,878 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:04:37,945 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:04:38,38 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:04:38,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:04:38,190 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:04:38,282 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:04:38,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:04:38,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:04:57,73 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 13%]
materialized_views_test.py::TestMaterializedViews::test_prepared_statement 
-------------------------------- live log call ---------------------------------
20:05:00,575 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:00,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:05:00,730 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:05:00,822 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:00,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:05:00,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:05:01,70 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:01,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:05:01,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:05:20,714 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 15%]
materialized_views_test.py::TestMaterializedViews::test_immutable 
-------------------------------- live log call ---------------------------------
20:05:22,581 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:22,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:05:22,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:05:22,824 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:22,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:05:22,981 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:05:23,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:23,160 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:05:23,226 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:05:41,860 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 16%]
materialized_views_test.py::TestMaterializedViews::test_drop_mv 
-------------------------------- live log call ---------------------------------
20:05:43,332 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:43,418 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:05:43,486 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:05:43,580 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:43,665 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:05:43,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:05:43,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:05:43,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:05:43,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:06:02,338 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:06:04,126 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 18%]
materialized_views_test.py::TestMaterializedViews::test_drop_column 
-------------------------------- live log call ---------------------------------
20:06:07,600 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:07,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:06:07,756 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:06:07,872 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:07,956 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:06:08,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:06:08,116 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:08,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:06:08,268 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:06:27,793 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 20%]
materialized_views_test.py::TestMaterializedViews::test_drop_table 
-------------------------------- live log call ---------------------------------
20:06:29,113 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:29,201 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:06:29,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:06:29,365 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:29,449 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:06:29,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:06:29,609 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:29,693 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:06:29,760 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:06:48,387 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 21%]
materialized_views_test.py::TestMaterializedViews::test_clustering_column 
-------------------------------- live log call ---------------------------------
20:06:52,885 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:52,972 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:06:53,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:06:53,131 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:53,216 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:06:53,283 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:06:53,375 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:06:53,460 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:06:53,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:07:12,972 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 23%]
materialized_views_test.py::TestMaterializedViews::test_add_dc_after_mv_simple_replication 
-------------------------------- live log call ---------------------------------
20:07:25,699 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:07:25,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:07:25,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:07:25,948 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:07:26,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:07:26,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:07:26,192 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:07:26,276 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:07:26,343 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:07:45,835 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:08:02,276 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:08:02,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:08:02,443 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:09:16,826 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:09:16,917 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
20:09:16,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
PASSED                                                                   [ 25%]
materialized_views_test.py::TestMaterializedViews::test_add_dc_after_mv_network_replication 
-------------------------------- live log call ---------------------------------
20:10:38,752 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:10:38,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:10:38,905 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:10:38,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:10:39,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:10:39,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:10:39,242 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:10:39,327 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:10:39,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:10:58,677 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:11:15,90 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:11:15,188 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:11:15,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:12:28,635 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:12:28,726 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
20:12:28,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
20:13:44,231 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
20:13:45,588 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 26%]
materialized_views_test.py::TestMaterializedViews::test_add_node_after_mv 
-------------------------------- live log call ---------------------------------
20:13:59,108 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:13:59,194 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:13:59,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:13:59,354 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:13:59,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:13:59,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:13:59,609 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:13:59,694 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:13:59,761 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:14:19,406 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:14:31,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:14:31,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:14:31,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 28%]
materialized_views_test.py::TestMaterializedViews::test_insert_during_range_movement_rf1 
-------------------------------- live log call ---------------------------------
20:15:52,658 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:15:52,744 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:15:52,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:15:52,904 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:15:52,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:15:53,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:15:53,150 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:15:53,236 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:15:53,304 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:16:11,938 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:16:13,331 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:16:13,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:16:13,563 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:17:36,907 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:17:38,665 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:17:40,452 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:17:55,169 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 30%]
materialized_views_test.py::TestMaterializedViews::test_insert_during_range_movement_rf2 
-------------------------------- live log call ---------------------------------
20:18:01,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:18:01,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:18:01,942 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:18:02,35 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:18:02,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:18:02,187 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:18:02,280 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:18:02,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:18:02,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:18:21,935 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:18:22,876 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:18:22,979 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:18:23,74 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:19:44,17 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:19:45,827 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:19:47,602 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:19:49,283 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 31%]
materialized_views_test.py::TestMaterializedViews::test_insert_during_range_movement_rf3 
-------------------------------- live log call ---------------------------------
20:19:55,806 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:19:55,892 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:19:55,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:19:56,52 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:19:56,138 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:19:56,205 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:19:56,299 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:19:56,386 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:19:56,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:20:15,921 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:20:16,849 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:20:16,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:20:17,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:21:39,753 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:21:41,524 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:21:43,337 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:21:45,104 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 33%]
materialized_views_test.py::TestMaterializedViews::test_add_node_after_wide_mv_with_range_deletions 
-------------------------------- live log call ---------------------------------
20:21:50,940 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:21:51,26 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:21:51,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:21:51,186 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:21:51,271 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:21:51,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:21:51,430 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:21:51,516 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:21:51,583 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:22:10,0 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:22:46,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:22:46,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:22:46,843 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:22:46,898 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:22:46,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 35%]
materialized_views_test.py::TestMaterializedViews::test_add_node_after_very_wide_mv 
-------------------------------- live log call ---------------------------------
20:24:19,795 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:24:19,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:24:19,948 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:24:20,40 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:24:20,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:24:20,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:24:20,283 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:24:20,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:24:20,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:24:39,878 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:27:17,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:27:17,657 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:27:17,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:27:17,789 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:27:17,883 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 36%]
materialized_views_test.py::TestMaterializedViews::test_add_write_survey_node_after_mv 
-------------------------------- live log call ---------------------------------
20:32:44,851 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:32:44,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:32:45,6 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:32:45,98 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:32:45,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:32:45,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:32:45,343 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:32:45,428 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:32:45,496 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:33:03,893 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:33:15,670 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:33:15,766 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
20:33:15,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
PASSED                                                                   [ 38%]
materialized_views_test.py::TestMaterializedViews::test_allow_filtering 
-------------------------------- live log call ---------------------------------
20:34:37,464 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:34:37,549 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:34:37,617 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:34:37,711 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:34:37,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:34:37,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:34:37,958 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:34:38,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:34:38,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:34:57,575 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:34:59,366 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 40%]
materialized_views_test.py::TestMaterializedViews::test_secondary_index 
-------------------------------- live log call ---------------------------------
20:35:23,392 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:35:23,478 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:35:23,546 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:35:23,638 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:35:23,724 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:35:23,791 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:35:23,884 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:35:23,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:35:24,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:35:42,646 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 41%]
materialized_views_test.py::TestMaterializedViews::test_ttl 
-------------------------------- live log call ---------------------------------
20:35:43,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:35:43,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:35:44,58 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:35:44,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:35:44,237 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:35:44,304 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:35:44,397 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:35:44,482 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:35:44,549 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:36:03,791 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 43%]
materialized_views_test.py::TestMaterializedViews::test_query_all_new_column 
-------------------------------- live log call ---------------------------------
20:36:27,228 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:36:27,314 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:36:27,381 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:36:27,495 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:36:27,580 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:36:27,648 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:36:27,740 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:36:27,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:36:27,894 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:36:47,389 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 45%]
materialized_views_test.py::TestMaterializedViews::test_query_new_column 
-------------------------------- live log call ---------------------------------
20:37:01,37 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:37:01,124 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:37:01,192 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:37:01,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:37:01,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:37:01,437 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:37:01,531 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:37:01,615 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:37:01,682 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:37:20,145 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:37:21,913 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 46%]
materialized_views_test.py::TestMaterializedViews::test_rename_column 
-------------------------------- live log call ---------------------------------
20:37:36,606 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:37:36,692 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:37:36,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:37:36,851 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:37:36,935 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:37:37,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:37:37,96 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:37:37,185 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:37:37,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:37:56,493 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 48%]
materialized_views_test.py::TestMaterializedViews::test_rename_column_atomicity 
-------------------------------- live log call ---------------------------------
20:38:10,440 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:38:10,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:38:10,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:38:17,94 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:38:21,414 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
20:38:22,605 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:38:24,610 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:38:28,420 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 50%]
materialized_views_test.py::TestMaterializedViews::test_lwt 
-------------------------------- live log call ---------------------------------
20:38:35,463 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:38:35,549 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:38:35,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:38:35,709 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:38:35,793 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:38:35,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:38:35,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:38:36,37 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:38:36,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:38:54,755 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:39:09,480 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:11,223 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:13,5 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:27,538 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:29,188 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:30,859 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:43,377 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:44,991 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:46,646 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:58,349 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:39:59,939 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:40:01,651 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 51%]
materialized_views_test.py::TestMaterializedViews::test_interrupt_build_process 
-------------------------------- live log call ---------------------------------
20:40:06,512 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:40:06,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:40:06,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:40:06,763 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:40:06,848 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:40:06,917 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:40:07,12 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:40:07,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:40:07,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:40:07,224 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:40:07,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:40:07,362 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:40:07,447 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:40:07,499 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:40:07,584 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:41:36,622 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:41:38,673 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
20:41:39,679 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:41:41,486 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:41:45,97 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:41:51,917 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:42:09,563 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:42:44,854 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:42:57,578 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:42:57,579 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:42:57,581 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:42:58,693 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:42:58,693 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:43:00,497 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:43:00,597 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:43:04,221 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:43:05,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:43:13,348 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:43:13,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:43:23,419 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:43:44,548 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 53%]
materialized_views_test.py::TestMaterializedViews::test_drop_while_building SKIPPED [ 55%]
materialized_views_test.py::TestMaterializedViews::test_drop_with_stopped_build 
-------------------------------- live log call ---------------------------------
20:44:33,860 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:44:33,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:44:34,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:44:34,112 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:44:34,197 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:44:34,267 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:44:34,361 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:44:34,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:44:34,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:44:34,575 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:44:34,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:44:34,712 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:44:34,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:44:34,849 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:44:34,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:45:35,488 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:45:43,832 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:46:07,339 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 56%]
materialized_views_test.py::TestMaterializedViews::test_resume_stopped_build 
-------------------------------- live log call ---------------------------------
20:46:08,71 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:46:08,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:46:08,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:46:08,330 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:46:08,414 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:46:08,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:46:08,578 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:46:08,663 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:46:08,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:46:08,790 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:46:08,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:46:08,928 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:46:09,13 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:46:09,65 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:46:09,150 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:47:10,310 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:47:16,413 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:47:28,192 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
20:47:28,193 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:47:29,200 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.14 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:47:29,201 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:47:31,409 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:47:31,410 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:47:34,921 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:47:35,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:47:41,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:47:44,847 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
20:47:55,582 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:47:58,193 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:47:58,195 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:47:59,292 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:48:01,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:48:26,695 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 58%]
materialized_views_test.py::TestMaterializedViews::test_mv_with_default_ttl_with_flush 
-------------------------------- live log call ---------------------------------
20:48:27,438 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:48:27,524 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:48:27,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:48:27,698 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:48:27,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:48:27,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:48:27,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:48:28,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:48:28,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:48:28,157 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:48:28,244 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:48:28,294 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:48:28,380 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:48:28,431 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:48:28,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:48:50,56 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:48:52,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:48:54,462 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:48:56,243 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:03,404 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:05,68 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:06,692 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:13,439 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:15,40 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:16,643 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:23,178 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:24,764 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:26,368 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:39,181 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:40,851 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:42,389 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:49,143 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:50,748 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:52,354 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:49:58,821 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:00,459 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:02,96 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:08,459 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:10,104 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:11,715 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:28,627 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:50:31,406 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:33,3 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:34,557 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:41,278 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:42,881 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:44,483 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:50,866 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:52,460 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:50:54,34 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:06,420 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:08,38 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:09,595 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:16,138 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:17,733 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:19,277 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:25,705 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:27,270 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:51:28,840 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 60%]
materialized_views_test.py::TestMaterializedViews::test_mv_with_default_ttl_without_flush 
-------------------------------- live log call ---------------------------------
20:51:40,108 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:51:40,196 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:51:40,265 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:51:40,361 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:51:40,452 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:51:40,520 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:51:40,614 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:51:40,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:51:40,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:51:40,826 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:51:40,911 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:51:40,962 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:51:41,49 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:51:41,101 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:51:41,274 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:52:02,761 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:52:05,455 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:07,252 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:08,966 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:10,640 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:12,253 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:13,869 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:15,531 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:17,210 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:18,835 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:20,542 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:22,191 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:23,759 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:25,420 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:27,41 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:28,680 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:30,252 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:31,837 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:33,482 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:35,133 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:36,745 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:38,372 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:40,74 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:41,613 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:43,229 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:49,794 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:52:52,354 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:53,939 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:55,594 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:57,251 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:52:58,835 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:00,464 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:02,91 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:03,715 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:05,272 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:06,888 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:08,457 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:10,9 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:11,681 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:13,234 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:14,900 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:16,535 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:18,83 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:19,646 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 61%]
materialized_views_test.py::TestMaterializedViews::test_no_base_column_in_view_pk_complex_timestamp_with_flush 
-------------------------------- live log call ---------------------------------
20:53:20,440 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:53:20,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:53:20,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:53:20,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:53:20,776 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:53:20,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:53:20,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:53:21,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:53:21,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:53:21,149 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:53:21,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:53:21,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:53:21,457 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:53:21,509 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:53:21,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:53:42,908 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:53:46,190 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:47,964 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:49,718 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:56,941 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:53:58,583 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:00,226 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:07,60 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:08,644 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:10,257 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:16,801 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:18,420 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:20,27 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:26,557 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:28,177 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:29,734 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:36,467 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:38,73 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:39,745 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:46,245 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:47,880 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:49,464 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:55,967 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:57,614 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:54:59,140 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:05,721 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:07,268 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:08,832 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:15,229 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:16,810 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:18,434 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:24,847 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:26,365 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:27,978 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:34,541 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:36,92 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:37,671 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:44,130 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:45,740 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:47,311 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:53,561 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:55,85 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:55:56,668 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:56:23,208 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:56:24,805 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:56:26,395 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 63%]
materialized_views_test.py::TestMaterializedViews::test_no_base_column_in_view_pk_complex_timestamp_without_flush SKIPPED [ 65%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_complex_timestamp_with_flush 
-------------------------------- live log call ---------------------------------
20:56:51,957 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:56:52,44 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:56:52,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:56:52,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:56:52,294 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:56:52,449 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:56:52,543 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:56:52,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:56:52,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:56:52,752 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:56:52,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
20:56:52,888 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:56:52,974 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
20:56:53,24 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
20:56:53,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
20:57:14,614 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
20:57:18,12 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:19,824 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:21,562 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:28,858 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:30,503 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:32,98 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:38,826 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:40,452 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:42,89 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:48,684 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:50,288 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:51,934 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:57:58,530 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:00,126 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:01,725 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:14,678 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:16,292 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:17,880 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:24,600 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:26,187 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:27,803 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:34,415 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:36,27 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:37,588 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:43,877 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:45,483 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:47,50 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:53,482 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:55,90 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:58:56,657 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:59:02,963 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:59:04,514 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:59:06,91 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:59:10,962 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:12,72 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:13,979 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:15,473 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:15,474 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:16,282 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:16,283 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:16,580 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:17,390 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:17,591 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:18,384 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:18,976 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:19,596 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:19,811 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:19,812 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:19,999 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:20,279 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:20,280 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:20,817 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:21,285 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:21,549 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:21,550 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:21,928 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:21,929 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:22,94 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:22,305 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:22,556 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:23,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:23,90 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:23,135 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:23,606 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:24,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:25,40 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:25,79 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:25,80 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:25,914 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:26,176 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:26,177 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:26,286 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:26,633 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:26,647 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:26,649 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:26,917 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:27,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:27,403 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:27,654 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:27,794 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:27,795 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:28,395 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:28,529 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:59:28,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:28,853 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:28,877 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:29,19 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:29,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:29,961 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:30,125 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:30,128 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:30,496 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:30,498 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:30,921 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:31,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:31,633 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:31,706 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:31,720 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:31,726 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:31,769 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
20:59:32,92 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:32,94 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:32,208 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:32,833 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:33,1 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:33,201 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:33,241 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:33,465 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:33,815 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:34,474 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:34,504 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:34,507 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:34,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:34,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:34,940 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:35,10 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:35,612 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:35,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:36,18 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:36,19 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:36,82 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:36,83 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:36,502 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:36,874 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:37,24 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:37,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:37,188 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:37,579 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:37,581 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:37,718 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:38,230 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:38,686 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:39,194 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:39,251 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:39,322 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:39,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:40,446 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
20:59:40,448 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:40,491 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:40,737 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:41,453 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:41,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:42,80 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:42,81 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:42,227 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:42,494 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:43,87 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:43,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:43,404 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:43,462 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:43,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:43,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:44,65 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:44,67 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:45,93 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:45,103 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:45,750 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:47,40 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:47,41 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:47,871 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
20:59:47,873 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:47,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
20:59:48,47 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:48,445 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:48,474 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:48,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:49,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:50,155 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:50,985 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:51,641 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:52,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:52,389 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:53,935 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:54,136 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:54,270 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:55,97 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:56,442 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:59,209 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
20:59:59,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:00:02,276 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:00:03,77 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 66%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_complex_timestamp_without_flush 
-------------------------------- live log call ---------------------------------
21:00:09,298 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:00:09,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:00:09,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:00:09,547 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:00:09,633 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:00:09,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:00:09,801 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:00:09,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:00:09,954 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:00:10,10 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:00:10,96 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:00:10,147 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:00:10,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:00:10,283 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:00:10,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:00:31,889 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:00:35,217 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:36,999 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:38,817 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:40,521 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:42,138 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:43,707 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:45,356 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:47,7 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:48,627 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:50,280 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:51,933 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:53,585 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:55,246 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:57,30 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:00:58,632 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:06,58 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:07,708 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:09,371 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:11,51 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:12,666 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:14,273 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:15,950 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:17,574 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:19,120 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:20,728 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:22,298 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:23,877 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:25,524 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:27,115 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:28,722 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:30,372 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:31,976 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:33,551 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:33,615 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:34,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:36,734 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:36,975 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:36,976 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:37,698 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:37,699 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:38,182 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:38,904 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:40,288 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:41,47 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:41,110 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:41,620 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:42,127 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:42,128 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:42,657 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:42,658 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:42,854 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:43,133 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:43,696 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:43,698 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:43,764 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:44,261 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:44,262 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:44,701 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:44,803 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:45,160 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:45,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:45,322 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:45,468 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:45,770 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:46,908 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:46,995 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:46,997 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:47,563 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:47,564 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:47,573 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:48,2 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:48,570 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:48,616 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:48,618 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:48,947 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:49,110 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:49,112 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:49,380 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:49,624 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:49,673 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:50,9 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:50,219 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:50,274 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:50,319 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:50,483 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:51,220 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:51,530 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:51,824 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:51,888 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:51,924 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:51,925 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:52,288 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:52,290 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:52,327 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:52,791 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:01:53,133 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:53,303 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:53,576 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:53,578 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:53,724 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:53,866 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:53,868 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:54,53 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:54,293 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:54,684 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:54,937 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:55,73 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:55,309 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:55,778 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:56,143 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:56,337 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:56,388 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:57,21 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:57,23 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:57,104 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:01:57,106 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:57,179 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:58,111 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:58,229 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:58,503 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:58,622 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:58,623 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:58,710 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:01:58,712 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:58,899 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:58,915 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:59,107 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:59,445 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:59,550 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:01:59,718 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:01:59,729 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:00,218 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:00,334 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:00,599 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:00,788 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:01,144 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:01,510 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:01,523 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:01,935 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:01,964 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:02:01,966 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:03,171 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:03,541 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:02:03,542 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:03,762 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:03,828 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:04,648 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:04,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:05,277 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:05,333 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:05,460 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:05,658 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:05,946 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:06,869 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:06,954 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:07,137 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:07,320 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:02:08,792 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:02:08,794 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:09,361 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:02:09,362 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:09,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:09,800 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:09,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:10,368 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:11,384 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:11,983 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:12,184 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:13,788 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:15,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:15,294 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:15,796 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:16,195 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:16,396 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 29.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:17,96 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:18,897 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:19,8 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:02:22,312 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 68%]
materialized_views_test.py::TestMaterializedViews::test_expired_liveness_with_limit_rf1_nodes1 
-------------------------------- live log call ---------------------------------
21:02:28,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:28,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:02:28,343 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:02:28,400 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:28,485 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:02:34,972 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 70%]
materialized_views_test.py::TestMaterializedViews::test_expired_liveness_with_limit_rf1_nodes3 
-------------------------------- live log call ---------------------------------
21:02:36,413 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:36,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:02:36,568 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:02:36,662 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:36,756 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:02:36,825 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:02:36,919 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:37,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:02:37,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:02:37,129 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:37,215 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:02:37,266 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:37,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:02:37,406 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:02:37,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:02:59,51 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 71%]
materialized_views_test.py::TestMaterializedViews::test_expired_liveness_with_limit_rf3 
-------------------------------- live log call ---------------------------------
21:03:02,705 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:02,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:03:02,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:03:02,971 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:03,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:03:03,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:03:03,345 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:03,431 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:03:03,504 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:03:03,561 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:03,647 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:03:03,697 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:03,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:03:03,834 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:03,921 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:03:24,795 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 73%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_commutative_tombstone_with_flush 
-------------------------------- live log call ---------------------------------
21:03:28,613 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:28,700 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:03:28,768 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:03:28,860 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:28,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:03:29,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:03:29,103 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:29,190 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:03:29,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:03:29,312 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:29,398 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:03:29,448 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:29,533 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:03:29,583 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:03:29,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:03:51,380 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:03:59,650 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:01,357 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:03,27 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:10,445 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:12,90 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:13,708 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:20,289 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:21,984 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:23,606 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:30,207 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:31,823 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:33,477 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:40,52 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:41,668 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:43,298 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:56,327 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:58,9 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:04:59,644 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 75%]
materialized_views_test.py::TestMaterializedViews::test_base_column_in_view_pk_commutative_tombstone_without_flush 
-------------------------------- live log call ---------------------------------
21:05:05,379 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:05:05,467 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:05:05,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:05:05,628 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:05:05,713 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:05:05,781 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:05:05,874 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:05:05,960 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:05:06,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:05:06,84 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:05:06,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:05:06,230 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:05:06,315 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:05:06,365 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:05:06,451 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:05:28,170 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:05:35,950 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:37,704 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:39,326 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:41,8 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:42,630 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:44,310 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:45,943 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:47,641 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:49,258 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:50,917 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:52,544 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:54,198 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:55,888 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:57,529 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:05:59,166 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:00,819 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:02,440 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:04,81 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 76%]
materialized_views_test.py::TestMaterializedViews::test_view_tombstone 
-------------------------------- live log call ---------------------------------
21:06:04,651 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:06:04,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:06:04,888 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:06:04,981 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:06:05,66 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:06:05,132 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:06:05,224 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:06:05,308 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:06:05,375 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:06:05,430 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:06:05,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:06:05,564 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:06:05,648 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:06:05,698 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:06:05,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:06:27,520 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:06:30,159 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:31,932 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:33,697 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:35,340 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:37,1 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:38,631 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:40,258 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:41,898 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:43,531 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:43,574 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:06:44,583 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:06:46,490 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:06:50,1 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:06:53,222 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:54,889 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:06:59,234 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:01,907 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:07:01,909 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:02,914 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:05,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:06,988 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:07:06,989 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:07,995 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:09,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 78%]
materialized_views_test.py::TestMaterializedViews::test_simple_repair_by_base 
-------------------------------- live log call ---------------------------------
21:07:11,165 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:07:11,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:07:11,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:07:11,419 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:07:11,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:07:11,575 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:07:11,668 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:07:11,755 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:07:11,823 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:07:11,879 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:07:11,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:07:12,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:07:12,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:07:12,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:07:12,237 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:07:33,749 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:07:34,667 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:07:35,672 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:37,579 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:41,89 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:48,53 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:07:48,370 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:07:49,793 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:08:02,860 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 80%]
materialized_views_test.py::TestMaterializedViews::test_simple_repair_by_view 
-------------------------------- live log call ---------------------------------
21:08:42,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:08:42,777 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:08:42,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:08:42,939 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:08:43,25 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:08:43,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:08:43,198 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:08:43,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:08:43,352 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:08:43,408 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:08:43,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:08:43,578 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:08:43,663 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:08:43,714 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:08:43,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:09:05,555 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:09:06,499 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:09:07,507 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:09:09,413 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:09:13,325 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:09:19,757 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:09:21,256 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:09:21,504 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:09:35,547 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 29.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
PASSED                                                                   [ 81%]
materialized_views_test.py::TestMaterializedViews::test_base_replica_repair 
-------------------------------- live log call ---------------------------------
21:10:14,199 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:10:14,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:10:14,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:10:14,457 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:10:14,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:10:14,609 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:10:14,701 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:10:14,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:10:14,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:10:34,389 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:10:40,172 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:10:41,988 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:10:43,783 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:11:01,903 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:11:02,942 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
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
21:11:03,234 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:11:10,149 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:11:11,963 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:11:11,965 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:12,970 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:13,756 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:11:13,758 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:14,763 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:15,75 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:17,69 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:19,289 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:21,201 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:27,308 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:30,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:31,905 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:11:31,905 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:11:33,11 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:33,112 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:35,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:11:35,417 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:39,432 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:44,882 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:11:46,752 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 83%]
materialized_views_test.py::TestMaterializedViews::test_base_replica_repair_with_contention 
-------------------------------- live log call ---------------------------------
21:12:00,889 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:12:00,978 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:12:01,46 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:12:01,139 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:12:01,225 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:12:01,293 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:12:01,387 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:12:01,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:12:01,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:12:21,149 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:12:26,766 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:12:28,551 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:12:30,390 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:12:43,449 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:12:43,542 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:12:48,627 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:12:49,738 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:12:49,765 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:12:49,766 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:12:56,735 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:12:58,523 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:12:58,524 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:12:59,630 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:13:00,363 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:13:00,365 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:01,370 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:01,936 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:13:03,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:06,147 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:13:07,89 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:13,6 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:13:15,589 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:18,628 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:13:18,629 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:13:19,634 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:19,735 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:13:21,640 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:13:21,840 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:25,851 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:33,380 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:13:34,40 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
PASSED                                                                   [ 85%]
materialized_views_test.py::TestMaterializedViews::test_complex_repair 
-------------------------------- live log call ---------------------------------
21:13:53,637 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:53,724 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:13:53,792 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:13:53,885 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:53,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:13:54,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:13:54,131 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:54,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:13:54,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:13:54,378 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:54,464 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:13:54,532 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:13:54,625 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:54,711 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:13:54,788 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:13:54,846 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:54,934 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:13:54,986 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:55,74 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:13:55,127 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:55,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:13:55,265 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:55,351 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:13:55,403 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:13:55,488 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:14:19,941 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:14:22,201 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:14:23,207 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:14:25,14 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:14:29,316 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:14:29,628 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:14:30,431 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:14:32,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:14:37,149 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:14:37,551 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:14:44,151 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:16:14,193 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:16:14,196 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:16:14,198 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:16:14,199 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:16:14,200 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:16:14,201 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:16:15,208 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:16:15,209 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:16:15,311 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:16:17,20 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:16:17,425 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:16:17,529 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:16:20,759 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:16:21,262 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:16:22,63 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:16:28,722 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:16:29,524 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:16:29,825 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:16:43,365 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:16:44,868 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:16:45,370 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 29.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:17:15,153 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 60.8 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
PASSED                                                                   [ 86%]
materialized_views_test.py::TestMaterializedViews::test_throttled_partition_update 
-------------------------------- live log call ---------------------------------
21:17:42,771 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:42,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:17:42,924 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:17:43,17 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:43,102 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:17:43,170 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:17:43,263 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:43,348 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:17:43,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:17:43,508 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:43,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:17:43,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:17:43,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:43,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:17:43,907 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:17:43,963 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:44,48 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:17:44,98 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:44,182 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:17:44,233 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:44,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:17:44,369 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:44,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:17:44,504 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:17:44,589 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:18:16,650 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:18:18,879 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:18:19,885 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:18:21,792 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:18:25,504 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:18:26,891 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:18:28,13 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:18:30,319 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:18:33,126 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:18:34,430 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:18:42,358 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:18:44,354 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:18:46,46 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:18:47,742 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:18:48,183 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:18:56,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:19:10,359 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:19:11,409 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:13,615 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:16,19 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:19:16,21 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:17,227 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:17,926 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:18,372 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:19:19,132 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:19,430 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.94 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:21,436 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:23,43 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 6.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:23,142 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:19:25,350 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:25,852 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:30,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:30,672 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:19:31,878 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 62.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:19:33,81 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:42,505 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:47,716 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:19:47,718 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:48,521 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:19:48,622 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:48,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.86 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:50,829 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:19:55,342 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:20:03,364 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:20:12,987 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 65.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:20:16,196 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 56.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:20:18,603 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:20:25,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 55.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:20:48,91 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:20:53,68 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:20:54,895 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:20:56,698 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:20:58,456 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:00,276 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:05,734 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:07,350 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:08,978 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:10,598 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:12,258 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:21:14,329 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:21:14,330 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:15,336 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:17,241 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:21,653 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:23,63 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:21:23,65 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:24,174 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:24,868 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:21:24,869 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:25,974 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:26,482 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:27,880 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:28,774 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:30,664 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:21:30,666 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:31,94 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:31,672 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:32,392 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:33,477 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:35,175 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:21:35,175 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:21:35,177 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:21:35,724 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:21:35,726 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:36,281 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:36,282 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:36,381 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:36,832 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:37,341 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:21:37,342 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:37,986 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:38,90 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:38,186 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:38,387 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:38,447 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:38,938 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:38,968 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:21:38,969 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:40,74 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:40,122 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:40,252 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:40,614 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:41,997 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:42,79 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:42,298 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:42,398 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:43,49 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:44,263 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:44,907 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:45,689 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:45,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:46,22 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:21:46,23 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:21:47,129 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:21:49,435 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:21:49,616 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:50,170 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:50,920 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:51,221 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:53,289 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:53,309 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:53,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:21:56,673 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:21:56,674 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:57,170 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:21:57,679 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:21:58,428 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:21:58,429 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:21:59,66 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:21:59,435 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:21:59,786 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:00,244 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:22:00,246 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:01,351 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:01,541 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:02,375 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:03,256 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:03,355 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:03,696 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:04,357 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 32.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:22:05,176 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:22:05,176 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:22:05,178 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:05,359 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:06,52 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:06,263 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:06,263 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:06,362 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 34.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:07,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 30.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:07,869 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:08,167 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:08,228 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:22:08,368 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:10,585 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:22:10,587 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:10,754 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:10,825 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:11,592 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.82 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:12,246 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:22:12,247 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:12,278 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:12,579 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:12,970 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:13,352 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:13,498 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:14,995 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:15,558 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.48 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:17,719 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:22:17,720 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:17,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 69.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:18,110 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:18,726 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:19,699 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:19,821 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:20,69 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.28 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:20,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:21,33 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:24,744 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:25,630 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.76 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:25,746 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:27,391 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.68 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:29,275 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:29,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:30,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 28.8 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:32,965 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 13.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:33,233 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:33,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:35,500 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 63.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:22:35,640 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:35,962 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:22:36,844 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 36.8 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:37,44 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:22:37,297 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:41,256 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:22:43,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:43,475 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:44,745 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:22:46,802 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:22:48,395 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:22:59,411 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 57.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:00,97 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 62.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:01,338 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:01,340 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:01,343 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:01,344 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:01,345 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:23:01,346 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:23:01,349 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:23:01,350 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:23:01,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:02,354 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:02,458 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:02,458 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:02,459 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:04,475 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:04,576 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:04,678 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:04,781 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:08,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:08,821 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:08,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.52 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:09,125 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:11,343 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 62.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:12,143 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 63.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:13,657 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 72.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:13,868 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 72.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:15,893 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:16,505 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:17,317 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:17,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:19,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 57.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:27,704 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 111.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:30,867 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 119.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:31,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 142.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:31,336 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:23:31,337 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:31,810 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:31,810 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.0 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:23:32,102 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 122.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:32,412 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:32,512 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:33,595 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 142.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:34,217 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 33.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:34,517 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:38,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 131.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:38,931 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 112.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:23:39,29 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:46,463 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 144.64 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:47,651 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:52,645 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 124.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:23:53,764 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 130.56 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:23:54,863 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 119.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:23:57,46 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 144.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:02,261 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 131.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:03,492 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 66.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:24:03,893 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 64.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:05,799 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 34.56 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:08,205 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:08,706 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 62.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:24:10,810 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 116.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:24:13,435 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 121.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:15,517 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 138.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:16,733 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 138.24 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:26,268 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 116.48 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:26,646 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 133.12 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:37,65 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:24:37,68 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:37,71 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:37,71 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:37,73 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:24:37,74 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:24:37,76 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:24:37,78 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:24:38,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.06 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:38,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:24:38,84 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:38,86 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:39,805 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:40,7 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:24:40,208 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.52 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:40,409 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:40,419 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 65.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:43,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:43,738 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:43,938 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 9.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:24:44,853 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:51,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:24:52,18 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:24:52,627 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:24:53,131 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:25:03,330 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 108.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:25:07,62 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:25:07,64 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:07,938 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:08,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:08,549 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 131.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:25:09,546 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:25:09,546 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 27.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:25:10,148 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:10,152 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 116.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:25:10,248 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:25:10,854 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 129.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:13,957 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:19,79 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 284.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:22,381 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:29,980 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 286.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:31,611 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 250.88 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:35,16 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 256.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:35,818 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 71.04 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:37,122 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:25:37,323 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 27.84 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:41,32 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 59.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:25:42,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 71.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:25:46,350 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 142.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:50,361 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 263.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:25:53,169 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 253.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:25:53,971 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 281.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:55,744 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 281.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:25:56,881 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 235.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:03,0 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:03,3 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:03,5 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:03,6 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:03,7 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:26:03,8 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:26:03,11 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:26:03,12 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:26:04,19 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:04,19 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.88 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:04,122 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:04,122 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:04,419 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 227.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:05,209 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 70.4 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:05,936 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:06,239 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:06,343 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:06,343 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:10,92 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:10,190 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:10,495 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:10,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:11,109 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 253.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:14,163 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 266.24 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:15,71 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 238.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:17,695 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:17,900 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:18,101 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:19,517 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:21,726 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 217.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:22,757 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 294.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:32,997 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:26:32,998 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:33,796 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 253.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:33,910 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:34,211 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.28 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:26:34,212 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.74 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:34,412 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:35,15 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 286.72 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:36,16 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:36,519 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 36.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:39,627 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:39,813 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 291.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:40,621 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 113.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:26:45,33 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 135.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:46,846 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:46,938 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 111.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:26:52,157 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 240.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:53,656 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 131.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:26:56,681 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:26:56,682 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:57,788 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 2.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:26:59,994 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:01,183 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:03,804 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.64 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:05,194 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 58.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:27:06,695 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 227.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:06,899 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 54.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:07,501 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 69.12 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:12,527 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:12,715 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 61.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:27:15,615 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 128.0 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:20,231 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 258.56 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:20,431 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 273.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:30,473 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:31,958 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:31,960 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:27:31,964 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:31,964 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:31,965 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:27:31,966 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:27:31,968 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:27:31,969 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:27:32,267 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 65.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:32,979 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:33,83 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:27:33,84 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:33,85 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:35,100 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:35,100 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:27:35,300 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:35,403 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:38,525 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:27:38,824 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:39,226 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:27:39,327 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.44 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:46,598 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 17.28 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:27:46,700 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:27:46,800 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:27:47,207 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:28:00,827 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:28:00,925 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:28:01,327 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 131.84 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:28:01,930 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:28:01,956 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:28:01,958 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:03,34 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:03,533 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 145.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:28:03,835 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 35.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:28:03,936 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.52 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:28:05,39 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:08,454 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 232.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:28:08,649 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:14,170 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 112.64 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:16,675 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 136.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:28:16,675 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:33,820 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:28:34,521 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 68.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:28:34,625 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 271.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:28:37,229 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 67.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:28:37,630 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 113.92 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:28:38,335 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 261.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:28:39,135 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 57.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:28:39,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:00,792 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 243.2 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:05,504 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 289.28 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:08,681 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.3:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:08,684 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:08,687 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.2:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:08,688 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:08,689 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:29:08,690 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:29:08,692 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:29:08,693 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:29:09,701 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:09,723 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 71.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:09,802 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.3 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:09,802 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.02 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:09,902 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:11,412 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:11,917 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:11,918 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:12,115 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:14,545 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 142.08 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:15,554 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 8.16 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:15,654 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:15,756 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:15,858 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:22,725 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:23,632 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 217.6 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:23,730 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 14.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:24,33 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 17.44 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:24,233 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:36,539 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 116.48 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:36,739 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 120.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:29:38,460 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 35.84 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:29:38,680 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:29:38,681 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:29:39,864 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:29:41,67 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:41,67 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:41,568 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.72 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:29:41,668 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:29:42,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 552.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:43,55 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 126.72 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:29:45,161 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 145.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:29:45,679 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 9.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
PASSED                                                                   [ 88%]
materialized_views_test.py::TestMaterializedViews::test_really_complex_repair 
-------------------------------- live log call ---------------------------------
21:29:51,468 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:51,554 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:29:51,622 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:29:51,715 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:51,801 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:29:51,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:29:52,38 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:52,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:29:52,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:29:52,281 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:52,365 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:29:52,432 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:29:52,523 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:52,608 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:29:52,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:29:52,730 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:52,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:29:52,865 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:52,949 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:29:53,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:53,85 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:29:53,135 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:53,219 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node4
21:29:53,269 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:29:53,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node5
21:30:19,359 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:30:21,172 cassandra.cluster WARNING Host 127.0.0.2:9042 has been marked down
21:30:22,201 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:30:24,209 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:30:27,720 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 7.76 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:30:29,185 cassandra.cluster WARNING Host 127.0.0.3:9042 has been marked down
21:30:30,229 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 1.9 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:30:32,134 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 3.56 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:30:35,543 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:30:35,743 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 7.6 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:30:43,363 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 16.96 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:30:46,945 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:30:48,664 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:30:49,485 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:30:50,475 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:30:52,136 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:30:53,789 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:30:55,453 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:30:55,471 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:30:56,526 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:30:58,531 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.4 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:00,336 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 34.24 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:31:01,941 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:02,599 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:31:03,645 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:05,650 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:09,661 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:09,761 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 7.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:11,704 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:31:12,770 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:14,975 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.0 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:16,880 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.32 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:16,909 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:31:16,910 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:18,16 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:18,636 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:31:18,638 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:18,988 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 7.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:19,726 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:19,745 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:20,452 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:31:20,455 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:21,556 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:21,562 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.08 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:22,125 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:31:22,127 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:23,233 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.78 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:23,668 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.64 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:23,778 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:31:23,778 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:23,938 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.12 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:24,884 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 2.12 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:25,37 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:25,65 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:25,443 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:31:25,444 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:26,14 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.2:9042, scheduling retry in 55.04 seconds: [Errno 111] Tried connecting to [('127.0.0.2', 9042)]. Last error: Connection refused
21:31:26,215 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:26,449 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 1.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:27,90 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 3.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:27,318 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 31.36 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:27,377 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.56 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:28,454 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 3.6 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:28,647 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:31,101 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:31,155 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 17.92 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:32,64 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.96 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:33,234 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:34,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 13.92 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:34,638 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.3:9042, scheduling retry in 62.72 seconds: [Errno 111] Tried connecting to [('127.0.0.3', 9042)]. Last error: Connection refused
21:31:36,0 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 15.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:36,668 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 16.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:39,623 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 16.0 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:41,88 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:44,664 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 32.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:48,23 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 31.04 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:49,102 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 28.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:51,440 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 36.48 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:31:53,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 33.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:55,664 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 30.4 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:31:58,701 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 61.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:31:59,536 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 27.2 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:03,714 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 56.96 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:15,402 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:15,404 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.5:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:15,406 cassandra.cluster WARNING Failed to create connection pool for new host 127.0.0.4:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3175, in cassandra.cluster.Session.add_or_renew_pool.run_add_or_renew_pool
  File "cassandra/pool.py", line 402, in cassandra.pool.HostConnection.__init__
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:15,407 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:32:15,408 cassandra.cluster WARNING Host 127.0.0.5:9042 has been marked down
21:32:15,409 cassandra.cluster WARNING Host 127.0.0.4:9042 has been marked down
21:32:16,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:16,414 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 1.7 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:16,513 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 2.26 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:17,51 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 65.92 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:17,336 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:32:17,681 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:18,121 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 4.36 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:18,221 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:18,823 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 4.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:19,117 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 73.6 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:19,121 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:32:20,767 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:32:21,731 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:22,406 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:32:22,548 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 8.08 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:23,150 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 8.32 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:24,11 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:32:25,595 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:32:26,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 67.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:26,817 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 63.36 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:27,119 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 61.44 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:27,948 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 59.52 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:30,267 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 18.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:32:30,670 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 15.52 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:31,476 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 18.4 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:32:46,213 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 28.16 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
21:32:49,924 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.5:9042, scheduling retry in 29.44 seconds: [Errno 111] Tried connecting to [('127.0.0.5', 9042)]. Last error: Connection refused
21:33:00,677 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.4:9042, scheduling retry in 147.2 seconds: [Errno 111] Tried connecting to [('127.0.0.4', 9042)]. Last error: Connection refused
PASSED                                                                   [ 90%]
materialized_views_test.py::TestMaterializedViews::test_complex_mv_select_statements 
-------------------------------- live log call ---------------------------------
21:33:22,729 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:33:22,815 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:33:22,883 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:33:22,976 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:33:23,114 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:33:23,183 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:33:23,275 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:33:23,360 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:33:23,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:33:42,394 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:33:50,776 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:34:00,144 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:34:08,135 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:34:16,654 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 91%]
materialized_views_test.py::TestMaterializedViews::test_base_view_consistency_on_failure_after_mv_apply 
-------------------------------- live log call ---------------------------------
21:34:24,708 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:34:24,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:34:24,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:34:24,957 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:34:25,43 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:34:25,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:34:25,205 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:34:25,290 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:34:25,359 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:34:44,269 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:35:12,396 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:35:13,118 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:35:13,118 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:35:13,506 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:35:14,224 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 1.98 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:35:15,714 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:35:16,229 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.2 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:35:19,626 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 7.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:35:20,767 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:36:07,760 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:36:09,478 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:36:11,252 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 93%]
materialized_views_test.py::TestMaterializedViews::test_base_view_consistency_on_failure_before_mv_apply 
-------------------------------- live log call ---------------------------------
21:36:21,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:36:21,646 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:36:21,715 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:36:21,809 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:36:21,895 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:36:21,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:36:22,58 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:36:22,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:36:22,212 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:36:41,886 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:37:10,237 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:37:10,940 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:37:10,941 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:11,245 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.22 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:11,946 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:13,553 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.68 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:14,152 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:17,264 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:18,420 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
21:37:18,422 cassandra.cluster WARNING [control connection] Error connecting to 127.0.0.1:9042:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 3522, in cassandra.cluster.ControlConnection._reconnect_internal
  File "cassandra/cluster.py", line 3544, in cassandra.cluster.ControlConnection._try_connect
  File "cassandra/cluster.py", line 1620, in cassandra.cluster.Cluster.connection_factory
  File "cassandra/connection.py", line 831, in cassandra.connection.Connection.factory
  File "/users/masix/dtest/src/cassandra-driver/cassandra/io/libevreactor.py", line 267, in __init__
    self._connect_socket()
  File "cassandra/connection.py", line 898, in cassandra.connection.Connection._connect_socket
ConnectionRefusedError: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:37:18,464 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 6.8 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
21:38:05,529 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:38:07,244 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
21:38:09,39 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 95%]
materialized_views_test.py::TestMaterializedViewsConsistency::test_single_partition_consistent_reads_after_write SKIPPED [ 96%]
materialized_views_test.py::TestMaterializedViewsConsistency::test_multi_partition_consistent_reads_after_write 
-------------------------------- live log call ---------------------------------
21:38:19,187 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:38:19,274 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:38:19,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:38:19,436 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:38:19,522 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:38:19,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
21:38:19,683 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:38:19,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:38:19,837 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
21:38:42,239 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
21:38:54,275 cassandra.cluster WARNING Node 127.0.0.2:9042 is reporting a schema disagreement: None
21:39:07,126 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
21:39:07,127 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
21:39:07,128 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
21:39:07,130 cassandra.cluster WARNING Cluster.__init__ called with contact_points specified, but no load_balancing_policy. In the next major version, this will raise an error; please specify a load-balancing policy. (contact_points = ['127.0.0.2'], lbp = None)
21:39:07,147 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,147 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,148 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,149 cassandra.cluster WARNING Downgrading core protocol version from 66 to 65 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,154 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,156 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,158 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
21:39:07,161 cassandra.cluster WARNING Downgrading core protocol version from 65 to 5 for 127.0.0.2:9042. To avoid this, it is best practice to explicitly set Cluster(protocol_version) to the version supported by your cluster. http://datastax.github.io/python-driver/api/cassandra/cluster.html#cassandra.cluster.Cluster.protocol_version
PASSED                                                                   [ 98%]
materialized_views_test.py::TestMaterializedViewsLockcontention::test_mutations_dontblock 
-------------------------------- live log call ---------------------------------
21:43:27,4 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:43:27,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:43:27,161 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:43:27,217 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:43:27,302 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:43:27,356 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
21:43:27,441 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
21:43:34,138 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
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

============== 55 passed, 4 skipped, 1 xpassed in 6407.19 seconds ==============
[msx] rc = 0
