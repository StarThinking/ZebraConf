#!/bin/bash

correct_tests_path=$1

cat $correct_tests_path | sort -u | awk -F '#' '{print $1}' | sort -u | while read class; do tests=( $( grep ^"$class"'#' $correct_tests_path) ); echo -n "$class"'#zebraconf_class_test '; for test in ${tests[@]}; do echo -n "$test"',' ; done; echo ''; done | sed 's/,$//g'
