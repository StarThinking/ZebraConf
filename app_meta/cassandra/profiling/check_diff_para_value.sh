#!/bin/bash

log=$1
IFS=$'\n'
rm ~/values.txt &> /dev/null
para_component_instance_keys=( $(~/vm_images/ZebraConf/app_meta/cassandra/trails/profiling/convert.sh $log | sort -k 1,2 | sort -u | awk '{print $1" "$2}' | sort -u) )
~/vm_images/ZebraConf/app_meta/cassandra/trails/profiling/convert.sh $log | sort -k 1,2 | sort -u > ~/values.txt

for key in ${para_component_instance_keys[@]}
do
    #if [ "$key" != "file_cache_size_in_mb Daemon.1" ]; then continue; fi
    
    values=( $(grep ^"$key " ~/values.txt) )
    if [ ${#values[@]} -gt 1 ]; then
        echo -n "$key"
        for value in ${values[@]}
        do 
            echo -n " $(echo $value | awk '{print $NF}')"
        done
        echo ""
    fi
done

#for key in $(cat 1.txt | grep 'file_cache_size_in_mb' | grep Daemon.1); do values=( $(grep $key 2.txt)); for i in ${values}; do echo $i; done | grep -v 'null'$; done
