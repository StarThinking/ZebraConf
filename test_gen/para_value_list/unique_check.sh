#!/bin/bash

cat $(find . -name '*.txt*') | awk '{print $1}' | sort | uniq -c | grep -v 1
