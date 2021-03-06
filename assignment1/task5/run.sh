#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=1 \
-D mapreduce.partition.keycomparator.options=-k1,1nr \
-input /user/s1626868/assignment1/task4/ \
-output /user/s1626868/assignment1/task5/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-numReduceTasks 1
