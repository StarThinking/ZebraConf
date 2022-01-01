cassandra token_generator_test.py true true
the_test is token_generator_test.py
============================= test session starts ==============================
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.11.0, pluggy-0.7.1 -- /users/masix/dtest/bin/python
cachedir: .pytest_cache
rootdir: /users/masix/cassandra-dtest, inifile: pytest.ini
plugins: timeout-1.4.2, repeat-0.9.1, flaky-3.7.0
timeout: 900.0s
timeout method: signal
timeout func_only: False
collecting ... collected 3 items

token_generator_test.py::TestTokenGenerator::test_multi_dc_tokens_default SKIPPED [ 33%]
token_generator_test.py::TestTokenGenerator::test_multi_dc_tokens_murmur3 SKIPPED [ 66%]
token_generator_test.py::TestTokenGenerator::test_multi_dc_tokens_random SKIPPED [100%]

========================== 3 skipped in 1.02 seconds ===========================
[msx] rc = 0
