# HDFS
# test SecondaryNameNode with hdfs unit test
dfs.replication.max SecondaryNameNode 5 9 hdfs org.apache.hadoop.hdfs.server.namenode.TestCheckpoint#testCheckpoint 2

# test NameNode with hadoop-tools unit test
dfs.replication.max NameNode 5 9 hadoop-tools org.apache.hadoop.tools.TestDistCpWithAcls#testAclsNotEnabled 2

# test DataNode with hbase unit test
dfs.replication.max DataNode 5 9 hbase org.apache.hadoop.hbase.regionserver.wal.TestLogRollAbort#testRSAbortWithUnflushedEdits 3

# test DataNode with mapreduce unit test
dfs.replication.max DataNode 5 9 mapreduce org.apache.hadoop.fs.TestFileSystem#testFsCache 1

# test DataNode with yarn unit test
dfs.replication.max DataNode 5 9 yarn org.apache.hadoop.yarn.service.TestYarnNativeServices#testCancelUpgrade 1

# test JournalNode with hdfs unit test
dfs.replication.max JournalNode 5 9 hdfs org.apache.hadoop.hdfs.qjournal.client.TestQuorumJournalManager#testOutOfSyncAtBeginningOfSegment1 2

# Yarn
# test ResourceManager with hadoop-tools unit test
yarn.dispatcher.drain-events.timeout ResourceManager 300000 700000 hadoop-tools org.apache.hadoop.streaming.TestSymLink#testSymLink 1

# test NodeManager with mapreduce unit test
yarn.dispatcher.drain-events.timeout NodeManager 300000 700000 mapreduce org.apache.hadoop.mapred.TestMRTimelineEventHandling#testMapreduceJobTimelineServiceEnabled 2

# test NodeManager with yarn unit test
yarn.dispatcher.drain-events.timeout NodeManager 300000 700000 yarn org.apache.hadoop.yarn.client.api.impl.TestAMRMClient#testAMRMClientWithSaslEncryption[1] 1

# test ApplicationHistoryServer with mapreduce unit test
yarn.dispatcher.drain-events.timeout ApplicationHistoryServer 300000 700000 mapreduce org.apache.hadoop.mapred.TestMRTimelineEventHandling#testMapreduceJobTimelineServiceEnabled 2

# MapReduce
# test JobHistoryServer with hadoop-tools unit test
mapreduce.map.sort.spill.percent JobHistoryServer 0.80 0.90 hadoop-tools org.apache.hadoop.mapred.gridmix.TestSleepJob#testRandomLocation 1

# test JobHistoryServer with mapreduce unit test
mapreduce.map.sort.spill.percent JobHistoryServer 0.80 0.90 mapreduce org.apache.hadoop.mapred.TestMRTimelineEventHandling#testMapreduceJobTimelineServiceEnabled 2

# HBase
# test HMaster with hbase unit test
hbase.client.max.total.tasks HMaster 100 200 hbase org.apache.hadoop.hbase.regionserver.TestRegionReplicas#testFlushAndCompactionsInPrimary 2 

# test HRegionServer with hbase unit test
hbase.client.max.total.tasks HRegionServer 100 200 hbase org.apache.hadoop.hbase.rsgroup.TestRSGroupsAdmin1#testRSGroupListDoesNotContainFailedTableCreation 3
