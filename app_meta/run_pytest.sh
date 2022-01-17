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

log_dts_dir="$ZEBRACONF_HOME"'/app_meta/logs'
echo "log_dts_dir = $log_dts_dir"
if [ "$save_log" == "true" ] && [ ! -d $log_dts_dir ]; then
    echo "$log_dts_dir not exisited"
    mkdir $log_dts_dir
fi

echo "the_test is $the_test"
echo "$verbose_enable" > $ZEBRACONF_HOME/app_meta/lib/enable

# delete old log
cassandra_dtest_log='/tmp/my_log.txt'
cassandra_dtest_pid_log='/tmp/my_id.txt'
rm $cassandra_dtest_log
rm $cassandra_dtest_pid_log

# run pytest
cd $project_root_dir
pytest --log-cli-level=WARN --cassandra-dir=$cassadra_src_dir $the_test
rc=$?
echo "[msx] rc = $rc"
sleep 2

# if save_log enabled, copy output log to dst directory
if [ "$save_log" == "true" ]; then
    LOG_TIME="$(($(date +%s%N)/1000000))"
    my_random_name="$the_test"-output_"$LOG_TIME"_"$RANDOM$RANDOM"'.txt'
    mv $cassandra_dtest_log $log_dts_dir/$my_random_name
    ## append rc
    echo "rc $rc" >> $log_dts_dir/$my_random_name
fi

# return exit code of pytest
exit $rc
