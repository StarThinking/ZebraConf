#!/bin/bash

if [ $# -ne 2 ]; then echo "[proj] [version]"; exit -1; fi
proj=$1
version=$2
if [ $version -eq 3 ]; then
    proj_root_dir=$(cat /root/reconf_test_gen/$proj/project_root_dir.txt)
else
    proj_root_dir=$(cat /root/reconf_test_gen/$proj/project_root_dir_2.txt)
fi

tmp_file='jar.class.tmp'
	
IFS=$'\n'
function jar_contains_any_comp {
    jar_path=$1
    if [ -f $tmp_file ]; then rm $tmp_file; fi
    jar tf $jar_path > $tmp_file
    for comp in $(cat /root/reconf_test_gen/$proj/all_components.txt)
    do
        if [ "$(grep $comp $tmp_file)" != "" ]; then
    	    echo "$jar_path"
    	    return
        fi
    done    
}

jar_contains_comp_array=$(for j_path in $(find $proj_root_dir -name '*.jar')
do
    jar_contains_any_comp $j_path
done)

# just keep one jar_path per jar_name
declare -A jar_map

for j_path in ${jar_contains_comp_array[@]}
do
    j_name=$(echo $j_path | awk -F '/' '{print $NF}')
    if [ "${jar_map["$j_name"]}" == "" ]; then
        jar_map["$j_name"]="$j_path"
        echo "$j_name ${jar_map["$j_name"]}"
    fi
done

rm $tmp_file
