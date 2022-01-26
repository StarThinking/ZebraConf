# check component id match
for i in *; do echo $i; ~/vm_images/ZebraConf/app_meta/cassandra/trails/profiling/convert.sh $i | awk '{print $2" "$3}' | sort -u; echo ''; done > ../pid_component_id_match.txt

# do convert to generate prerun data
for i in *; do mypath="$(echo $i | awk -F '-output' '{print $1}')-ultimate-meta.txt"; ../../convert.sh $i | awk '{print $1" "$2" "$3}' | sort -u | sed -r '/^\s*$/d'  >  ../cassandra/ultimate/$mypath; done

pids=(); for p in $(cat ../app_meta/cassandra/parameter/boolean.txt ); do ./generate_tuples.sh $p > ~/testing_tuples/boolean/"$p".txt & pids+=($!); done; for id in ${pids[@]}; do wait $id; echo "$id done"; done
