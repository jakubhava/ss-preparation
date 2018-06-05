#!/bin/bash
s3cmd del --force --recursive s3://h2o-spark-summit-data
rm -rf spark-summit-demo-data
mkdir spark-summit-demo-data
counter=0
while :
do
    echo Generating Row $counter
    python generate_single_row.py $counter
    s3cmd put --acl-public spark-summit-demo-data/$counter.csv s3://h2o-spark-summit-data/$counter.csv
	counter=$((counter+1))
    sleep 2
done
