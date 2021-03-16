#!/bin/bash
IFS=$'\n'

base_dir='/root/vm_images/ZebraConf/app_meta'

# tests in a porject
hdfs_proj_tests=( $(cat $base_dir/hdfs/about_test/CORRECT_TESTS.txt)) 
hbase_proj_tests=( $(cat $base_dir/hbase/about_test/all_tests.txt)) ## sixiang: for hbase, I used all_tests.txt
yarn_proj_tests=( $(cat $base_dir/yarn/about_test/CORRECT_TESTS.txt)) 
mapreduce_proj_tests=( $(cat $base_dir/mapreduce/about_test/CORRECT_TESTS.txt)) 
hadoop_tools_proj_tests=( $(cat $base_dir/hadoop-tools/about_test/CORRECT_TESTS.txt)) 
flink_proj_tests=( $(cat $base_dir/flink/about_test/CORRECT_TESTS.txt)) 
echo "---tests used in a proj(unit test suite)---"
echo "# of hdfs_proj_tests: ${#hdfs_proj_tests[@]}"
echo "# of hbase_proj_tests: ${#hbase_proj_tests[@]}"
echo "# of yarn_proj_tests: ${#yarn_proj_tests[@]}"
echo "# of mapreduce_proj_tests: ${#mapreduce_proj_tests[@]}"
echo "# of hadoop_tools_proj_tests: ${#hadoop_tools_proj_tests[@]}"
echo "# of flink_proj_tests: ${#flink_proj_tests[@]}"
echo ""

# application specific parameters
hdfs_specific_paras=( $(cat $base_dir/hdfs/all_parameters.txt) )
hbase_specific_paras=( $(cat $base_dir/hbase/all_parameters.txt) )
yarn_specific_paras=( $(cat $base_dir/yarn/all_parameters.txt) )
mapreduce_specific_paras=( $(cat $base_dir/mapreduce/all_parameters.txt) )
flink_specific_paras=( $(cat $base_dir/flink/all_parameters.txt) )
common_specific_paras=( $(cat $base_dir/hadoop-common/all_parameters_xml.txt) )
echo "---application specific parameters---"
echo "# of hdfs_specific_paras: ${#hdfs_specific_paras[@]}"
echo "# of hbase_specific_paras: ${#hbase_specific_paras[@]}"
echo "# of yarn_specific_paras: ${#yarn_specific_paras[@]}"
echo "# of mapreduce_specific_paras: ${#mapreduce_specific_paras[@]}"
echo "# of flink_specific_paras: ${#flink_specific_paras[@]}"
echo ""

# application specific nodes
hdfs_specific_nodes=('NameNode' 'DataNode' 'JournalNode' 'Balancer' 'Mover' 'SecondaryNameNode')
hbase_specific_nodes=('HRegionServer' 'HMaster' 'RESTServer' 'ThriftServer')
yarn_specific_nodes=('ResourceManager' 'NodeManager' 'ApplicationHistoryServer')
mapreduce_specific_nodes=('MapTaskRun' 'ReduceTaskRun' 'JobHistoryServer')
flink_specific_nodes=('TaskManager' 'JobManager')
echo "---application specific nodes---"
echo "# of hdfs_specific_nodes: ${#hdfs_specific_nodes[@]}"
echo "# of hbase_specific_nodes: ${#hbase_specific_nodes[@]}"
echo "# of yarn_specific_nodes: ${#yarn_specific_nodes[@]}"
echo "# of mapreduce_specific_nodes: ${#mapreduce_specific_nodes[@]}"
echo "# of flink_specific_nodes: ${#flink_specific_nodes[@]}"
echo ""

# parameters involved in project
# hdfs = hdfs + common
hdfs_proj_paras=( $(echo ${hdfs_specific_paras[@]} ${common_specific_paras[@]} | tr ' ' '\n' | sort -u) )
# hbase = hdfs + common + hbase
hbase_proj_paras=( $(echo ${hdfs_specific_paras[@]} ${common_specific_paras[@]} ${hbase_specific_paras[@]} | tr ' ' '\n' | sort -u) )
# yarn = hdfs + common + yarn
yarn_proj_paras=( $(echo ${hdfs_specific_paras[@]} ${common_specific_paras[@]} ${yarn_specific_paras[@]} | tr ' ' '\n' | sort -u) )
# mapreduce = hdfs + common + yarn + mapreduce
mapreduce_proj_paras=( $(echo ${hdfs_specific_paras[@]} ${common_specific_paras[@]} ${yarn_specific_paras[@]} ${mapreduce_specific_paras[@]} | tr ' ' '\n' | sort -u) )
# hadoop-tools = mapreduce's
hadoop_tools_proj_paras=( $(echo ${hdfs_specific_paras[@]} ${common_specific_paras[@]} ${yarn_specific_paras[@]} ${mapreduce_specific_paras[@]} | tr ' ' '\n' | sort -u) )
# flink = all
flink_proj_paras=( $(echo ${hdfs_specific_paras[@]} ${common_specific_paras[@]} ${yarn_specific_paras[@]} ${mapreduce_specific_paras[@]} ${hbase_specific_paras[@]} ${flink_specific_paras[@]} | tr ' ' '\n' | sort -u) )

echo "---parameters used in a proj(unit test suite)---"
echo "hdfs_proj_paras = ${#hdfs_proj_paras[@]}"
echo "hbase_proj_paras = ${#hbase_proj_paras[@]}"
echo "yarn_proj_paras = ${#yarn_proj_paras[@]}"
echo "mapreduce_proj_paras = ${#mapreduce_proj_paras[@]}"
echo "hadoop_tools_proj_paras = ${#hadoop_tools_proj_paras[@]}"
echo "flink_proj_paras = ${#flink_proj_paras[@]}"
echo ""

# nodes involved in project
# hdfs = hdfs
hdfs_proj_nodes=( $(echo ${hdfs_specific_nodes[@]} | tr ' ' '\n' | sort -u) )
# hbase = hdfs + hbase
hbase_proj_nodes=( $(echo ${hdfs_specific_nodes[@]} ${hbase_specific_nodes[@]} | tr ' ' '\n' | sort -u) )
# yarn = hdfs + yarn
yarn_proj_nodes=( $(echo ${hdfs_specific_nodes[@]} ${yarn_specific_nodes[@]} | tr ' ' '\n' | sort -u) )
# mapreduce = hdfs + yarn + mapreduce
mapreduce_proj_nodes=( $(echo ${hdfs_specific_nodes[@]} ${yarn_specific_nodes[@]} ${mapreduce_specific_nodes[@]} | tr ' ' '\n' | sort -u) )
# hadoop-tools = mapreduce's
hadoop_tools_proj_nodes=( $(echo ${hdfs_specific_nodes[@]} ${yarn_specific_nodes[@]} ${mapreduce_specific_nodes[@]} | tr ' ' '\n' | sort -u) )
# flink = all
flink_proj_nodes=( $(echo ${hdfs_specific_nodes[@]} ${yarn_specific_nodes[@]} ${mapreduce_specific_nodes[@]} ${hbase_specific_nodes[@]} ${flink_specific_nodes[@]}| tr ' ' '\n' | sort -u) )

echo "---nodes used in a proj(unit test suite)---"
echo "hdfs_proj_nodes = ${#hdfs_proj_nodes[@]}"
echo "hbase_proj_nodes = ${#hbase_proj_nodes[@]}"
echo "yarn_proj_nodes = ${#yarn_proj_nodes[@]}"
echo "mapreduce_proj_nodes = ${#mapreduce_proj_nodes[@]}"
echo "hadoop_tools_proj_nodes = ${#hadoop_tools_proj_nodes[@]}"
echo "flink_proj_nodes = ${#flink_proj_nodes[@]}"
echo ""

# start calculate
v2_assign_combination=3
echo "v2_assign_combination constabt is 3"
para_value_list_dir=/root/vm_images/ZebraConf/test_gen/para_value_list/

for my_project in hdfs hbase yarn mapreduce hadoop_tools flink
do
    echo ">>>>>> calculating testing tuples for $my_project:"
    sum_of_v_pairs_num=0
    para_i_set_values=0
    var="$my_project"_proj_paras[@]
    my_proj_paras=( $(echo ${!var} | tr ' ' '\n') )
    var="$my_project"_proj_nodes[@]
    my_proj_nodes=( $(echo ${!var} | tr ' ' '\n') )
    var="$my_project"_proj_tests[@]
    my_proj_tests=( $(echo ${!var} | tr ' ' '\n') )
    for p in ${my_proj_paras[@]}
    do
        # check whether we set values for this parameter or not
        if [ "$(grep -r ^"$p " $para_value_list_dir)" == "" ]; then
            continue
        else
    	    para_i_set_values=$(( para_i_set_values + 1 ))
        fi 
        v_num=$(grep -r ^"$p " $para_value_list_dir | head -n 1 | awk -F "$p " '{print $2}' | awk '{print NF}')
        v_pairs_num=$(( (v_num - 1 ) * 2 ))
        sum_of_v_pairs_num=$(( sum_of_v_pairs_num + v_pairs_num ))
    done
    echo "# of "$my_project"_proj_nodes is ${#my_proj_nodes[@]}"
    echo "# of "$my_project"_proj_paras is ${#my_proj_paras[@]}"
    echo "para_i_set_values is $para_i_set_values"
    echo "sum_of_v_pairs_num is $sum_of_v_pairs_num"
    echo "# of tuples: $(( sum_of_v_pairs_num * ${#my_proj_tests[@]} * ${#my_proj_nodes[@]} * $v2_assign_combination ))"
    echo ""
done
