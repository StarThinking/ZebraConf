#!/bin/bash

i=0
#THRESHOLD=5

addr_array+=('130.127.134.5')
addr_array+=('128.105.145.156')

#for addr in ${addr_array[@]}
#do
#    ssh $addr 'ls ~'
#done
#exit 0

while true
do

echo "start update for $i round"
i=$(( i + 1 ))

for addr in ${addr_array[@]}
do
    ssh $addr '~/parameter_test_controller/pm_fetch_analyze_hypo.sh' 
done

sleep 2

rm ~/extra_white_list.txt
for addr in ${addr_array[@]}
do
    ssh $addr 'cat ~/my_white_list.txt' >> ~/extra_white_list.txt
done

cat ~/extra_white_list.txt | sort | uniq -c | awk '{if($1 >= 5) print $0}' | awk '{print $2}' > ~/extra_white_list_thres.txt

cat ~/parameter_test_controller/white_list.txt ~/extra_white_list_thres.txt > ~/white_list_tmp.txt

cat ~/white_list_tmp.txt | sort -u  > ~/parameter_test_controller/white_list.txt

cd ~/parameter_test_controller
git add white_list.txt
git commit -m 'update wl'
git push origin master


for addr in ${addr_array[@]}
do
    ssh $addr '~/parameter_test_controller/container_utility_sh/whole_cluster_update_white_list.sh'
done

echo 'sleep for 600s'
sleep 600

done
