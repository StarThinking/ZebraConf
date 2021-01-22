#!/bin/bash

rm ~/parameter_test_controller/target/*.class
#rm ~/parameter_test_controller/target/*.txt

javac -cp ~/parameter_test_controller/src/lib/commons-math3-3.6.1.jar ~/parameter_test_controller/src/*.java -d ~/parameter_test_controller/target/
