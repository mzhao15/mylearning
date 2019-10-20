
# https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/

#    Spark
from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json


# create spark context
sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
#optional
sc.setLogLevel("WARN")

# create streaming contexts
# batch duration is set to 60 seconds
ssc = StreamingContext(sc, 60)

# connect to kafka
# topic: twitter
# consumer group: spark-streaming
kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming', {'twitter':1})

# parse the inbound message as json
'''	The inbound stream is a DStream, which supports various built-in transformations such as map 
	which is used here to parse the inbound messages from their native JSON format.
	Note that this will fail horribly if the inbound message isn't valid JSON.'''
parsed = kafkaStream.map(lambda v: json.loads(v[1]))

# count the number of tweets in the batch
''' the DStream object 'parsed' has built-in functions: count and pprint 
	pprint only prints the first 10 values '''
parsed.count().map(lambda x:'Tweets in this batch: %s' % x).pprint()


# extract author name from each tweet
authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])


# count the number of tweets per anthor
author_counts = authors_dstream.countByValue()
author_counts.pprint()


# sort the author count
''' sort is not a built-in DStream function. instread use the 'transform' function to access
	'sortBy s'from pySpark'''
author_counts_sorted_dstream = author_counts.transform((lambda foo:foo.sortBy(lambda x:( -x[1]))))
author_counts_sorted_dstream.pprint()


# get top 5 authors by tweet count
top_five_authors = author_counts_sorted_dstream.transform\
  (lambda rdd:sc.parallelize(rdd.take(5)))
top_five_authors.pprint()


# streaming starts here
ssc.start()
ssc.awaitTermination()