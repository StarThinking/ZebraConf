#/bin/bash

while IFS=' ' read -r a1 a2 a3 
do	
	#echo $a1 $a2 $a3
	/root/ZebraConf/runner/run_heter_conf_test.sh $a1 $a2 $a3
done < 58_reported_cases.txt
