cassandra putget_test.py true true
the_test is putget_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 7 items

putget_test.py::TestPutGet::test_putget SKIPPED                          [ 14%]
putget_test.py::TestPutGet::test_putget_snappy SKIPPED                   [ 28%]
putget_test.py::TestPutGet::test_putget_deflate SKIPPED                  [ 42%]
putget_test.py::TestPutGet::test_non_local_read SKIPPED                  [ 57%]
putget_test.py::TestPutGet::test_rangeputget SKIPPED                     [ 71%]
putget_test.py::TestPutGet::test_wide_row SKIPPED                        [ 85%]
putget_test.py::TestPutGet::test_wide_slice SKIPPED                      [100%]

========================== 7 skipped in 2.54 seconds ===========================
[msx] rc = 0
