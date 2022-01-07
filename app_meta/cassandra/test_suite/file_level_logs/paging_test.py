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
22:04:36,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:04:37,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:04:37,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:04:37,245 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:04:37,330 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:04:37,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:04:37,487 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:04:37,571 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:04:37,637 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  1%]
paging_test.py::TestPagingSize::test_with_less_results_than_page_size 
-------------------------------- live log call ---------------------------------
22:04:57,492 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:04:57,579 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:04:57,645 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:04:57,741 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:04:57,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:04:57,915 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:04:58,7 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:04:58,93 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:04:58,159 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  3%]
paging_test.py::TestPagingSize::test_with_more_results_than_page_size 
-------------------------------- live log call ---------------------------------
22:05:17,232 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:17,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:05:17,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:05:17,477 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:17,562 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:05:17,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:05:17,722 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:17,806 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:05:17,872 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  5%]
paging_test.py::TestPagingSize::test_with_equal_results_to_page_size 
-------------------------------- live log call ---------------------------------
22:05:38,244 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:38,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:05:38,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:05:38,515 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:38,601 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:05:38,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:05:38,761 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:38,846 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:05:38,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  7%]
paging_test.py::TestPagingSize::test_undefined_page_size_default 
-------------------------------- live log call ---------------------------------
22:05:58,992 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:59,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:05:59,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:05:59,239 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:59,325 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:05:59,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:05:59,483 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:05:59,567 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:05:59,634 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [  8%]
paging_test.py::TestPagingWithModifiers::test_with_order_by 
-------------------------------- live log call ---------------------------------
22:06:21,333 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:06:21,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:06:21,495 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:06:21,592 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:06:21,681 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:06:21,751 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:06:21,843 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:06:21,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:06:21,993 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 10%]
paging_test.py::TestPagingWithModifiers::test_with_order_by_reversed 
-------------------------------- live log call ---------------------------------
22:06:41,578 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:06:41,663 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:06:41,730 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:06:41,822 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:06:41,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:06:41,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:06:42,92 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:06:42,177 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:06:42,243 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 12%]
paging_test.py::TestPagingWithModifiers::test_with_limit 
-------------------------------- live log call ---------------------------------
22:07:04,81 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:04,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:07:04,233 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:07:04,324 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:04,408 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:07:04,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:07:04,564 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:04,647 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:07:04,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 14%]
paging_test.py::TestPagingWithModifiers::test_with_allow_filtering 
-------------------------------- live log call ---------------------------------
22:07:27,853 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:27,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:07:28,6 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:07:28,97 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:28,181 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:07:28,248 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:07:28,339 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:28,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:07:28,490 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 15%]
paging_test.py::TestPagingData::test_paging_a_single_wide_row 
-------------------------------- live log call ---------------------------------
22:07:49,605 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:49,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:07:49,756 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:07:49,848 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:49,933 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:07:49,999 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:07:50,91 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:07:50,176 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:07:50,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 17%]
paging_test.py::TestPagingData::test_paging_across_multi_wide_rows 
-------------------------------- live log call ---------------------------------
22:08:12,769 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:12,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:08:12,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:08:13,11 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:13,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:08:13,161 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:08:13,253 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:13,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:08:13,404 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 19%]
paging_test.py::TestPagingData::test_paging_using_secondary_indexes 
-------------------------------- live log call ---------------------------------
22:08:36,667 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:36,752 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:08:36,819 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:08:36,910 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:36,994 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:08:37,60 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:08:37,151 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:37,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:08:37,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 21%]
paging_test.py::TestPagingData::test_paging_with_in_orderby_and_two_partition_keys 
-------------------------------- live log call ---------------------------------
22:08:58,957 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:59,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:08:59,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:08:59,204 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:59,288 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:08:59,354 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:08:59,446 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:08:59,530 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:08:59,596 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 22%]
paging_test.py::TestPagingData::test_group_by_paging 
-------------------------------- live log call ---------------------------------
22:09:19,712 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:09:19,800 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:09:19,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:09:19,961 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:09:20,45 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:09:20,112 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:09:20,204 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:09:20,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:09:20,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:09:40,125 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,191 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,251 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,274 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,290 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,330 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,356 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,372 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,418 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,449 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,470 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,493 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,505 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,530 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,549 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,565 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,593 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,629 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,651 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,672 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,716 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,743 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,765 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,791 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,818 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,841 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,869 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,889 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,916 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,939 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,965 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:40,993 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,13 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,37 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,60 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,78 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,101 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,125 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,144 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,168 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,190 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,203 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,227 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,586 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,607 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,629 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,640 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,662 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,675 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,690 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,707 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,720 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,732 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,742 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,754 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,767 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,778 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,787 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,800 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,814 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,824 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,837 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,852 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,861 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,875 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,885 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,895 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,909 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,921 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,932 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,945 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,957 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:41,979 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:41,989 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,7 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,21 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,43 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,59 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,86 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,111 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,128 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,138 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,157 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,170 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,190 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,211 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,228 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,245 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,267 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,294 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,325 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,336 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,357 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,380 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,404 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,427 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,456 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,475 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,500 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,532 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,543 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,565 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,584 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,594 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,610 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:42,848 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,860 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,867 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,883 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,894 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,904 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,920 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,933 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,943 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,954 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,965 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,973 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,985 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:42,997 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,8 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,21 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,33 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,46 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,57 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,69 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,79 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,89 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,99 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,115 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,131 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,143 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,161 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,175 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,193 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,214 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,225 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,239 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,250 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,267 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,284 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,298 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,313 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,333 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,350 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,377 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,397 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,421 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,439 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,461 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,477 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,494 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,511 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,539 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,558 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,578 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,587 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,606 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:43,820 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,832 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,847 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,863 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,876 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,888 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,897 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,915 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,926 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,938 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,950 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,961 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,972 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,984 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:43,996 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,4 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,13 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,22 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,30 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,38 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,52 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,69 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,77 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,89 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,104 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,121 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,139 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,150 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,168 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,177 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,189 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,205 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,217 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,229 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,260 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,270 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,295 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,317 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,343 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,364 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,374 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,393 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,401 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,427 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,445 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,462 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,470 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,488 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,645 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,656 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,669 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,682 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,694 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,705 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,712 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,721 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,730 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,741 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,751 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,761 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,773 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,784 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,795 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,801 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,813 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,821 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,831 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,838 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:44,855 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,873 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,888 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,900 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,917 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,936 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,950 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,962 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,978 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:44,989 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,1 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,24 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,50 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,66 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,91 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,112 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,135 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,161 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,178 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,194 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,203 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,216 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,362 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,373 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,383 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,395 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,405 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,416 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,427 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,437 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,445 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,455 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,463 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,472 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,482 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,488 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,496 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:45,509 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,519 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,531 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,542 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,558 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,573 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,582 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,594 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,607 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,617 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,628 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,652 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,676 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,694 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,718 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,743 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,768 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,788 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,803 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,819 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,827 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,840 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:09:45,997 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,8 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,18 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,31 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,43 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,53 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,64 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,74 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,84 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,95 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,105 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,116 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,128 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,137 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:09:46,144 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
PASSED                                                                   [ 24%]
paging_test.py::TestPagingData::test_group_by_with_range_name_query_paging 
-------------------------------- live log call ---------------------------------
22:09:46,767 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:09:46,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:09:46,920 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:09:47,12 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:09:47,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:09:47,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:09:47,256 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:09:47,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:09:47,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:10:06,292 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,368 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,438 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,465 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,496 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,526 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,556 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,573 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,602 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,629 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,656 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,679 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,711 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,733 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,766 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,798 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,840 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,875 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,904 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,934 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:06,976 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,5 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,20 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,48 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,61 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,86 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,111 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,126 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,151 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,165 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,191 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,216 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,259 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,276 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,319 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,337 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,372 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,386 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,419 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,440 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,461 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,485 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,507 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,527 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,546 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,567 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,600 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,640 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,677 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,706 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,728 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,748 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,773 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,787 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,808 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,829 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,850 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,890 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,933 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,973 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:07,996 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,14 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,32 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,57 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,74 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,91 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,107 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,146 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,187 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,221 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,241 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,258 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,275 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,297 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,313 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,331 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,346 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,382 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,420 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,453 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:08,473 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 26%]
paging_test.py::TestPagingData::test_group_by_with_static_columns_paging 
-------------------------------- live log call ---------------------------------
22:10:09,22 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:10:09,107 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:10:09,173 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:10:09,266 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:10:09,350 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:10:09,417 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:10:09,509 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:10:09,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:10:09,660 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:10:29,780 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,856 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,912 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,931 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,955 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,967 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,984 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:29,996 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,19 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,34 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,59 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,88 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,119 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,133 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,159 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,281 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,301 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,322 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,338 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,359 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,372 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,386 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,402 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,422 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,436 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,449 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,469 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,493 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,507 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,526 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,544 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,558 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,575 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,590 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,613 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,631 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,642 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,654 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,678 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,712 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,739 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,762 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,776 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,805 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:30,908 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,931 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,953 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,972 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:30,986 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,4 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,23 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,41 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,59 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,70 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,89 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,107 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,123 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,140 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,156 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,166 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,183 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,211 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,235 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,260 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,271 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,294 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,384 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,401 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,417 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,431 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,443 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,460 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,476 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,492 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,508 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,520 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,536 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,552 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,570 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,587 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,603 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,615 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,632 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,656 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,680 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,703 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,714 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,737 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:31,818 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,834 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,853 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,871 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,884 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,900 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,916 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,931 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,946 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,957 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,972 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:31,988 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,5 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,20 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,35 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,46 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,61 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,85 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,106 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,127 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,138 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,161 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,240 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,253 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,268 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,281 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,292 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,306 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,322 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,336 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,349 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,360 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,374 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,388 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,402 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,416 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,428 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,438 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,452 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,469 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,490 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,509 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,518 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,537 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,609 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,623 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,638 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,652 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,662 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,676 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,691 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,705 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,719 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,729 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,743 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:32,872 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,891 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,901 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,924 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,942 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,959 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:32,967 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,8 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,30 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,45 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,74 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,108 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,122 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,128 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,149 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,169 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,183 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,190 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,215 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,242 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,268 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,289 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,306 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,320 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,327 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,348 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,368 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,387 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,395 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,421 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,439 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,447 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,466 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,484 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,492 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,511 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,529 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,546 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,568 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,589 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,600 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,620 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:33,786 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,799 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,808 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,828 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,840 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,853 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,862 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,884 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,898 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,911 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,931 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,947 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,959 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,967 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,979 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:33,991 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,1 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,8 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,25 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,46 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,63 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,75 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,86 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,97 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,104 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,120 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,129 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,141 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,151 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,160 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,168 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,179 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,188 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,201 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,216 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,225 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,237 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,245 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,259 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,269 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,283 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:34,306 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,318 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,336 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,350 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,358 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,378 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,395 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,414 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,443 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,455 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,470 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,483 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,490 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,509 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,529 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,554 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,570 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,585 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,593 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,614 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,637 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,645 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,671 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,685 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,715 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,728 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,757 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,766 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,788 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,809 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,831 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,840 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,862 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:34,995 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,3 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,16 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,26 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,34 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,51 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,64 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,79 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,91 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,98 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,109 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,119 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,126 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,138 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,155 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,166 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,177 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,188 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,195 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,209 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,217 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,228 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,241 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,249 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,260 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,267 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,280 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,291 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,303 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,316 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,324 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,335 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,352 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,359 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,374 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,387 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,404 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,418 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,434 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,453 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,460 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,474 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,486 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,501 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,519 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,533 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,546 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,559 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,581 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,600 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,623 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,630 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,656 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,662 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,690 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,706 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,726 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,746 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,754 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,776 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:35,900 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,907 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,919 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,930 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,947 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,960 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,973 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,989 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:35,996 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,7 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,17 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,28 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,42 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,53 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,63 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,72 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,87 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,98 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,106 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,117 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,130 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,140 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,151 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,163 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,172 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,183 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,198 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,211 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,223 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,239 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,250 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,266 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,287 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,302 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,310 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,325 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,338 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,348 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,360 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,369 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,396 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,411 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,436 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,460 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,485 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,497 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,516 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,536 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,545 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,565 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,690 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,702 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,710 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,723 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,735 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,747 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,759 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,771 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,778 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,786 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,801 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,810 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,820 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,827 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,839 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,850 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,858 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,874 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,886 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,896 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,906 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,917 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,925 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,938 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:36,956 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,975 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:36,990 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,4 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,20 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,39 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,53 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,63 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,77 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,87 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,100 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,125 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,156 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,181 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,204 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,221 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,240 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,259 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,269 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,287 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,397 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,410 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,421 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,433 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,445 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,456 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,467 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,477 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,488 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,497 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,508 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,520 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,531 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,543 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,554 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,564 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,572 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,583 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,591 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,603 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:37,615 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,626 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,639 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,650 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,665 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,679 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,689 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,699 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,711 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,721 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,733 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,757 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,786 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,812 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,834 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,849 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,866 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,885 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,893 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:37,910 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
22:10:38,23 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,34 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,45 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,56 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,68 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,78 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,88 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,97 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,107 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,115 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,126 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,138 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,149 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,161 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,172 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,183 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,192 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,203 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,211 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
22:10:38,223 cassandra.protocol WARNING Server warning: Aggregation query used on multiple partition keys (IN restriction)
PASSED                                                                   [ 28%]
paging_test.py::TestPagingData::test_static_columns_paging 
-------------------------------- live log call ---------------------------------
22:10:38,844 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:10:38,952 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:10:39,19 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:10:39,111 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:10:39,195 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:10:39,262 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:10:39,354 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:10:39,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:10:39,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 29%]
paging_test.py::TestPagingData::test_paging_using_secondary_indexes_with_static_cols 
-------------------------------- live log call ---------------------------------
22:11:10,149 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:10,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:11:10,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:11:10,393 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:10,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:11:10,544 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:11:10,636 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:10,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:11:10,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 31%]
paging_test.py::TestPagingData::test_static_columns_with_empty_non_static_columns_paging 
-------------------------------- live log call ---------------------------------
22:11:33,436 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:33,521 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:11:33,588 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:11:33,679 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:33,763 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:11:33,829 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:11:33,920 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:34,4 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:11:34,69 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 33%]
paging_test.py::TestPagingData::test_select_in_clause_with_duplicate_keys 
-------------------------------- live log call ---------------------------------
22:11:54,438 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:54,526 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:11:54,594 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:11:54,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:54,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:11:54,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:11:54,927 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:11:55,12 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:11:55,78 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 35%]
paging_test.py::TestPagingData::test_paging_with_filtering 
-------------------------------- live log call ---------------------------------
22:12:15,439 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:12:15,527 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:12:15,594 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:12:15,685 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:12:15,769 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:12:15,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:12:15,927 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:12:16,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:12:16,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 36%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_counter_columns 
-------------------------------- live log call ---------------------------------
22:12:38,699 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:12:38,785 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:12:38,852 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:12:38,944 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:12:39,28 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:12:39,95 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:12:39,187 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:12:39,271 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:12:39,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 38%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_counter_columns_compact SKIPPED [ 40%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_clustering_columns 
-------------------------------- live log call ---------------------------------
22:13:00,769 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:00,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:13:00,921 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:13:01,13 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:01,98 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:13:01,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:13:01,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:01,370 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:13:01,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 42%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_clustering_columns_compact SKIPPED [ 43%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_clustering_columns_with_contains 
-------------------------------- live log call ---------------------------------
22:13:23,69 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:23,154 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:13:23,220 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:13:23,311 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:23,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:13:23,465 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:13:23,558 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:23,642 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:13:23,708 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 45%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_static_columns 
-------------------------------- live log call ---------------------------------
22:13:47,587 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:47,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:13:47,741 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:13:47,837 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:47,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:13:47,989 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:13:48,82 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:13:48,166 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:13:48,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 47%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key 
-------------------------------- live log call ---------------------------------
22:14:08,336 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:08,424 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:14:08,494 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:14:08,586 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:08,669 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:14:08,735 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:14:08,827 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:08,910 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:14:08,976 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 49%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_with_limit 
-------------------------------- live log call ---------------------------------
22:14:31,112 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:31,197 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:14:31,264 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:14:31,356 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:31,440 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:14:31,507 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:14:31,599 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:31,683 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:14:31,750 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 50%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_counter_columns 
-------------------------------- live log call ---------------------------------
22:14:51,864 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:51,949 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:14:52,16 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:14:52,108 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:52,192 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:14:52,258 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:14:52,350 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:14:52,434 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:14:52,500 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 52%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_counter_columns_compact SKIPPED [ 54%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_clustering_columns 
-------------------------------- live log call ---------------------------------
22:15:13,920 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:15:14,5 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:15:14,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:15:14,165 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:15:14,249 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:15:14,317 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:15:14,408 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:15:14,492 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:15:14,559 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 56%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_clustering_columns_compact SKIPPED [ 57%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_clustering_columns_with_contains 
-------------------------------- live log call ---------------------------------
22:15:37,999 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:15:38,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:15:38,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:15:38,253 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:15:38,338 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:15:38,407 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:15:38,499 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:15:38,584 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:15:38,651 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 59%]
paging_test.py::TestPagingData::test_paging_with_filtering_on_partition_key_on_static_columns 
-------------------------------- live log call ---------------------------------
22:16:03,13 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:03,97 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:16:03,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:16:03,258 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:03,344 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:16:03,411 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:16:03,503 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:03,587 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:16:03,653 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 61%]
paging_test.py::TestPagingData::test_paging_on_compact_table_with_tombstone_on_first_column SKIPPED [ 63%]
paging_test.py::TestPagingData::test_paging_with_no_clustering_columns 
-------------------------------- live log call ---------------------------------
22:16:24,565 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:24,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:16:24,719 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:16:24,811 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:24,896 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:16:24,962 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:16:25,53 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:25,139 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:16:25,205 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 64%]
paging_test.py::TestPagingData::test_paging_with_no_clustering_columns_compact SKIPPED [ 66%]
paging_test.py::TestPagingData::test_per_partition_limit_paging 
-------------------------------- live log call ---------------------------------
22:16:45,884 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:45,970 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:16:46,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:16:46,129 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:46,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:16:46,279 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:16:46,370 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:16:46,455 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:16:46,521 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 68%]
paging_test.py::TestPagingData::test_paging_for_range_name_queries 
-------------------------------- live log call ---------------------------------
22:17:08,150 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:08,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:17:08,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:17:08,393 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:08,477 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:17:08,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:17:08,635 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:08,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:17:08,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 70%]
paging_test.py::TestPagingData::test_paging_for_range_name_queries_compact SKIPPED [ 71%]
paging_test.py::TestPagingData::test_paging_with_empty_row_and_empty_static_columns 
-------------------------------- live log call ---------------------------------
22:17:30,204 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:30,289 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:17:30,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:17:30,447 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:30,531 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:17:30,598 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:17:30,690 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:30,774 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:17:30,845 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 73%]
paging_test.py::TestPagingDatasetChanges::test_data_change_impacting_earlier_page 
-------------------------------- live log call ---------------------------------
22:17:51,953 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:52,39 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:17:52,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:17:52,198 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:52,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:17:52,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:17:52,470 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:17:52,555 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:17:52,621 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 75%]
paging_test.py::TestPagingDatasetChanges::test_data_change_impacting_later_page 
-------------------------------- live log call ---------------------------------
22:18:13,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:18:13,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:18:13,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:18:13,504 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:18:13,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:18:13,656 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:18:13,747 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:18:13,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:18:13,900 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 77%]
paging_test.py::TestPagingDatasetChanges::test_row_TTL_expiry_during_paging 
-------------------------------- live log call ---------------------------------
22:18:34,518 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:18:34,603 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:18:34,670 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:18:34,765 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:18:34,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:18:34,916 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:18:35,8 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:18:35,92 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:18:35,158 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 78%]
paging_test.py::TestPagingDatasetChanges::test_cell_TTL_expiry_during_paging 
-------------------------------- live log call ---------------------------------
22:19:10,830 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:19:10,918 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:19:10,986 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:19:11,78 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:19:11,163 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:19:11,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:19:11,320 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:19:11,405 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:19:11,471 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 80%]
paging_test.py::TestPagingDatasetChanges::test_node_unavailabe_during_paging 
-------------------------------- live log call ---------------------------------
22:19:49,437 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:19:49,523 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:19:49,590 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:19:49,682 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:19:49,767 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:19:49,834 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:19:49,926 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:19:50,10 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:19:50,76 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:20:18,754 cassandra.cluster ERROR Unexpected exception while handling result in ResponseFuture:
Traceback (most recent call last):
  File "cassandra/cluster.py", line 4678, in cassandra.cluster.ResponseFuture._set_result
  File "cassandra/cluster.py", line 4831, in cassandra.cluster.ResponseFuture._handle_retry_decision
  File "cassandra/cluster.py", line 4815, in cassandra.cluster.ResponseFuture._set_final_exception
  File "/users/masix/cassandra-dtest/tools/paging.py", line 68, in handle_error
    raise exc
cassandra.Unavailable: Error from server: code=1000 [Unavailable exception] message="Cannot achieve consistency level ALL" info={'consistency': 'ALL', 'required_replicas': 1, 'alive_replicas': 0}
22:20:18,756 cassandra.connection ERROR Callback handler errored, ignoring:
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
PASSED                                                                   [ 82%]
paging_test.py::TestPagingQueryIsolation::test_query_isolation 
-------------------------------- live log call ---------------------------------
22:20:24,44 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:20:24,130 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:20:24,196 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:20:24,287 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:20:24,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:20:24,437 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:20:24,528 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:20:24,613 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:20:24,679 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 84%]
paging_test.py::TestPagingWithDeletions::test_single_partition_deletions 
-------------------------------- live log call ---------------------------------
22:21:13,539 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:13,623 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:21:13,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:21:13,781 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:13,865 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:21:13,931 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:21:14,22 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:14,106 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:21:14,173 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 85%]
paging_test.py::TestPagingWithDeletions::test_multiple_partition_deletions 
-------------------------------- live log call ---------------------------------
22:21:37,303 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:37,388 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:21:37,454 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:21:37,545 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:37,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:21:37,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:21:37,798 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:37,882 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:21:37,953 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 87%]
paging_test.py::TestPagingWithDeletions::test_single_row_deletions 
-------------------------------- live log call ---------------------------------
22:21:59,308 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:59,393 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:21:59,459 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:21:59,552 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:59,637 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:21:59,705 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:21:59,802 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:21:59,888 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:21:59,955 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 89%]
paging_test.py::TestPagingWithDeletions::test_multiple_row_deletions SKIPPED [ 91%]
paging_test.py::TestPagingWithDeletions::test_single_cell_deletions 
-------------------------------- live log call ---------------------------------
22:22:24,332 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:22:24,417 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:22:24,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:22:24,575 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:22:24,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:22:24,728 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:22:24,819 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:22:24,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:22:24,970 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 92%]
paging_test.py::TestPagingWithDeletions::test_multiple_cell_deletions 
-------------------------------- live log call ---------------------------------
22:22:50,134 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:22:50,227 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:22:50,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:22:50,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:22:50,473 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:22:50,540 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:22:50,631 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:22:50,717 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:22:50,784 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 94%]
paging_test.py::TestPagingWithDeletions::test_ttl_deletions 
-------------------------------- live log call ---------------------------------
22:23:13,651 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:23:13,738 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:23:13,805 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:23:13,897 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:23:13,982 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:23:14,50 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:23:14,142 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:23:14,227 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:23:14,294 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 96%]
paging_test.py::TestPagingWithDeletions::test_failure_threshold_deletions 
-------------------------------- live log call ---------------------------------
22:23:53,723 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:23:53,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:23:53,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:23:53,969 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:23:54,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:23:54,120 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:23:54,213 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:23:54,301 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:23:54,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
PASSED                                                                   [ 98%]
paging_test.py::TestPagingWithDeletions::test_deletion_with_distinct_paging 
-------------------------------- live log call ---------------------------------
22:24:25,783 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:24:25,870 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:24:25,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
22:24:26,29 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:24:26,113 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:24:26,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
22:24:26,272 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
22:24:26,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
22:24:26,423 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
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

=================== 49 passed, 8 skipped in 1211.69 seconds ====================
[msx] rc = 0
