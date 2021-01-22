# run reconf_test dispatcher distributedly
proj='hdfs'; for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do ssh node-$i "rm ~/nohup.txt; ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9; nohup ~/reconf_test_gen/dispatcher.sh $proj > nohup.txt &" & pids[$i]=$!; done; for p in ${pids[@]}; do wait $p; echo "$p is done"; done

# for classes
./docker_fetch_result.sh; for i in org*.txt; do grep msx $i | grep -v msx-conf > $(echo $i | awk -F '-output.txt' '{print $1}'); done; rm *-output.txt; ls | grep org | wc -l; cat task.txt | wc -l

# for tests
./docker_fetch_result.sh; for i in org*.txt; do ./compress.sh $i; done | wc -l; rm *-output.txt; ls | grep component-meta.txt | wc -l; cat task.txt | wc -l

java ReadXMLFile hbase/hbase-default.xml | awk -F ' ' '{if($2 == "true" || $2 == "false") print $1}' | sort -u > boolean_xml.txt

# filter no_type.txt
grep -v .host$ | grep -v .url$ | grep -v .address$ | grep -v .classpath$ | grep -v .classes$ | grep -v .class$ | grep -v .path$ | grep -v .file$ | grep -v .root-dir$ | grep -v .provider$ | grep -v .principal$ | grep -v .hostname$ | grep -v .id$

for i in *; do if [ "$(grep 'msx-listener succeed' $i)" == "" ] && [ "$(grep 'msx-listener failed' $i)" == "" ]; then echo $i; fi; done

# find server classes for a componenet
cd OUTER_DIR_FOR_COMPONENT
find COMPONENT_SERVER_CLASS_PATH_PREFIX -name '*.java' | sed 's#/#.#g' | sed 's/^..//g' | sed 's/.java$//g'

# make up list add statement
cat server_classes.txt | sed 's/^/classList.add("/g' | sed 's/$/");/g'
