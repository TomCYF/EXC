#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input /data/assignments/ex1/uniLarge.txt \
-output /user/s1626868/assignment1/task8/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-numReduceTasks 1
