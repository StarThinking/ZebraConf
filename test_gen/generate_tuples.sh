#!/bin/bash
#
# we add suffix 'unidentifiable' to a tuple it is not identifiable
#

function get_combo {
    local array=( $(echo "$@" | awk -F ' ' '{for(i=1; i<=NF; i++) print $i}') )
    local array_num=${#array[@]}
    for i in $(seq 1 $(( array_num - 1 )))
    do
        if [ "${array[0]}" != "${array[$i]}" ]; then
            echo "${array[0]} ${array[$i]}"
            echo "${array[$i]} ${array[0]}"
        fi
    done | sort -u
}

IFS=$'\n'
if [ $# -ne 1 ]; then echo 'wrong: [parameter]'; exit -1; fi

parameter=$1

max_line=1 # default, the first line
para_value_list_dir='/users/masix/vm_images/ZebraConf/app_meta/cassandra/para_value_list'
function find_max_value_line {
    #para_value_list_dir='/root/data_store_sdb/hconf_result_fse/para_value_list'
    local pv_line_num=$(grep -r ^"$parameter " $para_value_list_dir | wc -l)
    local current_line=0
    local max_v_num=0
    if [ $pv_line_num -ne 1 ]; then
        # resolve duplicates by using line with more values
        if [ $pv_line_num -ge 2 ]; then 
    	    for line in $(grep -r ^"$parameter " $para_value_list_dir)
    	    do
    	        #1>&2 echo "line $line"
                current_line=$(( current_line + 1 ))
    	        v_num=$(echo $line | awk '{print NF}')
    	        if [ $v_num -gt $max_v_num ]; then max_v_num=$v_num; max_line=$current_line; fi
    	    done
    	    1>&2 echo "WARN: multiple pv lines for $parameter"
   	    #, let's use line $max_line with #value $max_v_num"
    	    #echo "WARN: multiple pv lines for $parameter, let's use line $max_line with #value $max_v_num"
        else
    	    1>&2 echo "ERROR: check $parameter value list!"
            exit -1
        fi
    fi
}

# manual-choose value list for this parameter
find_max_value_line
manual_select_v_list=( $(grep -r ^"$parameter " $para_value_list_dir | head -n $max_line | tail -n 1 | awk -F ':' '{print $2}' | awk '{for(i=2;i<=NF;i++) print $i}') )
v_list=()
v_list[0]='ut_runtime_v'
v_index=1
for v in ${manual_select_v_list[@]}
do
    v_list[$v_index]="$v"
    v_index=$(( v_index + 1 ))
done
1>&2 echo "--->generating testing tuples for $parameter with ${#v_list[@]} values: ${v_list[@]}"

# for check
#exit 0

final_root_dir='/users/masix/vm_images/ZebraConf/app_meta/cassandra/prerun'
unable_id_suffix="unidentifiable"
unable_id=0

#for p in hdfs hbase yarn mapreduce hadoop-tools
for p in cassandra
do
    logs=$(grep -r ^"$parameter " $final_root_dir/$p/ultimate | awk -F '-ultimate-meta.txt' '{print $1"-ultimate-meta.txt"}' | sort -u)

    for log in ${logs[@]}
    do
	#echo "log=$log"
        # perform identify filter when identify dir exists
        if [ -d $final_root_dir/$p/identify ]; then
	    # filter this test if its idnetify-cannot.txt contains this parameter
 	    cannot_identify=$(echo $log | awk -F '/ultimate/' '{print $2}' | awk -F '-ultimate-meta.txt' '{print $1"-identify-cannot.txt"}')
	    cannot_identify_log=$(echo "$final_root_dir/$p/identify/""$cannot_identify")
	    #unable_id=0
	    if [ ! -f $cannot_identify_log ]; then echo 'ERROR: can not find cannot_identify_log $cannot_identify_log'; exit 1; fi
	    if [ "$(grep ^"$parameter"$ $cannot_identify_log)" != "" ]; then 
	        #echo "$parameter is not identifiable in test $log"
	        #continue; 
	        unable_id=1
	    fi
        fi
        
    	the_proj="$p"
        the_test="$(echo $log | awk -F '/ultimate/' '{print $2}' | awk -F '-ultimate-meta.txt' '{print $1}')"
        component_inits=( $(cat $log | grep ^"$parameter " | awk '{print $2}' | sort -u | awk -F '.' '{print $1}' | uniq -c | awk '{print $2" "$1}') )
	#echo ${component_inits[@]}	
    	# add the default value used for this component at this point and create value pairs	
	# WARN!!! It might be a problem that we didn't filter out null value in configuration get printing.
        #echo ""
        #cat $log | grep ^"$parameter " | awk '{print $3}' | sort -u
        #echo ""
        
	#value_used=( $(cat $log | grep ^"$parameter " | awk '{print $3}' | sort -u | grep -v null | head -n 1) )       
	value_used=( $(cat $log | grep ^"$parameter " | awk '{print $3}' | sort -u | head -n 1) )       
	
	# let the index-1 value be the default value, if the used value is invalid
	if [[ "$value_used" == *'Ljava.lang.String'* ]]; then 
	    v_list[0]="${v_list[1]}"
	else
 	    v_list[0]="$value_used"
	fi
    	v_pairs=( $(get_combo ${v_list[@]}) )
	
	for component_init in ${component_inits[@]}
	do
	    the_component=$(echo $component_init | awk '{print $1}')
	    the_inits=$(echo $component_init | awk '{print $2}')
    	    for v_p in ${v_pairs[@]}
	    do
	 	if [ $the_inits -eq 1 ]; then
		    if [ $unable_id -eq 0 ]; then
		        echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" ""$the_inits"" ""$v_p"
		    else
			echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" ""$the_inits"" ""$v_p"" ""$unable_id_suffix"
		    fi
	 	else
		    if [ $unable_id -eq 0 ]; then
	                echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" -1 ""$v_p"
	                echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" -2 ""$v_p"
	                echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" -3 ""$v_p"
		    else
	                echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" -1 ""$v_p"" ""$unable_id_suffix"
	                echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" -2 ""$v_p"" ""$unable_id_suffix"
	                echo "$parameter"" ""$the_proj"" ""$the_test"" ""$the_component"" -3 ""$v_p"" ""$unable_id_suffix"
		    fi
		fi
	    done
	done
    done
done
