#!/bin/bash

#for component in NameNode DataNode JournalNode
#do
#    for t in $(cat all_tests_in_bc.txt); do if [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/restart.txt)" == "" ] && [ "$(grep $t ~/parameter_test_controller/tests/hdfs/$component/start.txt)" != "" ]; then echo $t; fi; done | sort -u > bc_coevers_"$component"_soely_start_test.txt
#done


for t in *
do
    #bc_line=$(grep -n 'before_class' $t | awk -F ':' '{print $1}')
    first_test_line=$(grep -n 'unitTestCounterInClass = 0' $t | awk -F ':' '{print $1}')
    echo first_test_line = $first_test_line
    cat $t | head -n $first_test_line >> ../$t
done
