#!/bin/bash

# clean target directory
rm -f ./target/*.class
rm -f ./target/*.txt

# build
javac -cp ~/ZebraConf/runner/lib/commons-math3-3.6.1.jar ~/ZebraConf/runner/src/*.java -d ~/ZebraConf/runner/target/
