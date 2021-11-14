#!/bin/bash

cd ~/cassandra-dtest 
pytest --log-cli-level=WARN --cassandra-dir=/users/masix/cassandra pending_range_test.py::TestPendingRangeMovements::test_pending_range
