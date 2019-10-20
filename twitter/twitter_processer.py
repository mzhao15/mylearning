import json

with open("tweets.txt","r") as f:
	for line in f:
		try:
			tweet = json.loads(line.strip())
			if 'text' in tweet:
				# print(tweet['user']['name'])
				print(tweet['text'])
				if tweet['entities']['hashtags']:
					hashtags = []
					for hashtag in tweet['entities']['hashtags']:
						hashtags.append(hashtag['text'])
					print(hashtags)
				# print(tweet['created_at'])
				print('__________________________________________________________')				
		except:
			continue