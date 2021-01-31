#!/bin/bash

IFS=$'\n'

if [ $# -ne 2 ]; then exit -1; fi

xml_file=$1
proj=$2

para_value_array=$(java -cp .:/root/recon_test_gen ReadXMLFile $xml_file getParameterValue)

function get_int_parameter_internal {
    for entry in ${para_value_array[@]}
    do
        para=$(echo "$entry" | awk -F ' ' '{print $1}')
        default_v=$(echo "$entry" | awk -F ' ' '{print $2}')
        if [[ $default_v =~ ^-?[0-9]+$ ]]; then
            #echo "$para $default_v"
            echo "$para"
        fi
    done

    getIntFile=/root/reconf_test_gen/soot_study/component_parameter_analysis/$proj/get/getInt.txt
    getLongFile=/root/reconf_test_gen/soot_study/component_parameter_analysis/$proj/get/getLong.txt
    cat $getIntFile $getLongFile
}

function get_int_parameter {
    get_int_parameter_internal | sort -u
}

get_int_parameter
