rm *txt; for i in *; do tar zxvf $i; rm $i; done; mkdir no_need_hypo/; cf=0.9999; for hlog in *_hypothesis_*; do ../sbin/hypo_analysis.sh $hlog $cf 1; done | while read line; do mv $line no_need_hypo/; done; cd no_need_hypo; for i in *; do p_and_c="$(~/vm_images/ZebraConf/runner/sbin/extract_utility.sh $i 'para')@@@$(~/vm_images/ZebraConf/runner/sbin/extract_utility.sh $i 'comp')"; if [ ! -d $p_and_c ]; then mkdir $p_and_c; fi; mv $i $p_and_c; done

# start hypo dispatcher
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do ssh node-$i "rm ~/nohup.txt; ps aux | grep dispatcher | awk '{print $2}' | xargs kill -9; nohup ~/parameter_test_controller/dispatcher_hypo.sh > nohup.txt &" & pids[$i]=$!; done; for p in ${pids[@]}; do wait $p; echo "$p is done"; done

# collect hypothesis .txt
### must in target dir
ls | xargs rm -rf; pids=(); for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do ssh node-$i "find ~/parameter_test_controller/target/ -type f -maxdepth 1 -name '*' | xargs rm; ~/parameter_test_controller/container_utility_sh/docker_fetch_result.sh _hypothesis_ /root/parameter_test_controller/target/ /root/parameter_test_controller/target/; cd /root/parameter_test_controller/; rm -rf target.$i; cp -r target target.$i; tar zcvf $i.tar.gz target.$i" & pids+=($!); done; for id in ${pids[@]}; do wait $id; echo "pid $id finished"; done; for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do scp node-$i:~/parameter_test_controller/$i.tar.gz ~/parameter_test_controller/target/; done; find -maxdepth 1 -name '*txt*' | xargs rm ; find -maxdepth 1 -name '*.class' | xargs rm; ls;

#
for i in *.tar.gz; do tar zxvf $i; rm $i; mv target.* $(($(date +%s%N)/1000000)); done
#
mkdir single_hypothesis; find 16* -name '*single_hypothesis_*' | xargs mv -t single_hypothesis; cd single_hypothesis; ~/parameter_test_controller/just_compile.sh; mkdir no_need_hypo/; cf=0.9999; for hlog in *_hypothesis_*; do ~/parameter_test_controller/hypo_analysis.sh $hlog $cf 1; done | while read line; do mv $line no_need_hypo/; done

#
cd  ??
pids=(); for i in 16*; do mkdir single_run_$i; find $i -name '*single_run_*' | xargs mv -t single_run_$i & pids+=($!); done; for p in ${pids[@]}; do wait $p; echo "$p is finished"; done

pids=(); for d in single_run_16*; do ~/parameter_test_controller/find_invalid_log.sh $d > invalid.$d & pids+=($!); done; for p in ${pids[@]}; do wait $p; echo "$p is finished"; done

# create invalid store
cat invalid.single_run_* | sort -u > invalid.txt
cat invalid.txt | awk '{print $2}' | sort -u > all_tests.txt
mkdir invalid_store
for i in $(cat all_tests.txt); do grep $i invalid.txt > invalid_store/$i; done

# remember to update incremental invalid store
cat invalid.txt ../round_?_analysis/invalid.txt | sort -u > invalid.txt.tmp
mv invalid.txt.tmp invalid.txt
cat invalid.txt | awk '{print $2}' | sort -u > all_tests.txt
mv invalid_store invalid_store.old
mkdir invalid_store
for i in $(cat all_tests.txt); do grep $i invalid.txt > invalid_store/$i; done
rm -rf invalid_store.old

# last step
pids=(); for i in x*; do ../filter.sh $i > filter.$i & pids+=($!); done; for p in ${pids[@]}; do wait $p; echo "$p is finished"; done
#remember to filter empty line
sed -r '/^\s*$/d'

# check finish ratio
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do finished=$(ssh node-$i "cat ~/nohup.txt | grep assign | wc -l"); all=$(ssh node-$i "cat nohup.txt | head -n 2 | tail -n 1" | awk -F ' = ' '{print $2}'); ratio=$(echo "scale=2; $finished / $all" | bc); echo "$finished out of $all are finished $ratio"; done

# list white list candidates
for i in *_hypothesis_*; do cat $i | head -n 3 | tail -n 1; done | sort | awk -F ' |@@@' '{print $2" "$3}'

cat tmp.txt | sort | uniq -c | awk '{if($1 >= 5) print $0}'

# check if hypo unfinished
for i in *_hypothesis_*; do if [ "$(grep 'Total execution time' $i)" == "" ]; then echo $i; fi; done

for i in $(for i in *hypothesis*; do if [ "$(grep 'Total execution time' $i)" == "" ]; then echo $i; fi; done); do echo $i; grep 'v1v2 test failed' $i | wc -l; grep 'Test vvMode=v1v2' $i | wc -l; grep 'v1v1 or v2v2 test failed' $i | wc -l; grep 'Test vvMode=v2v2\|Test vvMode=v1v1' $i | wc -l; done

# collect unfininshed tasks
for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do finished=$(ssh node-$i "cat ~/nohup.txt | grep assign | wc -l"); all=$(ssh node-$i "cat nohup.txt | head -n 2 | tail -n 1" | awk -F ' = ' '{print $2}'); ssh node-$i "cat ~/parameter_test_controller/task.txt | tail -n $(( all - finished ))"; done > left.1.txt
