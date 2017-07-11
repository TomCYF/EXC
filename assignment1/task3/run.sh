#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-input  /user/s1626868/assignment1/task2/ \
-output /user/s1626868/assignment1/task3/ \
-mapper /bin/cat \
-reducer reducer.py \
-file reducer.py \
-numReduceTasks 1
