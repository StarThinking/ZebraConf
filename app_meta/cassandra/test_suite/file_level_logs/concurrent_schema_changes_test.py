cassandra concurrent_schema_changes_test.py true true
the_test is concurrent_schema_changes_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 13 items

concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_create_lots_of_tables_concurrently SKIPPED [  7%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_create_lots_of_alters_concurrently SKIPPED [ 15%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_create_lots_of_indexes_concurrently SKIPPED [ 23%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_create_lots_of_mv_concurrently SKIPPED [ 30%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_create_lots_of_schema_churn SKIPPED [ 38%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_create_lots_of_schema_churn_with_node_down SKIPPED [ 46%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_basic SKIPPED [ 53%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_changes_to_different_nodes SKIPPED [ 61%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_changes_while_node_down SKIPPED [ 69%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_changes_while_node_toggle SKIPPED [ 76%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_decommission_node SKIPPED [ 84%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_snapshot SKIPPED [ 92%]
concurrent_schema_changes_test.py::TestConcurrentSchemaChanges::test_load SKIPPED [100%]

========================== 13 skipped in 0.31 seconds ==========================
[msx] rc = 0
