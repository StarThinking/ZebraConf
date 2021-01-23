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
 * `app_meta` contains the metadata information about the four applications (HDFS, YARN, MR, HBASE) we applied. The information will be used to set up testing environment.
 * `agent` contains the source code of ConfAgent module and a utility class to fetch unit tests' error report to ease debug. 
 * `runner` contains the source code of TestRunner, the library, the shared files used to communicate with ConfAgent,  the script to run heterogeneous tests, and scripts for cluster testing.
 * `test_gen` contains .
 * `analysis_data` contains .

Hardware Dependencies
-------------------
None.

Software Dependencies
---------------------
* Dependencies to compile and run the application.
* Docker if users want to use our testing environment.

Set up Testing Environment
---------------------
To let users instantly try ZebraConf, we have provided a Docker image (11.17 GB) that encapsulates all our testing environment. Currently, users can run heterogeneous configuration tests with HDFS, YARN, MR, HBASE. 

Command to create docker container:
```
$ docker run -d -it --name [YOUR_CONTAINER_NAME] sixiangma/reconf_parameter:artifact-0.1
```

Running the Experiments
---------------------
After creating the docker container, run an exmaple test case with the following commands:
```
$ cd /root;
$ git clone https://github.com/StarThinking/ZebraConf
$ cd ZebraConf/runner
$ ./build.sh
$ ./run_heter_conf_test.sh hdfs org.apache.hadoop.hdfs.security.token.block.TestBlockToken#testBlockTokenInLastLocatedBlockLegacy dfs.encrypt.data.transfer@@@hdfs:DataNode@@@1@@@true@@@false
```

Paper Citation
---------------------
