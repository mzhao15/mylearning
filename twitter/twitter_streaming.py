
import time
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials
 
# consumer_key = 'eBsE7dv4w9rQNo28G684fGXqh'
# consumer_secret = 't8rIQyH2XX2KPQCWF8aQS9D5EP3msEpXWwDNW95qJlvqqdBBbU'
# access_token = '805975346407411712-GwxPmRUzBuZMztkHiMKVNmqYcVo14EJ'
# access_secret = 'PthC1uV06tPgpc1jR5jPSjqvVg7Ab5am09uoJ9MHBMFoa'
 
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
 
# api = tweepy.API(auth)

# # read our own timeline (i.e. our Twitter homepage)
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status.text)

class MyListener(StreamListener):
 
    # def on_status(self,status):
    #     try:
    #         with open('python2.txt', 'a') as f:
    #             f.write(status.text)
    #             print(status.text)
    #             return True
    #     except BaseException as e:
    #         print("Error on_data: %s" % str(e))
    #         pass
    #     return True

    def on_data(self, data):
        try:
            with open('tweets.txt', 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        if status == 402:
        	return False
 
twitter_stream = Stream(auth, MyListener())
# twitter_stream.sample()
twitter_stream.filter(track = ["cricket"], languages = ["en"])   #track=['#python']

