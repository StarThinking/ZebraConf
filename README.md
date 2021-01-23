ZebraConf
===============
This repository contains scripts and other supplementary material
for the EuroSys'21 artifact evaluation of the paper **Finding Unsafe Heterogeneous Configurations in Cloud Systems** 
by Sixiang Ma, Fang Zhou, Michael D. Bond, and Yang Wang.

The scripts can be used to reproduce the results in the paper.

Authors
------- 
 * Sixiang Ma (The Ohio State University)
 * Fang Zhou (The Ohio State University)
 * Michael D. Bond (The Ohio State University)
 * Yang Wang (The Ohio State University)

Directory Structure
-------------------
 * `app_meta` contains the metadata information about the applications. Currently, we have applied ZebraConf to 4 popular applications (HDFS, YARN, MR, HBASE). The metadata information will be used by scripts to set up testing environment.
 * `agent` contains the source code of ConfAgent module in ConfAgent.java and a utility class TimedOutTestsListener.java which can fetch unit tests' error report to ease debug. 
 * `runner` contains the source code of TestRunner, the external library, the shared files used to communicate with ConfAgent, and utility scripts for cluster testing. Users can use run_heter_conf_test.sh to test a heterogeneous test case.
 * `test_gen` contains .
 * `analysis_data` contains .

Hardware Dependencies
-------------------
None.

Software Dependencies
---------------------
The scripts, compilation and binaries are tested on Ubuntu 18.04 LTS. 
Other Linux distributions may work, but are not tested.

Compilation
---------------------
To use Zebra


Running the Experiments
---------------------

Paper Citation
---------------------
