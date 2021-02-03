# get pre-pre run all raw tests (including parameterized tests)
#echo > ~/tmp.txtt; grep 'msx-listener test started ' * | awk -F 'msx-listener test started ' '{print $2}' | grep -v ':' >> ~/tmp.txtt; grep 'msx-listener test started ' * | awk -F 'msx-listener test started ' '{print $2}' | grep ':' | awk -F ':' '{print $1":*]"}' >> ~/tmp.txtt; cat ~/tmp.txtt | sort -u > ../all_tests.txt 

rm tmp.txt; cat 2.txt all_tests.txt | sort -u | grep '\[' | awk -F '[' '{print $1"[*]"}' | sort -u >> tmp.txt; cat 2.txt all_tests.txt | sort -u | grep -v '\[' >> tmp.txt; cat tmp.txt | sort -u > ALL_TESTS.txt

# get tests are at least succeed once in three rounds
grep -rn 'msx-rc 0' CORRECT_TEST_* | awk -F '/' '{print $2}' | grep 'msx-rc 0' | awk -F '-component-meta.txt' '{print $1}' | sort -u > CORRECT_TESTS.txt
## show all and succeed tests
for i in hdfs yarn mapreduce hadoop-tools hbase; do echo $i; cat $i/about_test/ALL_TESTS.txt | wc -l; cat $i/about_test/CORRECT_TESTS.txt | wc -l; echo ''; done

# test 2 sub project path mapping
find CORRECT_* -name '*-component-meta.txt' | while read log; do echo "$(echo $log | awk -F '#' '{print $1}' | awk -F '/' '{print $2}') $(cat $log | tail -n 2 | head -n 1 | awk -F 'msx-output-log ' '{print $2}' | awk -F '/target/' '{print $1}')"; done | sort -u > mapping.txt 

# find all the sub projects pom.xml path
find /root/flink-release-1.12.1 -name pom.xml | sed -e "s/pom.xml$//g" | sort | sed '1d' | grep -v '/target/' | grep -v '/src/' | while read sub_project; do cd $sub_project; echo "--------------------------$sub_project---------------------------"; mvn test; echo ''; echo ''; done

# test running time
docker container list -a | awk '{print $NF}' | grep -v NAMES | while read i; do docker container stop $i; docker container rm $i; done
for i in $(seq 0 19); do docker exec hadoop-$i bash -c 'cd /root/reconf_test_gen/; for i in target/*-mvnlog.txt; do ~/reconf_test_gen/filter_time.sh $i; done > yarn.txt'; done
for i in $(seq 0 9); do docker exec hadoop-$i bash -c 'cd /root/reconf_test_gen/; ./display_run_time.sh yarn run'; done

# structure final
rm *txt*; for i in $(grep -oP "node-[0-9]{1,2}$" /etc/hosts | sed 's/node-//g' | sort -n); do tar zxvf $i.tar.gz ; done; rm *.tar.gz; mkdir component; mkdir parameter; mkdir ultimate; mv *-component-meta.txt component; mv *-parameter-meta.txt parameter; mv *-ultimate-meta.txt ultimate;

# sanity check
grep -rn ERROR * | grep 'sanity check failed' | awk -F '-component-meta.txt' '{print $1}' | sort -u
grep -rn 'msx-rc 0' | wc -l; grep -rn 'msx-rc 1' | wc -l; 

# show components
grep registerMyCom * | awk -F 'msx-confcontroller| ' '{print $6}' | awk -F '.' '{print $1}' | sort -u | while read i; do count=$(grep -rn $i * | awk -F '-component-meta.txt' '{print $1}' | sort -u | wc -l); echo "$i $count"; done

# identified result
cd final/component/;
#grep registerMyComponent * | awk -F '-component-meta.txt' '{print $1"-component-meta.txt"}' | sort -u | while read line; do echo $line; ~/reconf_test_gen/identify.sh $line 1; echo ""; done > result.txt; mkdir ../identify; mv *-identify-*.txt ../identify; cd ../identify; cat *-identify-can.txt | sort -u > all_can.txt; cat *-identify-cannot.txt | sort -u > all_cannot.txt; comm -13 all_can.txt all_cannot.txt > unique_cannot.txt
mkdir ../identify;  ls | while read line; do echo $line; ~/reconf_test_gen/identify.sh $line 1; echo ""; done > ../identify/result.txt; mv *-identify-*.txt ../identify; 
#cd ../identify; cat *-identify-can.txt | sort -u > all_can.txt; cat *-identify-cannot.txt | sort -u > all_cannot.txt; comm -13 all_can.txt all_cannot.txt > unique_cannot.txt

# under final/identity
cat result.txt | grep '% can' | awk '{print $NF}' | sort -n > distri.txt

echo "avg:"; awk '{ total += $1; count++ } END { print total/count }' distri.txt; echo "50p:"; head -n $(echo "$(cat distri.txt | wc -l) / 2" | bc) distri.txt | tail -n 1;  echo "90p:"; head -n $(echo "scale=0; $(cat distri.txt | wc -l) / 100 * 10" | bc) distri.txt | tail -n 1;  echo "95p:"; head -n $(echo "scale=0; $(cat distri.txt | wc -l) / 100 * 5" | bc) distri.txt | tail -n 1;

echo "avg:"; awk '{ total += $1; count++ } END { print total/count }' distri.txt; echo "50p:"; head -n $(echo "$(cat distri.txt | wc -l) / 2" | bc) distri.txt | tail -n 1

# get hbase main+conf components
grep -rn 'static void main(' | awk -F ':' '{print $1}' | grep .java | grep -v '/test/' | while read line; do if [ "$(grep 'HBaseConfiguration.create' $line)" != "" ]; then echo $line; fi; done

# component init point statistics
grep ' init,' * | awk '{print $2}' | sort | uniq -c | sort -n -r -k1 | awk '{print $1" "$2}'
