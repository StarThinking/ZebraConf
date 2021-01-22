#!/bin/bash

component=NameNode
for t in $(cat all_tests_in_init_bc.txt); do if [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/restart.txt.origin)" == "" ] && [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/start.txt)" != "" ]; then echo $t; fi; done | sort -u > init_bc_coevers_"$component"_soely_start_test.txt

for t in $(cat all_tests_in_init_bc.txt); do if [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/restart.txt.origin)" != "" ]; then echo $t; fi; done | sort -u > init_bc_coevers_"$component"_restart_test.txt

for component in DataNode JournalNode
do
    for t in $(cat all_tests_in_init_bc.txt); do if [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/restart.txt)" == "" ] && [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/start.txt)" != "" ]; then echo $t; fi; done | sort -u > init_bc_coevers_"$component"_soely_start_test.txt
    for t in $(cat all_tests_in_init_bc.txt); do if [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/restart.txt)" != "" ]; then echo $t; fi; done | sort -u > init_bc_coevers_"$component"_restart_test.txt
done
