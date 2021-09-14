# ZebraConf
This repository contains scripts and other supplementary material
for the EuroSys'21 artifact evaluation of the paper **Finding Unsafe Heterogeneous Configurations in Cloud Systems** (http://web.cse.ohio-state.edu/~ma.1189/papers/eurosys21-ma.pdf)
by Sixiang Ma, Fang Zhou, Michael D. Bond, and Yang Wang.

The scripts can be used to reproduce the results in the paper.

## Authors
 * Sixiang Ma (The Ohio State University)
 * Fang Zhou (The Ohio State University)
 * Michael D. Bond (The Ohio State University)
 * Yang Wang (The Ohio State University)

## Directory Structure
 * `app_meta` contains the metadata information about the four applications (i.e., HDFS, YARN, MR, HBASE, FLINK) we applied. The information will be used to set up testing environment.
 * `agent` contains the source code of ConfAgent module and a utility class to fetch unit tests' error report to ease debug. 
 * `runner` contains the source code of TestRunner, the library, the shared files used to communicate with ConfAgent,  the script to run heterogeneous tests, and scripts for cluster testing.
 * `test_gen` contains the scripts to generate testing cases.

## Software Dependencies
* Dependencies required to compile and run the target application.
* Docker, if users want to run tests on our testing environment.

## Setting up Testing Environment
To let users instantly try ZebraConf, we have provided a Docker image (18 GB) that encapsulates our testing environment. With this, users can run heterogeneous configuration tests with HDFS, YARN, MapReduce, HBASE. 

- Create a docker container with specified repo and tag:
```
$ docker run -d -it --name [YOUR_CONTAINER_NAME] sixiangma/reconf_parameter:artifact-1.5.7
```

- Log into the docker container you just created:
```
$ docker exec -it [YOUR_CONTAINER_NAME] bash
```

## Running Heterogeneous Configuration Tests
After logging into the container, users can run heterogeneous configuration tests with *run_heter_conf_test.sh* script under *runner* directory. 

- Dowonload repo (skip this if you're running with docker image) 
```
$ cd /root
$ git clone https://github.com/StarThinking/ZebraConf
```

- Update repo and build the runner:
```
$ cd /root/ZebraConf
$ git pull
$ cd runner
$ ./build.sh
```

- Run a (single-paramater) heterogeneous configuration test.<br><br>The script *run_heter_conf_test.sh* takes three arguments. The first two specify the unit test suite and function. The third argument indicates the heterogeneous configuration assignment in the format of `para@@@component@@@point@@@v1@@@v2`. For example, `dfs.bytes-per-checksum@@@hdfs:DataNode@@@1@@@32@@@512` means setting *dfs.bytes-per-checksum* as 512 for the first HDFS DataNode and *dfs.bytes-per-checksum* as 32 to all the other nodes.
```
$ ./run_heter_conf_test.sh
./run_heter_conf_test.sh [suite] [u_test] [[para@@@component@@@point@@@v1@@@v2]%%%[...]]

$ ./run_heter_conf_test.sh hdfs org.apache.hadoop.hdfs.web.TestWebHdfsWithMultipleNameNodes#testRedirect \
dfs.bytes-per-checksum@@@hdfs:DataNode@@@1@@@32@@@512
```

- The test will finish a few minutes and the test results will be saved into ZebraConf/runner/log directory, as single\_hypothesis and single\_run txt files. Please check the end of single\_hypothesis files to see if Hypothesis Testing Info is recorded.

- Analyze hypothesis testing info. Here, the second argument indicates the confidence used in hypothesis testing analysis.
```
# under runner directory
$ ./sbin/hypo_analysis_wrapper.sh ./log/[replace with the SINGLE_HYPOTHESIS.txt file] 0.999
```

## Generating Testing Tuples
Now, we show how to generate heterogeneous configuration tests tuples by given parameters, and then how to compress them into pooled testing tuples.

- Generate tuples for all boolean type parameters. This procedure will take quite long (finish within a hour).
```
$ cd ZebraConf/test_gen
$ javac GroupTuple.java
$ mkdir boolean_tuples
$ mkdir boolean_tuples/tuples_per_para
$ ./generate_tuples_wrapper.sh parameter_types/getBoolean_xml.txt boolean_tuples/tuples_per_para

# check the number of total tuples, should be ~4.3M)
$ cat boolean_tuples/tuples_per_para/* | wc -l 
```

- Compress into grouped testing tuples. This procedure will take quite long (finish within a hour). 
```
$ cd boolean_tuples
$ ../generate_grouped_tuples.sh

# check the number of total tuples, should be ~94K
$ cat grouped/* | wc -l
```

- Finally, let's see how many tuples will be generated without prerun filtering and grouping. Taking HDFS for example, one can see naively mulitplying parameter, value, test, node dimensions will generate 408,032,256 testing tuples. This number is different (higher) than the data in Table 5 because we collect the complete HDFS unit test suite this time. 
```
$ cd ZebraConf/test_gen
# it takes about 5 minutes
$ ./calculate_ori_tuples.sh
```

## Reproducing Results in the Paper
- Table 5 data can be produced in the last part.

- Reproduce Table 3 (it will take 5 hours):
```
$ /root/ZebraConf/reproduce_result/run_58_reported_cases.sh

```

Paper Citation
---------------------
