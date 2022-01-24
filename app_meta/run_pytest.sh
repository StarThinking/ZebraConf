#!/bin/bash
source ~/.profile
echo $@

if [ $# -ne 4 ]; then echo 'ERROR: ./run_pytest.sh [project] [test_name] [verbose_enable] [save_log]'; exit -1; fi

the_project=$1
the_test=$2
verbose_enable=$3
save_log=$4

project_root_dir=$(cat "$ZEBRACONF_HOME"/app_meta/"$the_project"/project_root_dir.txt)
cassadra_src_dir='/users/masix/cassandra'

log_dst_dir="$ZEBRACONF_HOME"'/app_meta/logs'
timeout_value=1200

function force_fill {
    ps aux | grep -ie CassandraDaemon | grep java | awk '{print $2}' | xargs kill -9 &> /dev/null
    jps | grep -v 'Jps' | grep -v 'HConfRunner' | awk '{print $1}' | xargs kill -9 &> /dev/null
}

echo "log_dst_dir = $log_dst_dir"
if [ "$save_log" == "true" ] && [ ! -d $log_dst_dir ]; then
    echo "$log_dst_dir not exisited"
    mkdir $log_dst_dir
fi

echo "the_test is $the_test"
echo "$verbose_enable" > $ZEBRACONF_HOME/app_meta/lib/enable

# delete old log
cassandra_dtest_log='/tmp/my_log.txt'
rm $cassandra_dtest_log
rm /tmp/my_*_id.txt

# run pytest
force_fill
sleep 10
cd $project_root_dir
pytest --timeout=$timeout_value --log-cli-level=WARN --cassandra-dir=$cassadra_src_dir $the_test
rc=$?
echo "[msx] rc = $rc"
force_fill
sleep 10

# if save_log enabled, copy output log to dst directory
if [ "$save_log" == "true" ]; then
    LOG_TIME="$(($(date +%s%N)/1000000))"
    my_random_name="$the_test"-output_"$LOG_TIME"_"$RANDOM$RANDOM"'.txt'
    echo "mv $cassandra_dtest_log $log_dst_dir/$my_random_name"
    mv $cassandra_dtest_log $log_dst_dir/$my_random_name
    ## append rc
    echo "rc $rc" >> $log_dst_dir/$my_random_name
fi

# return exit code of pytest
exit $rc
