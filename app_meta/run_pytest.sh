#!/bin/bash
source ~/.profile
echo $@

if [ $# -ne 4 ]; then echo 'ERROR: ./run_pytest.sh [project] [test_name] [verbose_enable] [clone_log]'; exit -1; fi

the_project=$1
project_root_dir=$(cat "$ZEBRACONF_HOME"/app_meta/"$the_project"/project_root_dir.txt)
cassadra_src_dir='/users/masix/cassandra'

the_test=$2
log_dts_dir='/root/ZebraConf/app_meta/log' #???
echo "the_test is $the_test"
verbose_enable=$3
clone_log=$4
echo "$verbose_enable" > $ZEBRACONF_HOME/app_meta/lib/enable

# run pytest
rc=1
cd $project_root_dir
pytest --log-cli-level=WARN --cassandra-dir=$cassadra_src_dir $the_test
echo "[msx] rc = $?"
