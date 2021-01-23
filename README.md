# ZebraConf
This repository contains scripts and other supplementary material
for the EuroSys'21 artifact evaluation of the paper **Finding Unsafe Heterogeneous Configurations in Cloud Systems** 
by Sixiang Ma, Fang Zhou, Michael D. Bond, and Yang Wang.

The scripts can be used to reproduce the results in the paper.

## Authors
 * Sixiang Ma (The Ohio State University)
 * Fang Zhou (The Ohio State University)
 * Michael D. Bond (The Ohio State University)
 * Yang Wang (The Ohio State University)

## Directory Structure
 * `app_meta` contains the metadata information about the four applications (i.e., HDFS, YARN, MR, HBASE) we applied. The information will be used to set up testing environment.
 * `agent` contains the source code of ConfAgent module and a utility class to fetch unit tests' error report to ease debug. 
 * `runner` contains the source code of TestRunner, the library, the shared files used to communicate with ConfAgent,  the script to run heterogeneous tests, and scripts for cluster testing.
 * `test_gen` contains the scripts to generate testing cases.

## Software Dependencies
* Dependencies required to compile and run the target application.
* Docker, if users want to run tests on our testing environment.

## Setting up Testing Environment
To let users instantly try ZebraConf, we have provided a Docker image (11.17 GB) that encapsulates our testing environment. With this, users can run heterogeneous configuration tests with HDFS, YARN, MapReduce, HBASE. 

- Create a docker container with specified repo and tag:
```
$ docker run -d -it --name [YOUR_CONTAINER_NAME] sixiangma/reconf_parameter:artifact-0.1
```

- Log into the docker container you just created:
```
$ docker exec -it [YOUR_CONTAINER_NAME] bash
```

## Running Heterogeneous Configuration Tests
After logging into the container, users can run heterogeneous configuration tests with *run_heter_conf_test.sh* script under *runner* directory. 

- Dowonload repo and build the runner:
```
$ cd /root
$ git clone https://github.com/StarThinking/ZebraConf
$ cd ZebraConf/runner
$ ./build.sh
```

- Run a (single-paramater) heterogeneous configuration test.<br><br>The script *run_heter_conf_test.sh* takes three arguments. The first two specify the unit test suite and function. The third argument indicates the heterogeneous configuration assignment in the format of `para@@@component@@@point@@@v1@@@v2`. For example, `dfs.bytes-per-checksum@@@hdfs:DataNode@@@1@@@32@@@512` means setting *dfs.bytes-per-checksum* as 512 for the first HDFS DataNode and *dfs.bytes-per-checksum* as 32 to all the other nodes.
```
$ ./run_heter_conf_test.sh [suite] [u_test] [[para@@@component@@@point@@@v1@@@v2]%%%[...]]
$
$ ./run_heter_conf_test.sh hdfs org.apache.hadoop.hdfs.web.TestWebHdfsWithMultipleNameNodes#testRedirect \
dfs.bytes-per-checksum@@@hdfs:DataNode@@@1@@@32@@@512
```

Paper Citation
---------------------
