hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.partition.keycomparator.options=-k1,1nr \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/s1626868/assignment2/task4_temp \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-numReduceTasks 1

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.partition.keycomparator.options=-k1,1nr \
-input /user/s1626868/assignment2/task4_temp \
-output /user/s1626868/assignment2/task4 \
-mapper /bin/cat \
-reducer reducer2.py \
-file reducer2.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-numReduceTasks 1


