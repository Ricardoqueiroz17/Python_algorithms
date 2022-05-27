#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /proj1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/ny_transit.txt /proj1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/proj1/mappertype.py -mapper ../../mapreduce-test-python/proj1/mappertype.py \
-file ../../mapreduce-test-python/proj1/reducertype.py -reducer ../../mapreduce-test-python/proj1/reducertype.py \
-input /proj1/input/* -output /proj1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /proj1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /proj1/output/
../../stop.sh
