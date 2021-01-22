#!/bin/bash

# clean target directory
rm -f ./target/*.class
rm -f ./target/*.txt

# build
javac -cp /root/ZebraConf/runner/lib/commons-math3-3.6.1.jar /root/ZebraConf/runner/src/*.java -d /root/ZebraConf/runner/target/
