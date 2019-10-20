
# https://www.rittmanmead.com/blog/2017/01/getting-started-with-spark-streaming-with-python-and-kafka/

#    Spark
from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json


def createContext():
    sc = SparkContext(appName="PythonSparkStreamingKafka_RM_02")
    sc.setLogLevel("WARN")
    ssc = StreamingContext(sc, 5)
    
    # Define Kafka Consumer
    kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming2', {'twitter':1})
    
    ## --- Processing
    # Extract tweets
    parsed = kafkaStream.map(lambda v: json.loads(v[1]))
    
    # Count number of tweets in the batch
    count_this_batch = kafkaStream.count().map(lambda x:('Tweets this batch: %s' % x))
    
    # Count by windowed time period
    count_windowed = kafkaStream.countByWindow(60,5).map(lambda x:('Tweets total (One minute rolling count): %s' % x))

    # Get authors
    authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])
    
    # Count each value and number of occurences 
    count_values_this_batch = authors_dstream.countByValue()\
                                .transform(lambda rdd:rdd\
                                  .sortBy(lambda x:-x[1]))\
                              .map(lambda x:"Author counts this batch:\tValue %s\tCount %s" % (x[0],x[1]))

    # Count each value and number of occurences in the batch windowed
    count_values_windowed = authors_dstream.countByValueAndWindow(60,5)\
                                .transform(lambda rdd:rdd\
                                  .sortBy(lambda x:-x[1]))\
                            .map(lambda x:"Author counts (One minute rolling):\tValue %s\tCount %s" % (x[0],x[1]))

    # Write total tweet counts to stdout
    # Done with a union here instead of two separate pprint statements just to make it cleaner to display
    count_this_batch.union(count_windowed).pprint()

    # Write tweet author counts to stdout
    count_values_this_batch.pprint(5)
    count_values_windowed.pprint(5)
    
    return ssc




# launch the window streaming process

''' This uses local disk to store the checkpoint data. In a Production deployment this would 
    be on resilient storage such as HDFS.

    Note that, by design, if you restart this code using the same checkpoint folder, it will 
    execute the previous code - so if you need to amend the code being executed, specify a 
    different checkpoint folder. '''
    
ssc = StreamingContext.getOrCreate('/tmp/checkpoint_v01',lambda: createContext())
ssc.start()
ssc.awaitTermination()


