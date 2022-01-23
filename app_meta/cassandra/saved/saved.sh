# under all_pytest_files_logs, print the smallest level pytest
for i in *_test.py; do grep ^"$i":: $i; done | grep -v SKIPPED > ../cassandra/all_pytest.txt 

# run tests
for test in $(cat cassandra/all_pytest.txt); do echo $test; time ./run_pytest.sh cassandra $test true true &> pytest_logs/$test; ps aux | grep -ie CassandraDaemon | grep java | awk '{print $2}' | xargs kill; sleep 60; done

# show parameters which don't RETURN CONF.PARAMETER in DatabaseDescriptor.java
for i in $(cat parameters.txt); do ret="$(grep conf."$i" ~/cassandra/src/java/org/apache/cassandra/config/DatabaseDescriptor.java | grep return)"; if [ "$ret" == "" ]; then echo $i; fi; done

# show parameters which don't have a clear get() (p() or getp()) function
comm -23 parameters.txt complex_option.txt | while read i; do convert_key="$(echo $i | awk -F '_' '{for (col=1; col<=NF; col++) printf "%s", $col}')"; grep_res="$(grep --ignore-case "get"$convert_key'()'"\|' '"$convert_key'()'"" ~/cassandra/src/java/org/apache/cassandra/config/DatabaseDescriptor.java | grep static)"; if [ "$grep_res" != "" ]; then echo "get: $i $grep_res"; else echo "no_get: $i"; fi; done | sort  > get_or_no_get.txt

# get all parameters from the web page
cat cass_yaml_file.html | grep 'a class="anchor" href="#' | awk -F 'a class="anchor" href="#' '{print $2}' | awk -F '"' '{print $1}'

# get certain type of parameters
for i in $(cat parameters.txt); do grep " $i \| $i;" ~/cassandra/src/java/org/apache/cassandra/config/Config.java | grep public | grep ' int \| Integer '; done | awk -F ' = ' '{print $1}' | awk '{print $NF}' | awk -F ';' '{print $1}' > int.txt

# check those remaining parameters
comm -23 parameters.txt by_type_all.txt | while read i; do echo $i; grep " $i \| $i;" ~/cassandra/src/java/org/apache/cassandra/config/Config.java; echo ''; done
