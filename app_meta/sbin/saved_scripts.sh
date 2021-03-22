# generate zebra correct class which remove vanilla failed tests
for proj in hdfs yarn mapreduce hadoop-tools hbase flink; do ./sbin/zebra_class_generater.sh "$proj"/about_test/CORRECT_TESTS.txt > "$proj"/about_test/CORRECT_ZEBRA_CLASSES.txt; done
for proj in hdfs yarn mapreduce hadoop-tools hbase flink; do cat "$proj"/about_test/CORRECT_ZEBRA_CLASS_MAPPING.txt | awk -F '#zebraconf_class_test ' '{print $2"#zebraconf_class_test"}' > "$proj"/about_test/CORRECT_ZEBRA_CLASSES.txt; done

# find all the sub projects pom.xml path
find /root/flink-1.11.3 -name pom.xml | sed -e "s/pom.xml$//g" | sort | sed '1d' | grep -v '/target/' | grep -v '/src/' | while read sub_project; do cd $sub_project; echo "--------------------------$sub_project---------------------------"; mvn test; echo ''; echo ''; done

# get all test java/scala class
find . -name 'test' | grep '/src/test' | while read test_dir; do find $test_dir -name '*.java'; find $test_dir -name '*.scala'; done | awk -F 'src/test/' '{print $2}' | sed -e "s#^java/##g" | sed -e "s#^scala/##g" | sed -e "s/.java$//g" | sed -e "s/.scala$//g" | sed 's#/#.#g'  > ~/ZebraConf/app_meta/flink/about_test/JUST_ALL_TESTS.txt

# get pre-pre run all raw tests (including parameterized tests)
./app_meta/sbin/run_cluster_dispacther.sh flink false;
./app_meta/sbin/collect_prepre_run.sh 1;
rm *txt; for i in *; do tar zxvf $i; rm $i; done; find . -name '*-parameter-meta.txt' | xargs rm; find . -name '*-ultimate-meta.txt' | xargs rm;
cat * | grep -r 'msx-listener test started ' * | awk -F 'msx-listener test started ' '{print $2}' | sort -u > ~/tmp.1.txt; rm ~/tmp.2.txt; cat ~/tmp.1.txt | grep '\[' | awk -F '[' '{print $1"[*]"}' | sort -u >> ~/tmp.2.txt; cat ~/tmp.1.txt | grep -v '\[' >> ~/tmp.2.txt; cat ~/tmp.2.txt | sort -u > ALL_TESTS.txt

# get tests are at least succeed once in three rounds
grep -rn 'msx-rc 0' log | awk -F '/' '{print $2}' | grep 'msx-rc 0' | awk -F '-output' '{print $1}' | sort -u  > CORRECT_TESTS.txt
## show all and succeed tests
for i in hdfs yarn mapreduce hadoop-tools hbase; do echo $i; cat $i/about_test/ALL_TESTS.txt | wc -l; cat $i/about_test/CORRECT_TESTS.txt | wc -l; echo ''; done

# structure final
rm *txt*; for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do tar zxvf $i.tar.gz ; done; rm *.tar.gz; mkdir component; mkdir parameter; mkdir ultimate; find . -name '*-component-meta.txt' | xargs mv -t component; find . -name '*-parameter-meta.txt' | xargs mv -t parameter; find . -name '*-ultimate-meta.txt' | xargs mv -t ultimate;
    ### remove empty line
    ls | while read file; do sed -r '/^\s*$/d' $file > "$file".tmp; mv "$file".tmp $file; done

    ### sanity check
    grep -rn ERROR * | grep 'sanity check failed' | awk -F '-component-meta.txt' '{print $1}' | sort -u
    grep -rn 'msx-rc 0' . | wc -l; grep -rn 'msx-rc 1' . | wc -l; 

    ### show components
    grep -rn 'msx-confcontroller registerMyComponent' . | awk -F ' for comoponent ' '{print $2}' | awk -F '.' '{print $1}' | sort | uniq -c

# identified result
cd final/component/;
#grep registerMyComponent * | awk -F '-component-meta.txt' '{print $1"-component-meta.txt"}' | sort -u | while read line; do echo $line; ~/reconf_test_gen/identify.sh $line 1; echo ""; done > result.txt; mkdir ../identify; mv *-identify-*.txt ../identify; cd ../identify; cat *-identify-can.txt | sort -u > all_can.txt; cat *-identify-cannot.txt | sort -u > all_cannot.txt; comm -13 all_can.txt all_cannot.txt > unique_cannot.txt
mkdir ../identify;  ls | while read line; do echo $line; /root/vm_images/ZebraConf/app_meta/sbin/identify.sh $line 1; echo ""; done > ../identify/result.txt; find . -name '*-identify-*.txt' | xargs mv -t ../identify; 
#cd ../identify; cat *-identify-can.txt | sort -u > all_can.txt; cat *-identify-cannot.txt | sort -u > all_cannot.txt; comm -13 all_can.txt all_cannot.txt > unique_cannot.txt

# under final/identity
cat result.txt | grep '% can' | awk '{print $NF}' | sort -n > distri.txt

echo "avg:"; awk '{ total += $1; count++ } END { print total/count }' distri.txt; echo "50p:"; head -n $(echo "$(cat distri.txt | wc -l) / 2" | bc) distri.txt | tail -n 1;  echo "90p:"; head -n $(echo "scale=0; $(cat distri.txt | wc -l) / 100 * 10" | bc) distri.txt | tail -n 1;  echo "95p:"; head -n $(echo "scale=0; $(cat distri.txt | wc -l) / 100 * 5" | bc) distri.txt | tail -n 1;

echo "avg:"; awk '{ total += $1; count++ } END { print total/count }' distri.txt; echo "50p:"; head -n $(echo "$(cat distri.txt | wc -l) / 2" | bc) distri.txt | tail -n 1

# remove random number in file names
ls | while read i; do cp $i ../parameter_rename/"$(echo $i | awk -F '-output_' '{print $1"-parameter-meta.txt"}')"; done

# get hbase main+conf components
grep -rn 'static void main(' | awk -F ':' '{print $1}' | grep .java | grep -v '/test/' | while read line; do if [ "$(grep 'HBaseConfiguration.create' $line)" != "" ]; then echo $line; fi; done

# component init point statistics
grep ' init,' * | awk '{print $2}' | sort | uniq -c | sort -n -r -k1 | awk '{print $1" "$2}'

# test 2 sub project path mapping (not necessary anymore)
#find CORRECT_TEST_* -name '*txt' | while read log; do if [ "$(cat $log | tail -n 1 | grep 'msx-rc')" == "" ]; then continue; fi; echo "$(echo $log | awk -F '#' '{print $1}' | awk -F '/' '{print $2}') $(cat $log | tail -n 2 | head -n 1 | awk -F 'msx-output-log ' '{print $2}' | awk -F '/target/' '{print $1}')"; done | sort -u > mapping.txt

## get mapping from -output.txt
#find /root/flink-1.11.3 -name *-output.txt | while read i; do class=$(echo "$i" | awk -F '/' '{print $NF}' | awk -F '-output.txt' '{print $1}'); path=$(echo "$i" | awk -F '/target/' '{print $1}'); echo "$class $path"; done | sort -u > mapping.txt

# test running time
docker container list -a | awk '{print $NF}' | grep -v NAMES | while read i; do docker container stop $i; docker container rm $i; done
for i in $(seq 0 19); do docker exec hadoop-$i bash -c 'cd /root/reconf_test_gen/; for i in target/*-mvnlog.txt; do ~/reconf_test_gen/filter_time.sh $i; done > yarn.txt'; done
for i in $(seq 0 9); do docker exec hadoop-$i bash -c 'cd /root/reconf_test_gen/; ./display_run_time.sh yarn run'; done
