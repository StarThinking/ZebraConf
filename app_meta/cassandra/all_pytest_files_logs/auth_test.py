cassandra auth_test.py true true
the_test is auth_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 93 items

auth_test.py::TestAuth::test_system_auth_ks_is_alterable 
-------------------------------- live log call ---------------------------------
01:30:41,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:30:41,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:30:41,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:30:41,543 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:30:41,543 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:30:41,635 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:30:41,719 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:30:41,719 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:30:41,785 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:30:41,785 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:30:41,876 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:30:41,961 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:30:41,961 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:30:42,27 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
01:30:42,27 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:30:58,934 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [  1%]
auth_test.py::TestAuth::test_login 
-------------------------------- live log call ---------------------------------
01:32:08,173 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:32:08,260 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:32:08,260 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:32:08,327 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:32:08,327 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  2%]
auth_test.py::TestAuth::test_only_superuser_can_create_users SKIPPED     [  3%]
auth_test.py::TestAuth::test_password_authenticator_create_user_requires_password SKIPPED [  4%]
auth_test.py::TestAuth::test_cant_create_existing_user 
-------------------------------- live log call ---------------------------------
01:33:25,689 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:33:25,774 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:33:25,775 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:33:25,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:33:25,841 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  5%]
auth_test.py::TestAuth::test_list_users 
-------------------------------- live log call ---------------------------------
01:33:42,414 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:33:42,502 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:33:42,502 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:33:42,568 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:33:42,568 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  6%]
auth_test.py::TestAuth::test_handle_corrupt_role_data 
-------------------------------- live log call ---------------------------------
01:33:59,927 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:34:00,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:00,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:34:00,84 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:00,84 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:34:16,601 cassandra.cluster WARNING Host 127.0.0.1:9042 error: Server error.
PASSED                                                                   [  7%]
auth_test.py::TestAuth::test_user_cant_drop_themselves 
-------------------------------- live log call ---------------------------------
01:34:17,136 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:34:17,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:17,224 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:34:17,290 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:17,290 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [  8%]
auth_test.py::TestAuth::test_only_superusers_can_drop_users SKIPPED      [  9%]
auth_test.py::TestAuth::test_dropping_nonexistent_user_throws_exception 
-------------------------------- live log call ---------------------------------
01:34:33,655 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:34:33,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:33,744 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:34:33,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:33,811 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 10%]
auth_test.py::TestAuth::test_drop_user_case_sensitive 
-------------------------------- live log call ---------------------------------
01:34:50,156 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:34:50,242 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:50,243 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:34:50,309 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:34:50,309 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 11%]
auth_test.py::TestAuth::test_alter_user_case_sensitive 
-------------------------------- live log call ---------------------------------
01:35:07,119 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:35:07,204 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:07,205 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:35:07,271 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:07,271 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 12%]
auth_test.py::TestAuth::test_regular_users_can_alter_their_passwords_only 
-------------------------------- live log call ---------------------------------
01:35:24,98 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:35:24,186 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:24,186 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:35:24,296 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:24,297 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 13%]
auth_test.py::TestAuth::test_users_cant_alter_their_superuser_status 
-------------------------------- live log call ---------------------------------
01:35:43,599 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:35:43,685 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:43,685 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:35:43,752 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:35:43,752 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 15%]
auth_test.py::TestAuth::test_only_superuser_alters_superuser_status 
-------------------------------- live log call ---------------------------------
01:36:00,82 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:36:00,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:00,168 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:36:00,235 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:00,236 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 16%]
auth_test.py::TestAuth::test_altering_nonexistent_user_throws_exception 
-------------------------------- live log call ---------------------------------
01:36:17,60 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:36:17,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:17,146 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:36:17,213 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:17,213 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 17%]
auth_test.py::TestAuth::test_conditional_create_drop_user 
-------------------------------- live log call ---------------------------------
01:36:33,540 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:36:33,659 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:33,659 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:36:33,726 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:33,726 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 18%]
auth_test.py::TestAuth::test_create_ks_auth 
-------------------------------- live log call ---------------------------------
01:36:50,520 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:36:50,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:50,606 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:36:50,673 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:36:50,673 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 19%]
auth_test.py::TestAuth::test_create_cf_auth 
-------------------------------- live log call ---------------------------------
01:37:07,755 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:37:07,841 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:07,843 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:37:07,911 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:07,912 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 20%]
auth_test.py::TestAuth::test_alter_ks_auth 
-------------------------------- live log call ---------------------------------
01:37:25,237 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:37:25,322 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:25,322 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:37:25,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:25,389 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:37:42,27 cassandra.protocol WARNING Server warning: Your replication factor 2 for keyspace ks is higher than the number of nodes 1
01:37:42,28 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 21%]
auth_test.py::TestAuth::test_alter_cf_auth 
-------------------------------- live log call ---------------------------------
01:37:42,463 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:37:42,549 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:42,549 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:37:42,617 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:37:42,617 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 22%]
auth_test.py::TestAuth::test_materialized_views_auth 
-------------------------------- live log call ---------------------------------
01:38:00,455 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:38:00,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:00,541 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:38:00,607 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:00,608 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:38:17,521 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 23%]
auth_test.py::TestAuth::test_drop_ks_auth 
-------------------------------- live log call ---------------------------------
01:38:18,769 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:38:18,854 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:18,855 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:38:18,921 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:18,921 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 24%]
auth_test.py::TestAuth::test_drop_cf_auth 
-------------------------------- live log call ---------------------------------
01:38:36,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:38:36,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:36,329 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:38:36,395 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:36,396 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 25%]
auth_test.py::TestAuth::test_modify_and_select_auth 
-------------------------------- live log call ---------------------------------
01:38:54,233 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:38:54,318 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:54,318 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:38:54,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:38:54,385 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 26%]
auth_test.py::TestAuth::test_grant_revoke_without_ks_specified 
-------------------------------- live log call ---------------------------------
01:39:11,987 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:39:12,73 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:12,73 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:39:12,142 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:12,143 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 27%]
auth_test.py::TestAuth::test_grant_revoke_auth 
-------------------------------- live log call ---------------------------------
01:39:29,706 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:39:29,792 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:29,792 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:39:29,858 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:29,859 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 29%]
auth_test.py::TestAuth::test_grant_revoke_nonexistent_user_or_ks 
-------------------------------- live log call ---------------------------------
01:39:47,439 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:39:47,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:47,526 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:39:47,592 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:39:47,592 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 30%]
auth_test.py::TestAuth::test_grant_revoke_cleanup 
-------------------------------- live log call ---------------------------------
01:40:04,420 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:40:04,506 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:04,506 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:40:04,573 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:04,573 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 31%]
auth_test.py::TestAuth::test_permissions_caching 
-------------------------------- live log call ---------------------------------
01:40:22,921 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:40:23,6 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:23,6 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:40:23,81 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:23,81 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 32%]
auth_test.py::TestAuth::test_list_permissions 
-------------------------------- live log call ---------------------------------
01:40:43,158 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:40:43,243 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:43,243 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:40:43,310 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:40:43,310 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 33%]
auth_test.py::TestAuth::test_type_auth 
-------------------------------- live log call ---------------------------------
01:41:00,888 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:00,973 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:00,974 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:41:01,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:01,40 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 34%]
auth_test.py::TestAuth::test_restart_node_doesnt_lose_auth_data 
-------------------------------- live log call ---------------------------------
01:41:18,371 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:18,457 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:18,457 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:41:18,525 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:18,525 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:41:36,553 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
01:41:37,559 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.1 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:41:39,664 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 3.88 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:41:42,187 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:42,282 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:42,282 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:41:43,588 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.48 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:41:52,110 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 15.84 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
01:41:55,534 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:41:55,627 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:41:55,627 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 35%]
auth_test.py::TestAuth::test_auth_metrics 
-------------------------------- live log call ---------------------------------
01:42:02,938 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:42:03,24 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:42:03,24 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:42:03,90 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:42:03,91 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 36%]
auth_test.py::TestAuthRoles::test_create_drop_role 
-------------------------------- live log setup --------------------------------
01:42:40,721 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:42:40,806 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:42:40,806 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:42:40,874 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:42:40,874 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 37%]
auth_test.py::TestAuthRoles::test_conditional_create_drop_role 
-------------------------------- live log setup --------------------------------
01:42:57,452 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:42:57,537 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:42:57,537 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:42:57,604 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:42:57,605 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 38%]
auth_test.py::TestAuthRoles::test_create_drop_role_validation 
-------------------------------- live log setup --------------------------------
01:43:13,932 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:14,17 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:14,17 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:43:14,89 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:14,89 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 39%]
auth_test.py::TestAuthRoles::test_role_admin_validation 
-------------------------------- live log setup --------------------------------
01:43:31,166 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:31,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:31,252 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:43:31,320 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:31,321 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 40%]
auth_test.py::TestAuthRoles::test_creator_of_db_resource_granted_all_permissions 
-------------------------------- live log setup --------------------------------
01:43:51,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:43:51,273 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:51,273 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:43:51,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:43:51,342 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 41%]
auth_test.py::TestAuthRoles::test_create_and_grant_roles_with_superuser_status 
-------------------------------- live log setup --------------------------------
01:44:09,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:44:09,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:44:09,483 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:44:09,552 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:44:09,553 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 43%]
auth_test.py::TestAuthRoles::test_drop_and_revoke_roles_with_superuser_status 
-------------------------------- live log setup --------------------------------
01:44:26,389 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:44:26,476 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:44:26,476 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:44:26,544 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:44:26,544 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 44%]
auth_test.py::TestAuthRoles::test_drop_role_removes_memberships 
-------------------------------- live log setup --------------------------------
01:44:43,880 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:44:43,965 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:44:43,965 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:44:44,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:44:44,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 45%]
auth_test.py::TestAuthRoles::test_drop_role_revokes_permissions_granted_on_it 
-------------------------------- live log setup --------------------------------
01:45:00,869 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:01,70 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:01,70 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:45:01,140 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:01,140 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 46%]
auth_test.py::TestAuthRoles::test_grant_revoke_roles 
-------------------------------- live log setup --------------------------------
01:45:17,853 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:17,938 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:17,938 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:45:18,6 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:18,6 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 47%]
auth_test.py::TestAuthRoles::test_grant_revoke_role_validation 
-------------------------------- live log setup --------------------------------
01:45:34,837 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:34,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:34,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:45:34,989 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:34,990 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 48%]
auth_test.py::TestAuthRoles::test_list_roles 
-------------------------------- live log setup --------------------------------
01:45:52,328 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:45:52,414 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:52,414 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:45:52,484 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:45:52,485 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 49%]
auth_test.py::TestAuthRoles::test_grant_revoke_permissions 
-------------------------------- live log setup --------------------------------
01:46:09,811 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:09,895 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:09,895 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:46:09,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:09,963 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 50%]
auth_test.py::TestAuthRoles::test_filter_granted_permissions_by_resource_type 
-------------------------------- live log setup --------------------------------
01:46:27,47 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:27,137 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:27,138 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:46:27,206 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:27,207 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 51%]
auth_test.py::TestAuthRoles::test_list_permissions 
-------------------------------- live log setup --------------------------------
01:46:45,292 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:46:45,378 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:45,378 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:46:45,446 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:46:45,446 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 52%]
auth_test.py::TestAuthRoles::test_list_permissions_validation 
-------------------------------- live log setup --------------------------------
01:47:03,43 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:47:03,131 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:03,131 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:47:03,200 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:03,200 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 53%]
auth_test.py::TestAuthRoles::test_role_caching_authenticated_user 
-------------------------------- live log setup --------------------------------
01:47:20,536 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:47:20,621 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:20,621 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:47:20,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:20,689 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 54%]
auth_test.py::TestAuthRoles::test_drop_non_existent_role_should_not_update_cache 
-------------------------------- live log setup --------------------------------
01:47:41,300 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:47:41,385 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:41,385 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:47:41,453 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:41,453 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 55%]
auth_test.py::TestAuthRoles::test_prevent_circular_grants 
-------------------------------- live log setup --------------------------------
01:47:59,535 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:47:59,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:59,620 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:47:59,689 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:47:59,689 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 56%]
auth_test.py::TestAuthRoles::test_create_user_as_alias_for_create_role 
-------------------------------- live log setup --------------------------------
01:48:16,263 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:16,348 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:16,348 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:48:16,416 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:16,416 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 58%]
auth_test.py::TestAuthRoles::test_role_name 
-------------------------------- live log setup --------------------------------
01:48:33,25 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:33,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:33,111 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:48:33,186 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:33,186 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 59%]
auth_test.py::TestAuthRoles::test_role_requires_login_privilege_to_authenticate 
-------------------------------- live log setup --------------------------------
01:48:51,765 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:48:51,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:51,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:48:51,919 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:48:51,919 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 60%]
auth_test.py::TestAuthRoles::test_roles_do_not_inherit_login_privilege 
-------------------------------- live log setup --------------------------------
01:49:09,14 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:49:09,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:09,100 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:49:09,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:09,168 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 61%]
auth_test.py::TestAuthRoles::test_role_requires_password_to_login 
-------------------------------- live log setup --------------------------------
01:49:25,739 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:49:25,824 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:25,824 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:49:25,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:25,893 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 62%]
auth_test.py::TestAuthRoles::test_superuser_status_is_inherited 
-------------------------------- live log setup --------------------------------
01:49:42,721 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:49:42,807 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:42,807 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:49:42,875 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:42,875 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 63%]
auth_test.py::TestAuthRoles::test_list_users_considers_inherited_superuser_status 
-------------------------------- live log setup --------------------------------
01:49:59,703 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:49:59,788 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:49:59,788 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:50:00,11 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:00,12 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 64%]
auth_test.py::TestAuthRoles::test_grant_revoke_udf_permissions 
-------------------------------- live log setup --------------------------------
01:50:16,533 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:16,619 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:16,619 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:50:16,686 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:16,687 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 65%]
auth_test.py::TestAuthRoles::test_grant_revoke_are_idempotent 
-------------------------------- live log setup --------------------------------
01:50:34,271 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:34,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:34,357 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:50:34,428 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:34,429 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 66%]
auth_test.py::TestAuthRoles::test_function_resource_hierarchy_permissions 
-------------------------------- live log setup --------------------------------
01:50:51,508 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:50:51,593 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:51,593 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:50:51,661 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:50:51,661 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 67%]
auth_test.py::TestAuthRoles::test_udf_permissions_validation 
-------------------------------- live log setup --------------------------------
01:51:09,744 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:51:09,833 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:51:09,833 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:51:09,904 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:51:09,904 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 68%]
auth_test.py::TestAuthRoles::test_drop_role_cleans_up_udf_permissions 
-------------------------------- live log setup --------------------------------
01:51:27,993 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:51:28,79 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:51:28,79 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:51:28,148 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:51:28,148 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 69%]
auth_test.py::TestAuthRoles::test_drop_function_and_keyspace_cleans_up_udf_permissions 
-------------------------------- live log setup --------------------------------
01:51:45,475 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:51:45,561 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:51:45,561 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:51:45,629 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:51:45,629 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 70%]
auth_test.py::TestAuthRoles::test_udf_with_overloads_permissions 
-------------------------------- live log setup --------------------------------
01:52:03,714 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:03,799 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:03,799 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:52:03,866 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:03,867 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 72%]
auth_test.py::TestAuthRoles::test_drop_keyspace_cleans_up_function_level_permissions 
-------------------------------- live log setup --------------------------------
01:52:21,720 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:21,806 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:21,806 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:52:21,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:21,876 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 73%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_selection 
-------------------------------- live log setup --------------------------------
01:52:40,292 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:40,377 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:40,377 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:52:40,445 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:40,445 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 74%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_select_where_clause 
-------------------------------- live log setup --------------------------------
01:52:58,281 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:52:58,367 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:58,367 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:52:58,435 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:52:58,435 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 75%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_insert 
-------------------------------- live log setup --------------------------------
01:53:16,20 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:53:16,105 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:16,105 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:53:16,173 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:16,174 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 76%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_update 
-------------------------------- live log setup --------------------------------
01:53:34,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:53:34,113 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:34,113 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:53:34,181 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:34,181 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 77%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_delete 
-------------------------------- live log setup --------------------------------
01:53:52,18 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:53:52,104 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:52,105 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:53:52,172 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:53:52,173 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 78%]
auth_test.py::TestAuthRoles::test_inheritence_of_udf_permissions 
-------------------------------- live log setup --------------------------------
01:54:10,24 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:54:10,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:54:10,111 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:54:10,179 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:54:10,179 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 79%]
auth_test.py::TestAuthRoles::test_builtin_functions_require_no_special_permissions 
-------------------------------- live log setup --------------------------------
01:54:28,17 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:54:28,104 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:54:28,104 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:54:28,173 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:54:28,173 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 80%]
auth_test.py::TestAuthRoles::test_disallow_grant_revoke_on_builtin_functions 
-------------------------------- live log setup --------------------------------
01:54:45,252 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:54:45,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:54:45,338 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:54:45,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:54:45,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 81%]
auth_test.py::TestAuthRoles::test_disallow_grant_execute_on_non_function_resources 
-------------------------------- live log setup --------------------------------
01:55:01,992 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:02,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:02,77 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:55:02,145 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:02,145 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 82%]
auth_test.py::TestAuthRoles::test_aggregate_function_permissions 
-------------------------------- live log setup --------------------------------
01:55:18,974 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:19,59 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:19,59 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:55:19,128 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:19,128 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
-------------------------------- live log call ---------------------------------
01:55:37,108 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 83%]
auth_test.py::TestAuthRoles::test_ignore_invalid_roles 
-------------------------------- live log setup --------------------------------
01:55:37,875 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:37,963 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:37,963 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:55:38,31 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:38,31 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
PASSED                                                                   [ 84%]
auth_test.py::TestAuthUnavailable::test_authentication_handle_unavailable 
-------------------------------- live log call ---------------------------------
01:55:54,611 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:54,696 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:54,696 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:55:54,763 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:55:54,763 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:55:54,856 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:55:54,940 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:55:54,941 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:55:55,8 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:55:55,8 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:56:11,731 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 86%]
auth_test.py::TestAuthUnavailable::test_authentication_through_cache_handle_unavailable 
-------------------------------- live log call ---------------------------------
01:56:26,921 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:56:27,6 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:56:27,7 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:56:27,75 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:56:27,75 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:56:27,167 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:56:27,251 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:56:27,252 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:56:27,319 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:56:27,319 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:56:44,68 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 87%]
auth_test.py::TestAuthUnavailable::test_authentication_from_cache_while_unavailable 
-------------------------------- live log call ---------------------------------
01:57:00,998 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:57:01,83 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:57:01,83 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:01,151 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:57:01,151 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:01,243 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:57:01,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:57:01,329 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:01,397 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:57:01,397 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:18,102 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 88%]
auth_test.py::TestAuthUnavailable::test_credentials_cache_background_reload_handle_unavailable 
-------------------------------- live log call ---------------------------------
01:57:31,560 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:57:31,646 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:57:31,646 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:31,714 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:57:31,714 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:31,806 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:57:31,891 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:57:31,891 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:31,958 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:57:31,958 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:57:48,743 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 89%]
auth_test.py::TestAuthUnavailable::test_authorization_handle_unavailable 
-------------------------------- live log call ---------------------------------
01:58:08,888 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:58:08,978 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:58:08,978 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:09,46 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:58:09,46 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:09,140 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:58:09,224 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:58:09,225 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:09,292 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:58:09,292 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:26,6 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 90%]
auth_test.py::TestAuthUnavailable::test_authorization_through_cache_handle_unavailable 
-------------------------------- live log call ---------------------------------
01:58:39,695 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:58:39,782 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:58:39,782 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:39,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:58:39,850 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:39,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:58:40,33 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:58:40,33 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:40,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:58:40,101 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:58:56,877 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 91%]
auth_test.py::TestAuthUnavailable::test_authorization_from_cache_while_unavailable 
-------------------------------- live log call ---------------------------------
01:59:13,260 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:59:13,346 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:59:13,347 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:13,414 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:59:13,414 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:13,506 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:59:13,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:59:13,597 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:13,665 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:59:13,665 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:30,412 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 92%]
auth_test.py::TestAuthUnavailable::test_permission_cache_background_reload_handle_unavailable 
-------------------------------- live log call ---------------------------------
01:59:44,320 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:59:44,406 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:59:44,406 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:44,474 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
01:59:44,474 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:44,566 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
01:59:44,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:59:44,653 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
01:59:44,720 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
01:59:44,720 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:01,478 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 93%]
auth_test.py::TestNetworkAuth::test_full_dc_access 
-------------------------------- live log setup --------------------------------
02:00:22,403 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:00:22,489 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:00:22,489 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:22,558 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:00:22,558 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:22,650 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:00:22,734 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:00:22,734 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:22,801 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:00:22,802 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:39,579 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 94%]
auth_test.py::TestNetworkAuth::test_single_dc_access 
-------------------------------- live log setup --------------------------------
02:00:42,525 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:00:42,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:00:42,610 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:42,678 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:00:42,678 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:42,770 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:00:42,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:00:42,855 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:42,922 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:00:42,922 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:00:59,735 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 95%]
auth_test.py::TestNetworkAuth::test_revoked_dc_access 
-------------------------------- live log setup --------------------------------
02:01:02,427 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:01:02,512 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:01:02,512 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:02,580 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:01:02,580 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:02,673 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:01:02,757 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:01:02,758 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:02,825 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:01:02,825 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:19,652 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 96%]
auth_test.py::TestNetworkAuth::test_create_dc_validation 
-------------------------------- live log setup --------------------------------
02:01:26,827 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:01:26,915 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:01:26,915 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:26,986 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:01:26,986 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:27,79 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:01:27,164 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:01:27,164 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:27,232 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:01:27,232 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:44,32 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 97%]
auth_test.py::TestNetworkAuth::test_alter_dc_validation 
-------------------------------- live log setup --------------------------------
02:01:46,702 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:01:46,787 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:01:46,788 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:46,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:01:46,856 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:46,955 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:01:47,40 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:01:47,40 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:01:47,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:01:47,109 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:02:03,934 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 98%]
auth_test.py::TestNetworkAuth::test_revoked_login 
-------------------------------- live log setup --------------------------------
02:02:06,826 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:02:06,912 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:02:06,912 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:02:06,980 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
02:02:06,980 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:02:07,73 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
02:02:07,157 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:02:07,157 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:02:07,229 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
02:02:07,230 ccmlib.node WARNING [msx] ccmlib:node.py, sstable_preemptive_open_interval_in_mb = 50
02:02:24,36 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [100%]
===Flaky Test Report===

test_system_auth_ks_is_alterable passed 1 out of the required 1 times. Success!
test_login passed 1 out of the required 1 times. Success!
test_cant_create_existing_user passed 1 out of the required 1 times. Success!
test_list_users passed 1 out of the required 1 times. Success!
test_handle_corrupt_role_data passed 1 out of the required 1 times. Success!
test_user_cant_drop_themselves passed 1 out of the required 1 times. Success!
test_dropping_nonexistent_user_throws_exception passed 1 out of the required 1 times. Success!
test_drop_user_case_sensitive passed 1 out of the required 1 times. Success!
test_alter_user_case_sensitive passed 1 out of the required 1 times. Success!
test_regular_users_can_alter_their_passwords_only passed 1 out of the required 1 times. Success!
test_users_cant_alter_their_superuser_status passed 1 out of the required 1 times. Success!
test_only_superuser_alters_superuser_status passed 1 out of the required 1 times. Success!
test_altering_nonexistent_user_throws_exception passed 1 out of the required 1 times. Success!
test_conditional_create_drop_user passed 1 out of the required 1 times. Success!
test_create_ks_auth passed 1 out of the required 1 times. Success!
test_create_cf_auth passed 1 out of the required 1 times. Success!
test_alter_ks_auth passed 1 out of the required 1 times. Success!
test_alter_cf_auth passed 1 out of the required 1 times. Success!
test_materialized_views_auth passed 1 out of the required 1 times. Success!
test_drop_ks_auth passed 1 out of the required 1 times. Success!
test_drop_cf_auth passed 1 out of the required 1 times. Success!
test_modify_and_select_auth passed 1 out of the required 1 times. Success!
test_grant_revoke_without_ks_specified passed 1 out of the required 1 times. Success!
test_grant_revoke_auth passed 1 out of the required 1 times. Success!
test_grant_revoke_nonexistent_user_or_ks passed 1 out of the required 1 times. Success!
test_grant_revoke_cleanup passed 1 out of the required 1 times. Success!
test_permissions_caching passed 1 out of the required 1 times. Success!
test_list_permissions passed 1 out of the required 1 times. Success!
test_type_auth passed 1 out of the required 1 times. Success!
test_restart_node_doesnt_lose_auth_data passed 1 out of the required 1 times. Success!
test_auth_metrics passed 1 out of the required 1 times. Success!
test_create_drop_role passed 1 out of the required 1 times. Success!
test_conditional_create_drop_role passed 1 out of the required 1 times. Success!
test_create_drop_role_validation passed 1 out of the required 1 times. Success!
test_role_admin_validation passed 1 out of the required 1 times. Success!
test_creator_of_db_resource_granted_all_permissions passed 1 out of the required 1 times. Success!
test_create_and_grant_roles_with_superuser_status passed 1 out of the required 1 times. Success!
test_drop_and_revoke_roles_with_superuser_status passed 1 out of the required 1 times. Success!
test_drop_role_removes_memberships passed 1 out of the required 1 times. Success!
test_drop_role_revokes_permissions_granted_on_it passed 1 out of the required 1 times. Success!
test_grant_revoke_roles passed 1 out of the required 1 times. Success!
test_grant_revoke_role_validation passed 1 out of the required 1 times. Success!
test_list_roles passed 1 out of the required 1 times. Success!
test_grant_revoke_permissions passed 1 out of the required 1 times. Success!
test_filter_granted_permissions_by_resource_type passed 1 out of the required 1 times. Success!
test_list_permissions passed 1 out of the required 1 times. Success!
test_list_permissions_validation passed 1 out of the required 1 times. Success!
test_role_caching_authenticated_user passed 1 out of the required 1 times. Success!
test_drop_non_existent_role_should_not_update_cache passed 1 out of the required 1 times. Success!
test_prevent_circular_grants passed 1 out of the required 1 times. Success!
test_create_user_as_alias_for_create_role passed 1 out of the required 1 times. Success!
test_role_name passed 1 out of the required 1 times. Success!
test_role_requires_login_privilege_to_authenticate passed 1 out of the required 1 times. Success!
test_roles_do_not_inherit_login_privilege passed 1 out of the required 1 times. Success!
test_role_requires_password_to_login passed 1 out of the required 1 times. Success!
test_superuser_status_is_inherited passed 1 out of the required 1 times. Success!
test_list_users_considers_inherited_superuser_status passed 1 out of the required 1 times. Success!
test_grant_revoke_udf_permissions passed 1 out of the required 1 times. Success!
test_grant_revoke_are_idempotent passed 1 out of the required 1 times. Success!
test_function_resource_hierarchy_permissions passed 1 out of the required 1 times. Success!
test_udf_permissions_validation passed 1 out of the required 1 times. Success!
test_drop_role_cleans_up_udf_permissions passed 1 out of the required 1 times. Success!
test_drop_function_and_keyspace_cleans_up_udf_permissions passed 1 out of the required 1 times. Success!
test_udf_with_overloads_permissions passed 1 out of the required 1 times. Success!
test_drop_keyspace_cleans_up_function_level_permissions passed 1 out of the required 1 times. Success!
test_udf_permissions_in_selection passed 1 out of the required 1 times. Success!
test_udf_permissions_in_select_where_clause passed 1 out of the required 1 times. Success!
test_udf_permissions_in_insert passed 1 out of the required 1 times. Success!
test_udf_permissions_in_update passed 1 out of the required 1 times. Success!
test_udf_permissions_in_delete passed 1 out of the required 1 times. Success!
test_inheritence_of_udf_permissions passed 1 out of the required 1 times. Success!
test_builtin_functions_require_no_special_permissions passed 1 out of the required 1 times. Success!
test_disallow_grant_revoke_on_builtin_functions passed 1 out of the required 1 times. Success!
test_disallow_grant_execute_on_non_function_resources passed 1 out of the required 1 times. Success!
test_aggregate_function_permissions passed 1 out of the required 1 times. Success!
test_ignore_invalid_roles passed 1 out of the required 1 times. Success!
test_authentication_handle_unavailable passed 1 out of the required 1 times. Success!
test_authentication_through_cache_handle_unavailable passed 1 out of the required 1 times. Success!
test_authentication_from_cache_while_unavailable passed 1 out of the required 1 times. Success!
test_credentials_cache_background_reload_handle_unavailable passed 1 out of the required 1 times. Success!
test_authorization_handle_unavailable passed 1 out of the required 1 times. Success!
test_authorization_through_cache_handle_unavailable passed 1 out of the required 1 times. Success!
test_authorization_from_cache_while_unavailable passed 1 out of the required 1 times. Success!
test_permission_cache_background_reload_handle_unavailable passed 1 out of the required 1 times. Success!
test_full_dc_access passed 1 out of the required 1 times. Success!
test_single_dc_access passed 1 out of the required 1 times. Success!
test_revoked_dc_access passed 1 out of the required 1 times. Success!
test_create_dc_validation passed 1 out of the required 1 times. Success!
test_alter_dc_validation passed 1 out of the required 1 times. Success!
test_revoked_login passed 1 out of the required 1 times. Success!

===End Flaky Test Report===

=================== 90 passed, 3 skipped in 1909.00 seconds ====================
[msx] rc = 0
