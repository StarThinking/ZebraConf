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
15:28:20,750 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:28:20,835 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:28:20,903 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:28:20,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:28:21,77 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:28:21,143 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:28:21,234 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:28:21,316 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
15:28:21,383 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node3
15:28:38,863 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [  1%]
auth_test.py::TestAuth::test_login 
-------------------------------- live log call ---------------------------------
15:29:40,783 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:29:40,868 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:29:40,937 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  2%]
auth_test.py::TestAuth::test_only_superuser_can_create_users SKIPPED     [  3%]
auth_test.py::TestAuth::test_password_authenticator_create_user_requires_password SKIPPED [  4%]
auth_test.py::TestAuth::test_cant_create_existing_user 
-------------------------------- live log call ---------------------------------
15:30:58,281 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:30:58,366 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:30:58,470 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  5%]
auth_test.py::TestAuth::test_list_users 
-------------------------------- live log call ---------------------------------
15:31:15,262 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:31:15,346 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:31:15,413 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  6%]
auth_test.py::TestAuth::test_handle_corrupt_role_data 
-------------------------------- live log call ---------------------------------
15:31:32,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:31:32,860 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:31:32,932 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:31:49,572 cassandra.cluster WARNING Host 127.0.0.1:9042 error: Server error.
PASSED                                                                   [  7%]
auth_test.py::TestAuth::test_user_cant_drop_themselves 
-------------------------------- live log call ---------------------------------
15:31:50,242 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:31:50,329 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:31:50,396 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [  8%]
auth_test.py::TestAuth::test_only_superusers_can_drop_users SKIPPED      [  9%]
auth_test.py::TestAuth::test_dropping_nonexistent_user_throws_exception 
-------------------------------- live log call ---------------------------------
15:32:07,285 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:32:07,369 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:32:07,439 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 10%]
auth_test.py::TestAuth::test_drop_user_case_sensitive 
-------------------------------- live log call ---------------------------------
15:32:24,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:32:24,101 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:32:24,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 11%]
auth_test.py::TestAuth::test_alter_user_case_sensitive 
-------------------------------- live log call ---------------------------------
15:32:40,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:32:41,78 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:32:41,145 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 12%]
auth_test.py::TestAuth::test_regular_users_can_alter_their_passwords_only 
-------------------------------- live log call ---------------------------------
15:32:58,252 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:32:58,336 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:32:58,402 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 13%]
auth_test.py::TestAuth::test_users_cant_alter_their_superuser_status 
-------------------------------- live log call ---------------------------------
15:33:17,712 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:33:17,796 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:33:17,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 15%]
auth_test.py::TestAuth::test_only_superuser_alters_superuser_status 
-------------------------------- live log call ---------------------------------
15:33:34,456 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:33:34,541 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:33:34,610 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 16%]
auth_test.py::TestAuth::test_altering_nonexistent_user_throws_exception 
-------------------------------- live log call ---------------------------------
15:33:51,692 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:33:51,777 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:33:51,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 17%]
auth_test.py::TestAuth::test_conditional_create_drop_user 
-------------------------------- live log call ---------------------------------
15:34:08,441 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:34:08,528 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:34:08,597 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 18%]
auth_test.py::TestAuth::test_create_ks_auth 
-------------------------------- live log call ---------------------------------
15:34:25,753 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:34:25,839 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:34:25,905 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 19%]
auth_test.py::TestAuth::test_create_cf_auth 
-------------------------------- live log call ---------------------------------
15:34:43,238 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:34:43,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:34:43,391 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 20%]
auth_test.py::TestAuth::test_alter_ks_auth 
-------------------------------- live log call ---------------------------------
15:35:00,733 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:35:00,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:35:00,884 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:35:17,728 cassandra.protocol WARNING Server warning: Your replication factor 2 for keyspace ks is higher than the number of nodes 1
15:35:17,729 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 21%]
auth_test.py::TestAuth::test_alter_cf_auth 
-------------------------------- live log call ---------------------------------
15:35:18,230 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:35:18,313 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:35:18,380 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 22%]
auth_test.py::TestAuth::test_materialized_views_auth 
-------------------------------- live log call ---------------------------------
15:35:36,494 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:35:36,578 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:35:36,645 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:35:53,675 cassandra.protocol WARNING Server warning: Materialized views are experimental and are not recommended for production use.
PASSED                                                                   [ 23%]
auth_test.py::TestAuth::test_drop_ks_auth 
-------------------------------- live log call ---------------------------------
15:35:54,733 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:35:54,817 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:35:54,885 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 24%]
auth_test.py::TestAuth::test_drop_cf_auth 
-------------------------------- live log call ---------------------------------
15:36:12,473 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:36:12,562 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:36:12,630 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 25%]
auth_test.py::TestAuth::test_modify_and_select_auth 
-------------------------------- live log call ---------------------------------
15:36:30,468 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:36:30,553 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:36:30,620 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 26%]
auth_test.py::TestAuth::test_grant_revoke_without_ks_specified 
-------------------------------- live log call ---------------------------------
15:36:48,215 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:36:48,300 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:36:48,371 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 27%]
auth_test.py::TestAuth::test_grant_revoke_auth 
-------------------------------- live log call ---------------------------------
15:37:06,206 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:37:06,290 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:37:06,357 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 29%]
auth_test.py::TestAuth::test_grant_revoke_nonexistent_user_or_ks 
-------------------------------- live log call ---------------------------------
15:37:24,199 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:37:24,284 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:37:24,355 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 30%]
auth_test.py::TestAuth::test_grant_revoke_cleanup 
-------------------------------- live log call ---------------------------------
15:37:41,185 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:37:41,269 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:37:41,335 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 31%]
auth_test.py::TestAuth::test_permissions_caching 
-------------------------------- live log call ---------------------------------
15:37:59,926 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:38:00,9 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:38:00,76 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 32%]
auth_test.py::TestAuth::test_list_permissions 
-------------------------------- live log call ---------------------------------
15:38:20,169 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:38:20,253 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:38:20,320 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 33%]
auth_test.py::TestAuth::test_type_auth 
-------------------------------- live log call ---------------------------------
15:38:37,907 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:38:37,991 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:38:38,57 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 34%]
auth_test.py::TestAuth::test_restart_node_doesnt_lose_auth_data 
-------------------------------- live log call ---------------------------------
15:38:55,674 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:38:55,759 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:38:55,826 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:39:13,798 cassandra.cluster WARNING Host 127.0.0.1:9042 has been marked down
15:39:14,904 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 2.28 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
15:39:17,211 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 4.16 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
15:39:19,727 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:39:19,819 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:39:21,436 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 8.72 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
15:39:30,158 cassandra.pool WARNING Error attempting to reconnect to 127.0.0.1:9042, scheduling retry in 14.24 seconds: [Errno 111] Tried connecting to [('127.0.0.1', 9042)]. Last error: Connection refused
15:39:33,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:39:33,340 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 35%]
auth_test.py::TestAuth::test_auth_metrics 
-------------------------------- live log call ---------------------------------
15:39:40,752 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:39:40,840 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:39:40,908 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 36%]
auth_test.py::TestAuthRoles::test_create_drop_role 
-------------------------------- live log setup --------------------------------
15:40:19,37 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:40:19,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:40:19,189 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 37%]
auth_test.py::TestAuthRoles::test_conditional_create_drop_role 
-------------------------------- live log setup --------------------------------
15:40:35,521 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:40:35,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:40:35,674 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 38%]
auth_test.py::TestAuthRoles::test_create_drop_role_validation 
-------------------------------- live log setup --------------------------------
15:40:52,523 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:40:52,606 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:40:52,675 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 39%]
auth_test.py::TestAuthRoles::test_role_admin_validation 
-------------------------------- live log setup --------------------------------
15:41:09,754 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:41:09,838 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:41:09,906 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 40%]
auth_test.py::TestAuthRoles::test_creator_of_db_resource_granted_all_permissions 
-------------------------------- live log setup --------------------------------
15:41:29,766 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:41:29,850 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:41:29,918 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 41%]
auth_test.py::TestAuthRoles::test_create_and_grant_roles_with_superuser_status 
-------------------------------- live log setup --------------------------------
15:41:48,263 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:41:48,347 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:41:48,415 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 43%]
auth_test.py::TestAuthRoles::test_drop_and_revoke_roles_with_superuser_status 
-------------------------------- live log setup --------------------------------
15:42:05,771 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:42:05,855 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:42:05,927 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 44%]
auth_test.py::TestAuthRoles::test_drop_role_removes_memberships 
-------------------------------- live log setup --------------------------------
15:42:23,253 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:42:23,337 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:42:23,405 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 45%]
auth_test.py::TestAuthRoles::test_drop_role_revokes_permissions_granted_on_it 
-------------------------------- live log setup --------------------------------
15:42:40,496 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:42:40,580 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:42:40,648 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 46%]
auth_test.py::TestAuthRoles::test_grant_revoke_roles 
-------------------------------- live log setup --------------------------------
15:42:57,482 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:42:57,567 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:42:57,636 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 47%]
auth_test.py::TestAuthRoles::test_grant_revoke_role_validation 
-------------------------------- live log setup --------------------------------
15:43:14,735 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:43:14,819 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:43:14,890 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 48%]
auth_test.py::TestAuthRoles::test_list_roles 
-------------------------------- live log setup --------------------------------
15:43:32,249 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:43:32,333 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:43:32,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 49%]
auth_test.py::TestAuthRoles::test_grant_revoke_permissions 
-------------------------------- live log setup --------------------------------
15:43:49,762 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:43:49,847 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:43:49,915 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 50%]
auth_test.py::TestAuthRoles::test_filter_granted_permissions_by_resource_type 
-------------------------------- live log setup --------------------------------
15:44:07,502 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:44:07,586 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:44:07,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 51%]
auth_test.py::TestAuthRoles::test_list_permissions 
-------------------------------- live log setup --------------------------------
15:44:25,742 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:44:25,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:44:25,895 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 52%]
auth_test.py::TestAuthRoles::test_list_permissions_validation 
-------------------------------- live log setup --------------------------------
15:44:43,484 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:44:43,568 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:44:43,635 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 53%]
auth_test.py::TestAuthRoles::test_role_caching_authenticated_user 
-------------------------------- live log setup --------------------------------
15:45:01,772 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:45:01,856 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:45:01,924 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 54%]
auth_test.py::TestAuthRoles::test_drop_non_existent_role_should_not_update_cache 
-------------------------------- live log setup --------------------------------
15:45:22,792 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:45:22,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:45:22,950 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 55%]
auth_test.py::TestAuthRoles::test_prevent_circular_grants 
-------------------------------- live log setup --------------------------------
15:45:41,792 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:45:41,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:45:41,944 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 56%]
auth_test.py::TestAuthRoles::test_create_user_as_alias_for_create_role 
-------------------------------- live log setup --------------------------------
15:45:58,788 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:45:58,877 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:45:58,947 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 58%]
auth_test.py::TestAuthRoles::test_role_name 
-------------------------------- live log setup --------------------------------
15:46:16,27 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:46:16,111 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:46:16,180 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 59%]
auth_test.py::TestAuthRoles::test_role_requires_login_privilege_to_authenticate 
-------------------------------- live log setup --------------------------------
15:46:35,272 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:46:35,356 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:46:35,426 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 60%]
auth_test.py::TestAuthRoles::test_roles_do_not_inherit_login_privilege 
-------------------------------- live log setup --------------------------------
15:46:53,15 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:46:53,99 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:46:53,168 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 61%]
auth_test.py::TestAuthRoles::test_role_requires_password_to_login 
-------------------------------- live log setup --------------------------------
15:47:10,248 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:47:10,332 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:47:10,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 62%]
auth_test.py::TestAuthRoles::test_superuser_status_is_inherited 
-------------------------------- live log setup --------------------------------
15:47:27,479 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:47:27,564 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:47:27,635 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 63%]
auth_test.py::TestAuthRoles::test_list_users_considers_inherited_superuser_status 
-------------------------------- live log setup --------------------------------
15:47:44,968 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:47:45,52 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:47:45,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 64%]
auth_test.py::TestAuthRoles::test_grant_revoke_udf_permissions 
-------------------------------- live log setup --------------------------------
15:48:01,954 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:48:02,38 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:48:02,109 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 65%]
auth_test.py::TestAuthRoles::test_grant_revoke_are_idempotent 
-------------------------------- live log setup --------------------------------
15:48:19,947 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:48:20,32 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:48:20,100 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 66%]
auth_test.py::TestAuthRoles::test_function_resource_hierarchy_permissions 
-------------------------------- live log setup --------------------------------
15:48:37,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:48:37,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:48:37,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 67%]
auth_test.py::TestAuthRoles::test_udf_permissions_validation 
-------------------------------- live log setup --------------------------------
15:48:56,189 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:48:56,274 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:48:56,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 68%]
auth_test.py::TestAuthRoles::test_drop_role_cleans_up_udf_permissions 
-------------------------------- live log setup --------------------------------
15:49:14,691 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:49:14,776 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:49:14,845 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 69%]
auth_test.py::TestAuthRoles::test_drop_function_and_keyspace_cleans_up_udf_permissions 
-------------------------------- live log setup --------------------------------
15:49:32,692 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:49:32,775 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:49:32,843 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 70%]
auth_test.py::TestAuthRoles::test_udf_with_overloads_permissions 
-------------------------------- live log setup --------------------------------
15:49:51,190 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:49:51,274 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:49:51,342 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 72%]
auth_test.py::TestAuthRoles::test_drop_keyspace_cleans_up_function_level_permissions 
-------------------------------- live log setup --------------------------------
15:50:09,200 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:50:09,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:50:09,353 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 73%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_selection 
-------------------------------- live log setup --------------------------------
15:50:27,709 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:50:27,793 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:50:27,861 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 74%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_select_where_clause 
-------------------------------- live log setup --------------------------------
15:50:45,701 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:50:45,786 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:50:45,853 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 75%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_insert 
-------------------------------- live log setup --------------------------------
15:51:03,696 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:51:03,780 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:51:03,849 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 76%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_update 
-------------------------------- live log setup --------------------------------
15:51:21,687 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:51:21,771 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:51:21,844 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 77%]
auth_test.py::TestAuthRoles::test_udf_permissions_in_delete 
-------------------------------- live log setup --------------------------------
15:51:39,797 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:51:39,880 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:51:39,948 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 78%]
auth_test.py::TestAuthRoles::test_inheritence_of_udf_permissions 
-------------------------------- live log setup --------------------------------
15:51:58,39 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:51:58,122 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:51:58,191 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 79%]
auth_test.py::TestAuthRoles::test_builtin_functions_require_no_special_permissions 
-------------------------------- live log setup --------------------------------
15:52:16,305 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:52:16,389 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:52:16,458 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 80%]
auth_test.py::TestAuthRoles::test_disallow_grant_revoke_on_builtin_functions 
-------------------------------- live log setup --------------------------------
15:52:33,789 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:52:33,873 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:52:33,941 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 81%]
auth_test.py::TestAuthRoles::test_disallow_grant_execute_on_non_function_resources 
-------------------------------- live log setup --------------------------------
15:52:51,277 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:52:51,361 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:52:51,429 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 82%]
auth_test.py::TestAuthRoles::test_aggregate_function_permissions 
-------------------------------- live log setup --------------------------------
15:53:08,517 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:53:08,600 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:53:08,669 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
-------------------------------- live log call ---------------------------------
15:53:26,849 cassandra.protocol WARNING Server warning: Aggregation query used without partition key
PASSED                                                                   [ 83%]
auth_test.py::TestAuthRoles::test_ignore_invalid_roles 
-------------------------------- live log setup --------------------------------
15:53:27,515 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:53:27,599 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:53:27,668 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
PASSED                                                                   [ 84%]
auth_test.py::TestAuthUnavailable::test_authentication_handle_unavailable 
-------------------------------- live log call ---------------------------------
15:53:44,501 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:53:44,584 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:53:44,652 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:53:44,744 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:53:44,827 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:53:44,893 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:54:02,67 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 86%]
auth_test.py::TestAuthUnavailable::test_authentication_through_cache_handle_unavailable 
-------------------------------- live log call ---------------------------------
15:54:18,327 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:54:18,411 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:54:18,478 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:54:18,571 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:54:18,654 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:54:18,722 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:54:35,831 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 87%]
auth_test.py::TestAuthUnavailable::test_authentication_from_cache_while_unavailable 
-------------------------------- live log call ---------------------------------
15:54:53,414 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:54:53,499 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:54:53,567 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:54:53,660 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:54:53,743 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:54:53,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:55:10,948 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 88%]
auth_test.py::TestAuthUnavailable::test_credentials_cache_background_reload_handle_unavailable 
-------------------------------- live log call ---------------------------------
15:55:25,724 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:55:25,808 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:55:25,876 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:55:25,970 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:55:26,53 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:55:26,121 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:55:43,241 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 89%]
auth_test.py::TestAuthUnavailable::test_authorization_handle_unavailable 
-------------------------------- live log call ---------------------------------
15:56:03,579 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:56:03,667 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:56:03,737 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:56:03,830 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:56:03,913 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:56:03,981 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:56:21,123 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 90%]
auth_test.py::TestAuthUnavailable::test_authorization_through_cache_handle_unavailable 
-------------------------------- live log call ---------------------------------
15:56:36,620 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:56:36,704 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:56:36,772 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:56:36,870 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:56:36,953 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:56:37,21 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:56:54,438 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 91%]
auth_test.py::TestAuthUnavailable::test_authorization_from_cache_while_unavailable 
-------------------------------- live log call ---------------------------------
15:57:10,56 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:57:10,145 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:57:10,214 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:57:10,318 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:57:10,401 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:57:10,468 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:57:27,611 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 92%]
auth_test.py::TestAuthUnavailable::test_permission_cache_background_reload_handle_unavailable 
-------------------------------- live log call ---------------------------------
15:57:43,134 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:57:43,218 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:57:43,285 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:57:43,382 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:57:43,467 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:57:43,535 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:58:00,660 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 93%]
auth_test.py::TestNetworkAuth::test_full_dc_access 
-------------------------------- live log setup --------------------------------
15:58:21,726 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:58:21,811 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:58:21,879 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:58:21,973 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:58:22,62 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:58:22,131 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:58:39,291 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 94%]
auth_test.py::TestNetworkAuth::test_single_dc_access 
-------------------------------- live log setup --------------------------------
15:58:42,869 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:58:42,955 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:58:43,23 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:58:43,117 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:58:43,202 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:58:43,270 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:59:00,415 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 95%]
auth_test.py::TestNetworkAuth::test_revoked_dc_access 
-------------------------------- live log setup --------------------------------
15:59:02,994 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:59:03,78 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:59:03,146 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:59:03,241 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:59:03,324 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:59:03,392 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:59:20,518 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 96%]
auth_test.py::TestNetworkAuth::test_create_dc_validation 
-------------------------------- live log setup --------------------------------
15:59:27,149 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:59:27,234 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:59:27,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:59:27,399 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:59:27,483 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:59:27,551 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:59:44,682 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 97%]
auth_test.py::TestNetworkAuth::test_alter_dc_validation 
-------------------------------- live log setup --------------------------------
15:59:47,528 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:59:47,616 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:59:47,687 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
15:59:47,781 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
15:59:47,864 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
15:59:47,933 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:00:05,85 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
PASSED                                                                   [ 98%]
auth_test.py::TestNetworkAuth::test_revoked_login 
-------------------------------- live log setup --------------------------------
16:00:07,901 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:00:07,985 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:00:08,54 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node1
16:00:08,149 ccmlib.node WARNING [msx] ccmlib:copy_config_files.py, conf_dir = /users/masix/cassandra/conf
16:00:08,236 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:00:08,305 ccmlib.node WARNING [msx] ccmlib:node.py, self.name = node2
16:00:25,434 cassandra.protocol WARNING Server warning: When increasing replication factor you need to run a full (-full) repair to distribute the data.
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

=================== 90 passed, 3 skipped in 1932.18 seconds ====================
[msx] rc = 0
