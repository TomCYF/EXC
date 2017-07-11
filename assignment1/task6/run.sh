#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D map.output.key.field.separator=' ' \
-D stream.map.output.field.separator=' ' \
-D stream.num.map.output.key.fields=2 \
-D num.key.fields.for.partition=2 \
-D partition.keypartitioner.options=-k1,2 \
-input  /user/s1626868/assignment1/task4/ \
-output /user/s1626868/assignment1/task6/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
