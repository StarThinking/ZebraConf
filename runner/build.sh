#!/bin/bash

# clean target directory
rm -f ./target/*.class
rm -f ./target/*.txt

# build
javac -cp $ZEBRACONF_HOME/runner/lib/commons-math3-3.6.1.jar $ZEBRACONF_HOME/runner/src/*.java -d $ZEBRACONF_HOME/runner/target/
