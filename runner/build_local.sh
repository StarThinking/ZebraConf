#!/bin/bash

# clean target directory
rm -f ./target/*.class
rm -f ./target/*.txt

# build
javac -cp /root/vm_images/ZebraConf/runner/lib/commons-math3-3.6.1.jar /root/vm_images/ZebraConf/runner/src/*.java -d /root/vm_images/ZebraConf/runner/target/
