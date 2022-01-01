cassandra paging_test.py true true
the_test is paging_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 57 items

paging_test.py::TestPagingSize::test_with_no_results 
-------------------------------- live log call ---------------------------------
08:00:47,331 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:00:47,419 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:00:47,420 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:00:47,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:00:47,489 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:00:47,581 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:00:47,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:00:47,667 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:00:47,733 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:00:47,734 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:00:47,825 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:00:47,911 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:00:47,911 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:00:47,977 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:00:47,977 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  1%]
paging_test.py::TestPagingSize::test_with_less_results_than_page_size 
-------------------------------- live log call ---------------------------------
08:01:07,827 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:07,916 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:01:07,916 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:07,983 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:01:07,983 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:08,74 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:08,160 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:01:08,160 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:08,226 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:01:08,226 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:08,317 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:08,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:01:08,402 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:08,467 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:01:08,467 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  3%]
paging_test.py::TestPagingSize::test_with_more_results_than_page_size 
-------------------------------- live log call ---------------------------------
08:01:28,75 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:28,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:01:28,162 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:28,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:01:28,229 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:28,320 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:28,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:01:28,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:28,472 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:01:28,472 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:28,563 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:28,648 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:01:28,648 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:28,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:01:28,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  5%]
paging_test.py::TestPagingSize::test_with_equal_results_to_page_size 
-------------------------------- live log call ---------------------------------
08:01:48,835 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:48,926 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:01:48,926 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:48,993 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:01:48,994 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:49,85 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:49,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:01:49,172 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:49,238 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:01:49,238 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:49,329 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:01:49,414 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:01:49,414 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:01:49,480 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:01:49,480 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  7%]
paging_test.py::TestPagingSize::test_undefined_page_size_default 
-------------------------------- live log call ---------------------------------
08:02:08,312 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:08,399 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:02:08,399 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:08,465 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:02:08,466 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:08,557 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:08,643 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:02:08,643 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:08,709 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:02:08,709 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:08,801 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:08,886 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:02:08,886 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:08,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:02:08,952 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  8%]
paging_test.py::TestPagingWithModifiers::test_with_order_by 
-------------------------------- live log call ---------------------------------
08:02:29,830 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:29,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:02:29,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:29,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:02:29,990 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:30,81 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:30,167 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:02:30,167 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:30,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:02:30,234 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:30,324 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:30,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:02:30,434 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:30,501 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:02:30,501 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 10%]
paging_test.py::TestPagingWithModifiers::test_with_order_by_reversed 
-------------------------------- live log call ---------------------------------
08:02:51,72 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:51,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:02:51,159 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:51,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:02:51,225 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:51,315 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:51,400 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:02:51,400 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:51,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:02:51,466 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:51,556 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:02:51,641 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:02:51,641 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:02:51,707 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:02:51,707 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 12%]
paging_test.py::TestPagingWithModifiers::test_with_limit 
-------------------------------- live log call ---------------------------------
08:03:11,573 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:11,658 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:03:11,659 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:11,725 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:03:11,725 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:11,816 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:11,901 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:03:11,901 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:11,967 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:03:11,968 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:12,59 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:12,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:03:12,144 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:12,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:03:12,215 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 14%]
paging_test.py::TestPagingWithModifiers::test_with_allow_filtering 
-------------------------------- live log call ---------------------------------
08:03:34,845 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:34,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:03:34,931 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:34,997 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:03:34,998 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:35,89 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:35,174 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:03:35,174 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:35,240 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:03:35,241 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:35,332 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:35,421 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:03:35,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:35,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:03:35,489 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 15%]
paging_test.py::TestPagingData::test_paging_a_single_wide_row 
-------------------------------- live log call ---------------------------------
08:03:54,589 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:54,676 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:03:54,676 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:54,742 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:03:54,742 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:54,833 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:54,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:03:54,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:54,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:03:54,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:55,78 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:03:55,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:03:55,167 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:03:55,233 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:03:55,233 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 17%]
paging_test.py::TestPagingData::test_paging_across_multi_wide_rows 
-------------------------------- live log call ---------------------------------
08:04:18,250 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:04:18,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:04:18,336 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:18,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:04:18,402 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:18,492 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:04:18,577 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:04:18,578 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:18,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:04:18,668 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:18,761 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:04:18,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:04:18,846 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:18,912 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:04:18,912 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 19%]
paging_test.py::TestPagingData::test_paging_using_secondary_indexes 
-------------------------------- live log call ---------------------------------
08:04:41,388 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:04:41,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:04:41,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:41,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:04:41,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:41,631 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:04:41,716 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:04:41,717 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:41,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:04:41,783 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:41,873 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:04:41,958 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:04:41,958 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:04:42,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:04:42,23 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 21%]
paging_test.py::TestPagingData::test_paging_with_in_orderby_and_two_partition_keys 
-------------------------------- live log call ---------------------------------
08:05:02,417 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:02,503 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:05:02,503 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:02,569 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:05:02,570 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:02,661 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:02,746 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:05:02,746 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:02,812 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:05:02,812 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:02,903 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:02,987 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:05:02,987 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:03,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:05:03,53 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
paging_test.py::TestPagingData::test_group_by_paging 
-------------------------------- live log call ---------------------------------
08:05:22,920 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:23,7 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:05:23,8 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:23,74 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:05:23,75 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:23,166 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:23,252 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:05:23,252 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:23,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:05:23,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:23,409 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:23,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:05:23,494 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:23,560 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:05:23,560 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:42,125 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,192 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,278 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,300 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,318 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,356 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,380 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,396 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,430 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,463 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,484 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,507 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,521 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,547 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,567 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,585 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,612 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,645 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,667 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,686 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,710 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,726 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,753 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,774 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,802 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,833 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,862 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,890 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,912 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,941 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,960 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:42,983 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,11 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,28 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,48 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,71 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,90 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,110 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,135 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,156 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,179 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,203 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,216 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,240 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:43,621 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,641 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,660 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,669 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,696 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,709 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,723 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,740 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,754 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,767 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,779 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,791 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,804 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,816 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,823 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,837 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,851 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,862 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,875 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,889 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,896 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,909 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,919 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,927 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,940 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,952 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,963 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,976 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:43,991 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:44,21 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,34 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,51 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,69 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,94 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,112 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,139 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,163 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,180 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,189 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,206 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,219 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,240 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,262 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,282 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,298 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,326 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,354 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,388 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,400 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,423 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,447 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,474 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,496 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,522 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,548 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,574 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,602 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,611 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,633 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,653 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,663 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,681 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:44,925 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:44,939 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:44,948 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:44,965 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:44,980 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:44,991 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,6 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,19 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,31 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,41 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,54 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,61 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,73 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,85 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,94 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,106 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,120 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,131 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,142 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,154 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,162 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,172 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,182 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,202 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,219 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,232 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,250 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,266 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,285 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,305 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,317 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,332 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,342 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,359 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,386 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,405 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,422 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,442 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,459 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,489 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,509 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,531 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,547 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,569 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,585 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,602 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,619 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,644 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,661 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,686 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,696 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,716 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:45,917 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,927 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,938 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,950 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,961 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,970 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,979 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:45,990 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,0 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,12 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,23 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,31 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,42 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,54 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,64 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,71 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,82 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,90 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,99 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,109 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,124 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,139 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,149 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,162 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,175 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,193 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,213 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,224 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,240 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,249 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,264 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,280 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,291 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,301 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,328 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,337 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,363 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,384 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,415 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,443 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,452 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,477 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,486 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,517 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,535 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,552 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,561 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,578 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,734 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,744 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,757 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,770 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,781 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,793 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,800 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,809 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,819 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,831 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,843 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,852 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,864 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,874 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,886 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,893 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,906 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,913 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,923 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,932 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:46,949 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,967 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,983 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:46,996 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,12 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,32 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,47 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,59 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,75 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,86 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,97 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,126 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,154 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,171 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,195 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,219 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,245 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,269 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,287 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,305 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,314 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,332 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,489 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,502 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,514 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,525 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,541 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,551 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,562 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,573 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,582 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,594 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,605 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,615 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,627 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,636 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,643 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:47,657 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,674 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,687 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,700 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,716 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,735 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,745 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,757 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,771 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,782 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,793 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,817 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,841 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,863 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,888 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,910 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,937 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,961 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,977 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:47,993 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:48,2 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:48,17 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:05:48,163 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,175 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,187 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,197 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,208 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,218 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,228 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,237 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,246 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,256 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,266 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,275 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,285 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,293 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:05:48,300 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
PASSED                                                                   [ 24%]
paging_test.py::TestPagingData::test_group_by_with_range_name_query_paging 
-------------------------------- live log call ---------------------------------
08:05:48,969 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:49,55 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:05:49,55 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:49,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:05:49,122 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:49,213 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:49,298 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:05:49,298 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:49,365 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:05:49,365 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:49,456 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:05:49,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:05:49,542 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:05:49,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:05:49,642 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:09,183 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,259 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,350 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,379 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,410 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,440 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,470 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,486 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,515 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,540 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,570 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,599 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,628 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,652 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,688 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,720 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,754 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,789 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,816 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,844 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,884 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,914 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,927 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,955 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,966 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:09,987 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,11 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,25 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,51 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,65 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,88 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,115 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,153 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,169 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,216 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,237 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,276 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,293 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,322 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,342 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,361 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,385 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,406 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,427 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,446 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,464 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,497 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,534 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,564 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,594 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,616 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,638 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,659 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,673 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,693 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,709 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,729 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,768 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,804 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,840 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,864 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,881 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,898 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,917 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,933 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,954 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:10,969 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,5 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,41 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,77 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,99 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,116 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,132 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,154 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,170 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,186 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,200 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,234 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,270 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,303 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:11,323 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 26%]
paging_test.py::TestPagingData::test_group_by_with_static_columns_paging 
-------------------------------- live log call ---------------------------------
08:06:12,0 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:06:12,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:06:12,92 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:12,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:06:12,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:12,295 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:06:12,382 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:06:12,382 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:12,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:06:12,449 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:12,539 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:06:12,624 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:06:12,624 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:12,690 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:06:12,690 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:31,765 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,849 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,901 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,918 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,943 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,957 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,975 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:31,990 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,25 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,41 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,68 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,97 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,129 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,142 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,170 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,296 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,315 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,336 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,351 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,372 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,385 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,398 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,412 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,434 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,448 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,462 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,483 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,503 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,517 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,538 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,557 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,571 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,588 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,602 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,624 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,639 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,653 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,666 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,689 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,712 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,725 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,754 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,782 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,793 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,819 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:32,921 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,940 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,958 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,977 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:32,990 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,7 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,27 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,46 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,64 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,78 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,98 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,120 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,141 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,161 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,177 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,189 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,207 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,232 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,257 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,282 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,293 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,317 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,408 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,425 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,442 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,458 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,471 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,488 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,505 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,520 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,537 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,548 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,563 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,579 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,597 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,612 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,627 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,638 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,653 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,675 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,698 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,720 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,730 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,749 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:33,840 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,859 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,874 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,888 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,901 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,916 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,932 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,948 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,963 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,974 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:33,988 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,4 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,19 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,34 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,48 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,58 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,73 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,95 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,116 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,139 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,149 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,171 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,253 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,270 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,285 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,300 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,312 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,326 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,342 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,356 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,371 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,382 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,397 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,411 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,426 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,439 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,451 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,462 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,476 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,495 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,515 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,534 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,544 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,564 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,645 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,660 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,675 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,688 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,699 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,713 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,727 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,740 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,756 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,767 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,781 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:34,909 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,929 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,939 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,963 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,981 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:34,999 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,7 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,45 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,68 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,83 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,113 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,149 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,165 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,173 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,195 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,213 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,230 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,238 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,264 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,295 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,320 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,343 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,368 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,383 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,390 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,413 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,445 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,467 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,475 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,495 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,513 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,521 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,539 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,557 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,564 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,582 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,599 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,618 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,636 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,658 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,668 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,688 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:35,855 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,868 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,877 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,889 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,902 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,914 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,923 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,943 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,956 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,968 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:35,984 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,1 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,14 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,23 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,35 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,46 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,58 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,66 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,82 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,104 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,119 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,132 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,143 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,154 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,162 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,179 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,189 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,201 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,211 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,221 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,228 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,242 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,252 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,266 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,281 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,289 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,301 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,310 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,331 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,342 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,356 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:36,381 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,393 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,410 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,424 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,432 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,452 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,468 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,486 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,515 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,525 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,540 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,553 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,559 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,578 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,598 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,619 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,634 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,647 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,655 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,676 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,706 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,731 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,743 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,769 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,781 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,807 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,817 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,838 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,858 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,877 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,887 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:36,908 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,37 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,46 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,59 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,70 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,78 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,96 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,109 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,124 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,137 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,145 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,156 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,167 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,173 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,184 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,200 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,211 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,221 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,231 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,239 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,251 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,260 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,271 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,282 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,289 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,300 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,307 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,320 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,330 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,340 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,353 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,362 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,375 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,392 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,399 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,414 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,426 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,443 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,456 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,473 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,491 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,497 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,510 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,522 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,537 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,555 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,569 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,582 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,593 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,613 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,628 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,652 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,659 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,686 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,694 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,718 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,734 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,753 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,774 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,783 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,802 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:37,928 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,937 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,947 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,956 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,970 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,983 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:37,996 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,8 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,14 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,24 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,34 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,44 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,59 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,69 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,79 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,89 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,103 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,114 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,123 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,144 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,157 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,171 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,182 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,194 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,202 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,213 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,228 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,244 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,253 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,267 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,279 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,294 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,311 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,326 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,335 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,350 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,364 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,380 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,392 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,402 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,429 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,444 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,472 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,497 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,524 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,540 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,562 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,583 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,592 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,614 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:38,734 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,745 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,754 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,768 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,782 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,797 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,809 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,820 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,827 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,835 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,849 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,856 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,865 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,872 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,885 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,896 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,903 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,916 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,927 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,938 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,946 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,956 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,965 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,975 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:38,990 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,6 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,18 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,31 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,47 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,70 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,86 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,97 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,111 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,122 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,136 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,161 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,187 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,214 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,240 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,253 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,269 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,289 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,297 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,318 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,434 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,447 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,459 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,472 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,484 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,494 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,507 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,516 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,527 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,536 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,547 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,558 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,570 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,582 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,593 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,604 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,613 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,625 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,634 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,645 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:39,658 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,671 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,684 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,697 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,712 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,728 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,740 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,752 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,765 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,775 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,787 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,810 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,836 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,862 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,883 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,896 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,914 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,931 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,939 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:39,957 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
08:06:40,66 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,77 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,87 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,99 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,110 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,122 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,132 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,142 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,153 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,161 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,173 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,183 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,195 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,205 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,215 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,225 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,234 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,245 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,253 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
08:06:40,263 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
PASSED                                                                   [ 28%]
paging_test.py::TestPagingData::test_static_columns_paging 
-------------------------------- live log call ---------------------------------
08:06:40,818 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:06:40,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:06:40,904 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:40,971 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:06:40,971 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:41,62 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:06:41,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:06:41,147 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:41,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:06:41,213 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:41,304 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:06:41,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:06:41,389 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:06:41,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:06:41,455 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 29%]
paging_test.py::TestPagingData::test_paging_using_secondary_indexes_with_static_cols 
-------------------------------- live log call ---------------------------------
08:07:11,905 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:11,992 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:07:11,992 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:12,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:07:12,59 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:12,150 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:12,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:07:12,235 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:12,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:07:12,302 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:12,393 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:12,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:07:12,507 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:12,574 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:07:12,575 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 31%]
paging_test.py::TestPagingData::test_static_columns_with_empty_non_static_columns_paging 
-------------------------------- live log call ---------------------------------
08:07:33,711 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:33,797 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:07:33,797 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:33,863 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:07:33,863 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:33,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:34,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:07:34,39 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:34,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:07:34,105 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:34,196 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:34,280 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:07:34,281 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:34,346 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:07:34,346 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
paging_test.py::TestPagingData::test_select_in_clause_with_duplicate_keys 
-------------------------------- live log call ---------------------------------
08:07:54,706 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:54,792 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:07:54,792 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:54,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:07:54,859 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:54,949 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:55,35 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:07:55,36 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:55,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:07:55,102 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:55,193 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:07:55,278 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:07:55,278 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:07:55,344 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:07:55,344 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 35%]
paging_test.py::TestPagingData::test_paging_with_filtering 
-------------------------------- live log call ---------------------------------
08:08:15,454 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:15,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:08:15,540 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:15,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:08:15,606 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:15,698 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:15,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:08:15,784 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:15,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:08:15,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:15,940 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:16,26 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:08:16,26 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:16,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:08:16,92 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_counter_columns 
-------------------------------- live log call ---------------------------------
08:08:37,712 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:37,798 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:08:37,798 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:37,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:08:37,864 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:37,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:38,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:08:38,40 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:38,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:08:38,130 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:38,222 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:38,308 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:08:38,308 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:38,373 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:08:38,374 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 38%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_counter_columns_compact SKIPPED [ 40%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_clustering_columns 
-------------------------------- live log call ---------------------------------
08:08:59,530 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:59,617 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:08:59,617 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:59,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:08:59,683 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:59,773 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:08:59,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:08:59,858 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:08:59,924 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:08:59,924 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:00,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:00,103 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:09:00,104 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:00,171 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:09:00,171 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 42%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_clustering_columns_compact SKIPPED [ 43%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_clustering_columns_with_contains 
-------------------------------- live log call ---------------------------------
08:09:21,593 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:21,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:09:21,681 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:21,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:09:21,747 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:21,838 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:21,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:09:21,923 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:21,989 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:09:21,989 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:22,80 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:22,165 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:09:22,165 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:22,231 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:09:22,231 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 45%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_static_columns 
-------------------------------- live log call ---------------------------------
08:09:45,602 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:45,688 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:09:45,688 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:45,755 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:09:45,755 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:45,850 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:45,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:09:45,937 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:46,3 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:09:46,3 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:46,95 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:09:46,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:09:46,180 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:09:46,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:09:46,247 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 47%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key 
-------------------------------- live log call ---------------------------------
08:10:06,369 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:06,457 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:10:06,458 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:06,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:10:06,525 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:06,617 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:06,702 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:10:06,702 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:06,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:10:06,769 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:06,861 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:06,946 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:10:06,946 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:07,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:10:07,12 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 49%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_with_limit 
-------------------------------- live log call ---------------------------------
08:10:28,661 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:28,748 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:10:28,748 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:28,814 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:10:28,815 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:28,906 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:28,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:10:28,992 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:29,58 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:10:29,58 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:29,160 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:29,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:10:29,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:29,313 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:10:29,313 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_counter_columns 
-------------------------------- live log call ---------------------------------
08:10:48,892 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:48,980 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:10:48,980 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:49,47 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:10:49,47 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:49,138 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:49,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:10:49,224 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:49,290 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:10:49,290 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:49,381 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:10:49,466 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:10:49,466 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:10:49,532 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:10:49,532 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 52%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_counter_columns_compact SKIPPED [ 54%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_clustering_columns 
-------------------------------- live log call ---------------------------------
08:11:10,989 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:11,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:11:11,75 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:11,141 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:11:11,141 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:11,232 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:11,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:11:11,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:11,384 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:11:11,384 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:11,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:11,560 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:11:11,560 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:11,626 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:11:11,626 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 56%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_clustering_columns_compact SKIPPED [ 57%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_clustering_columns_with_contains 
-------------------------------- live log call ---------------------------------
08:11:33,581 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:33,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:11:33,667 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:33,733 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:11:33,734 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:33,824 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:33,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:11:33,913 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:33,981 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:11:33,981 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:34,72 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:34,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:11:34,157 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:34,223 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:11:34,223 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 59%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_static_columns 
-------------------------------- live log call ---------------------------------
08:11:58,340 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:58,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:11:58,426 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:58,495 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:11:58,496 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:58,589 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:58,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:11:58,674 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:58,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:11:58,741 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:58,832 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:11:58,918 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:11:58,918 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:11:58,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:11:58,984 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 61%]
paging_test.py::TestPagingData::test_paging_on_compact_table_with_tombstone_on_first_column SKIPPED [ 63%]
paging_test.py::TestPagingData::test_paging_with_no_clustering_columns 
-------------------------------- live log call ---------------------------------
08:12:20,152 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:12:20,239 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:12:20,239 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:20,306 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:12:20,306 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:20,397 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:12:20,482 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:12:20,482 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:20,548 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:12:20,548 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:20,639 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:12:20,725 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:12:20,725 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:20,791 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:12:20,791 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 64%]
paging_test.py::TestPagingData::test_paging_with_no_clustering_columns_compact SKIPPED [ 66%]
paging_test.py::TestPagingData::test_per_partition_limit_paging 
-------------------------------- live log call ---------------------------------
08:12:42,480 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:12:42,566 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:12:42,566 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:42,632 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:12:42,632 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:42,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:12:42,809 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:12:42,810 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:42,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:12:42,876 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:42,967 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:12:43,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:12:43,53 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:12:43,118 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:12:43,119 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 68%]
paging_test.py::TestPagingData::test_paging_for_range_name_queries 
-------------------------------- live log call ---------------------------------
08:13:04,491 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:04,577 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:13:04,577 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:04,644 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:13:04,644 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:04,735 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:04,821 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:13:04,821 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:04,887 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:13:04,887 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:04,978 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:05,63 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:13:05,63 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:05,129 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:13:05,129 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 70%]
paging_test.py::TestPagingData::test_paging_for_range_name_queries_compact SKIPPED [ 71%]
paging_test.py::TestPagingData::test_paging_with_empty_row_and_empty_static_columns 
-------------------------------- live log call ---------------------------------
08:13:25,559 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:25,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:13:25,674 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:25,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:13:25,741 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:25,832 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:25,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:13:25,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:25,984 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:13:25,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:26,75 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:26,162 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:13:26,163 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:26,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:13:26,229 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 73%]
paging_test.py::TestPagingDatasetChanges::test_data_change_impacting_earlier_page 
-------------------------------- live log call ---------------------------------
08:13:46,580 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:46,666 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:13:46,666 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:46,732 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:13:46,733 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:46,823 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:46,909 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:13:46,909 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:46,975 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:13:46,975 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:47,69 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:13:47,156 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:13:47,156 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:13:47,223 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:13:47,223 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
paging_test.py::TestPagingDatasetChanges::test_data_change_impacting_later_page 
-------------------------------- live log call ---------------------------------
08:14:07,336 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:14:07,422 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:14:07,422 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:07,488 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:14:07,488 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:07,579 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:14:07,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:14:07,668 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:07,734 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:14:07,734 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:07,825 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:14:07,910 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:14:07,910 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:07,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:14:07,976 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 77%]
paging_test.py::TestPagingDatasetChanges::test_row_TTL_expiry_during_paging 
-------------------------------- live log call ---------------------------------
08:14:28,353 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:14:28,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:14:28,440 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:28,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:14:28,506 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:28,597 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:14:28,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:14:28,683 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:28,748 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:14:28,749 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:28,840 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:14:28,925 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:14:28,925 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:14:28,990 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:14:28,990 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 78%]
paging_test.py::TestPagingDatasetChanges::test_cell_TTL_expiry_during_paging 
-------------------------------- live log call ---------------------------------
08:15:03,650 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:15:03,740 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:15:03,741 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:03,809 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:15:03,809 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:03,900 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:15:03,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:15:03,985 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:04,51 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:15:04,51 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:04,141 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:15:04,230 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:15:04,230 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:04,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:15:04,296 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
paging_test.py::TestPagingDatasetChanges::test_node_unavailabe_during_paging 
-------------------------------- live log call ---------------------------------
08:15:41,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:15:41,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:15:41,840 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:41,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:15:41,906 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:41,996 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:15:42,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:15:42,81 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:42,147 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:15:42,147 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:42,238 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:15:42,323 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:15:42,323 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:15:42,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:15:42,390 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:16:11,957 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
08:16:12,229 cassandra.cluster ERROR Unexpected exception while handling result in ResponseFuture:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 4678, in cassandra.cluster.ResponseFuture._set_result
  File "cassandra/cluster.py", line 4831, in cassandra.cluster.ResponseFuture._handle_retry_decision
  File "cassandra/cluster.py", line 4815, in cassandra.cluster.ResponseFuture._set_final_exception
  File "/users/masix/cassandra-dtest/tools/paging.py", line 68, in handle_error
    raise exc
cassandra.Unavailable: Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level ALL" info={'consistency': 'ALL', 'required_replicas': 1, 'alive_replicas': 0}
08:16:12,231 cassandra.connection ERROR Callback handler errored, ignoring:
Traceback (most recent call last):
  File "cassandra/connection.py", line 1218, in cassandra.connection.Connection.process_msg
  File "cassandra/cluster.py", line 4703, in cassandra.cluster.ResponseFuture._set_result
  File "cassandra/cluster.py", line 4815, in cassandra.cluster.ResponseFuture._set_final_exception
  File "/users/masix/cassandra-dtest/tools/paging.py", line 68, in handle_error
    raise exc
  File "cassandra/cluster.py", line 4678, in cassandra.cluster.ResponseFuture._set_result
  File "cassandra/cluster.py", line 4831, in cassandra.cluster.ResponseFuture._handle_retry_decision
  File "cassandra/cluster.py", line 4815, in cassandra.cluster.ResponseFuture._set_final_exception
  File "/users/masix/cassandra-dtest/tools/paging.py", line 68, in handle_error
    raise exc
cassandra.Unavailable: Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level ALL" info={'consistency': 'ALL', 'required_replicas': 1, 'alive_replicas': 0}
08:16:13,164 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.18 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
08:16:15,372 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.76 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
PASSED                                                                   [ 82%]
paging_test.py::TestPagingQueryIsolation::test_query_isolation 
-------------------------------- live log call ---------------------------------
08:16:17,352 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:16:17,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:16:17,439 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:16:17,505 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:16:17,505 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:16:17,596 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:16:17,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:16:17,681 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:16:17,747 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:16:17,747 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:16:17,838 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:16:17,923 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:16:17,923 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:16:17,988 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:16:17,988 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 84%]
paging_test.py::TestPagingWithDeletions::test_single_partition_deletions 
-------------------------------- live log call ---------------------------------
08:17:04,863 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:04,948 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:17:04,948 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:05,14 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:17:05,15 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:05,105 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:05,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:17:05,191 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:05,257 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:17:05,257 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:05,347 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:05,433 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:17:05,434 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:05,499 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:17:05,500 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 85%]
paging_test.py::TestPagingWithDeletions::test_multiple_partition_deletions 
-------------------------------- live log call ---------------------------------
08:17:27,864 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:27,951 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:17:27,951 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:28,18 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:17:28,18 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:28,120 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:28,206 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:17:28,206 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:28,272 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:17:28,272 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:28,363 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:28,448 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:17:28,449 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:28,517 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:17:28,517 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 87%]
paging_test.py::TestPagingWithDeletions::test_single_row_deletions 
-------------------------------- live log call ---------------------------------
08:17:49,360 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:49,447 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:17:49,448 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:49,514 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:17:49,514 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:49,606 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:49,749 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:17:49,749 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:49,818 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:17:49,819 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:49,911 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:17:49,997 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:17:49,997 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:17:50,63 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:17:50,63 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 89%]
paging_test.py::TestPagingWithDeletions::test_multiple_row_deletions SKIPPED [ 91%]
paging_test.py::TestPagingWithDeletions::test_single_cell_deletions 
-------------------------------- live log call ---------------------------------
08:18:13,878 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:18:13,964 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:18:13,964 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:14,31 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:18:14,31 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:14,134 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:18:14,220 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:18:14,220 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:14,286 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:18:14,286 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:14,377 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:18:14,463 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:18:14,463 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:14,529 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:18:14,529 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 92%]
paging_test.py::TestPagingWithDeletions::test_multiple_cell_deletions 
-------------------------------- live log call ---------------------------------
08:18:37,639 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:18:37,726 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:18:37,726 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:37,795 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:18:37,795 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:37,887 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:18:37,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:18:37,973 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:38,41 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:18:38,41 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:38,134 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:18:38,220 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:18:38,220 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:18:38,287 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:18:38,288 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 94%]
paging_test.py::TestPagingWithDeletions::test_ttl_deletions 
-------------------------------- live log call ---------------------------------
08:19:01,156 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:19:01,246 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:19:01,246 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:01,314 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:19:01,314 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:01,406 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:19:01,493 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:19:01,493 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:01,581 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:19:01,581 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:01,675 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:19:01,760 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:19:01,761 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:01,831 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:19:01,832 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 96%]
paging_test.py::TestPagingWithDeletions::test_failure_threshold_deletions 
-------------------------------- live log call ---------------------------------
08:19:39,725 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:19:39,813 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:19:39,813 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:39,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:19:39,880 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:39,971 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:19:40,56 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:19:40,57 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:40,123 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:19:40,123 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:40,216 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:19:40,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:19:40,301 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:19:40,368 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:19:40,368 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 98%]
paging_test.py::TestPagingWithDeletions::test_deletion_with_distinct_paging 
-------------------------------- live log call ---------------------------------
08:20:11,546 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:20:11,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:20:11,634 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:20:11,701 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
08:20:11,701 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:20:11,792 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:20:11,878 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:20:11,878 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:20:11,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
08:20:11,944 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:20:12,47 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
08:20:12,132 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:20:12,133 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
08:20:12,199 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
08:20:12,200 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [100%]
===Flaky Test Report===

test_with_no_results passed 1 out of the required 1 times. Success!
test_with_less_results_than_page_size passed 1 out of the required 1 times. Success!
test_with_more_results_than_page_size passed 1 out of the required 1 times. Success!
test_with_equal_results_to_page_size passed 1 out of the required 1 times. Success!
test_undefined_page_size_default passed 1 out of the required 1 times. Success!
test_with_order_by passed 1 out of the required 1 times. Success!
test_with_order_by_reversed passed 1 out of the required 1 times. Success!
test_with_limit passed 1 out of the required 1 times. Success!
test_with_allow_filtering passed 1 out of the required 1 times. Success!
test_paging_a_single_wide_row passed 1 out of the required 1 times. Success!
test_paging_across_multi_wide_rows passed 1 out of the required 1 times. Success!
test_paging_using_secondary_indexes passed 1 out of the required 1 times. Success!
test_paging_with_in_orderby_and_two_partition_keys passed 1 out of the required 1 times. Success!
test_group_by_paging passed 1 out of the required 1 times. Success!
test_group_by_with_range_name_query_paging passed 1 out of the required 1 times. Success!
test_group_by_with_static_columns_paging passed 1 out of the required 1 times. Success!
test_static_columns_paging passed 1 out of the required 1 times. Success!
test_paging_using_secondary_indexes_with_static_cols passed 1 out of the required 1 times. Success!
test_static_columns_with_empty_non_static_columns_paging passed 1 out of the required 1 times. Success!
test_select_in_clause_with_duplicate_keys passed 1 out of the required 1 times. Success!
test_paging_with_filtering passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_counter_columns passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_clustering_columns passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_clustering_columns_with_contains passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_static_columns passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_partition_key passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_partition_key_with_limit passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_partition_key_on_counter_columns passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_partition_key_on_clustering_columns passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_partition_key_on_clustering_columns_with_contains passed 1 out of the required 1 times. Success!
test_paging_with_filtering_on_partition_key_on_static_columns passed 1 out of the required 1 times. Success!
test_paging_with_no_clustering_columns passed 1 out of the required 1 times. Success!
test_per_partition_limit_paging passed 1 out of the required 1 times. Success!
test_paging_for_range_name_queries passed 1 out of the required 1 times. Success!
test_paging_with_empty_row_and_empty_static_columns passed 1 out of the required 1 times. Success!
test_data_change_impacting_earlier_page passed 1 out of the required 1 times. Success!
test_data_change_impacting_later_page passed 1 out of the required 1 times. Success!
test_row_TTL_expiry_during_paging passed 1 out of the required 1 times. Success!
test_cell_TTL_expiry_during_paging passed 1 out of the required 1 times. Success!
test_node_unavailabe_during_paging passed 1 out of the required 1 times. Success!
test_query_isolation passed 1 out of the required 1 times. Success!
test_single_partition_deletions passed 1 out of the required 1 times. Success!
test_multiple_partition_deletions passed 1 out of the required 1 times. Success!
test_single_row_deletions passed 1 out of the required 1 times. Success!
test_single_cell_deletions passed 1 out of the required 1 times. Success!
test_multiple_cell_deletions passed 1 out of the required 1 times. Success!
test_ttl_deletions passed 1 out of the required 1 times. Success!
test_failure_threshold_deletions passed 1 out of the required 1 times. Success!
test_deletion_with_distinct_paging passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 49 passed, 8 skipped in 1185.50 seconds ====================
[msx] rc = 0
