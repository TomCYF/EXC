#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input  /user/s1626868/assignment1/task1/ \
-output /user/s1626868/assignment1/task2/ \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py
