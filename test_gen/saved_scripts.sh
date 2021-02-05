#!/bin/bash

# generate testing tuples
pids=(); for p in $(cat final-x1.5/parameter_types/getBoolean_xml.txt | ./undesired_para_filter.sh); do ./generate_tuples.sh $p > final-x1.5/testing_tuples/getBoolaen/"$p".txt & pids+=($!); done; for id in ${pids[@]}; do wait $id; echo "$id done"; done

## filter 'unidentifiable' and 'unit_test'
cat per_para_tuples_all/* | grep -v 'unidentifiable' | grep -v 'unit_test'

# sort by proj test
 cat tuples_per_para.txt | awk '{print $2" "$3}' | sort -u | while read line; do grep -F " $line " tuples_per_para.txt | awk '{print $2" "$3" "$1" "$4" "$5" "$6" "$7}' > tuples_per_test/"$line".txt ; done
#find . -size  0 -print -delete

# grouping
mkdir ../grouped; IFS=$'\n'; for i in *; do echo "grouping for test $i"; java -cp ~/vm_images/ZebraConf/test_gen GroupTuple "$i" 100 > ../grouped/"$i";  done

# get*.txt
find . -name parameter | while read line; do cat $line/*; done | awk '{print $NF" "$1}' | sort -u | awk '{print $1}' | sort |uniq -c

find . -name parameter | while read line; do cat $line/*; done | grep ' getInt'$ | awk '{print $1}' | sort -u > getInt.txt
comm -12 getInt.txt ~/reconf_test_gen/all_xml_parameters.txt > getInt_xml.txt

# get all get-parameter table
for dir in $(find . -name parameter); do for i in $dir/*; do cat $i | awk '{print $5" "$3}'; done; done | sort -u > all_get_parameter.txt

# get 5-xml get-parameter
IFS=$'\n'; for line in $(cat all_get_parameter.txt); do para=$(echo $line | awk '{print $2}'); if [ "$(grep ^"$para"$ all_xml_parameters.txt)" != "" ]; then echo "$line"; fi; done 

# test num for each parameter
for i in *; do echo "$i $(cat $i | wc -l)"; done | sort -n -k2 -r
# test num for each component
cat * | awk '{print $4}' | sort  | uniq -c | sort -n -k1 -r

# sharing statistics
find . -name 'component' | while read dir; do cd $dir; echo "$dir"; num_of_conftests=$(grep -rn registerMy * | awk -F '-component-meta.txt' '{print $1}' | sort -u | wc -l); echo "num_of_conftests=$num_of_conftests"; sharing=$(ls | while read i; do if [ "$(grep 'record sharing, original external conf is read after being used for component init\|record sharing, original external conf is shared by multiple components' $i)" != "" ]; then echo $i; fi; done | wc -l); echo "sharing=$sharing"; echo "component_component_sharing % = $(echo "scale=3; $sharing * 100 / $num_of_conftests" | bc)"; cd - > /dev/null; done

grep -v -e '.address' -e '.bind-host' -e '.principal' -e '.parent-path' -e '.class' -e '.path' -e '.hostname' -e '.hosts' -e '-dir'$ -e '.port' -e '.dir' -e '.bindAddress' -e '.id' -e '.impl' -e '.file' -e '.keytab' -e '.uri' -e '.url' left.txt > left_select.txt

# shrink value space
cat get*.txt | awk '{if ( NF <= 4) print $0}' >> getInt.txt; cat get*.txt | awk '{if ( NF >= 5) print $0}' | while read LINE; do echo -e "$(echo $LINE | awk '{print $1" "$2}') $(echo $LINE | awk '{for (i=3; i<=NF; i++) print $i}' | tr ' ' '\n' | sort -n | paste -s -d" " | awk '{print $2" "$3}')"; done >> getInt.txt


