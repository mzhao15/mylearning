from user_generator import user_generator
from movie_generator import movie_generator
import random
import json
import math
from datetime import datetime,timedelta

title_path = 'title.basics.tsv.gz'
rating_path = 'title.ratings.tsv.gz'
num_users = 10
users = user_generator(num_users)
movies = movie_generator(title_path,rating_path)

starttime = datetime(2018,8,1,22,00,00)
endtime = datetime(2018,8,1,23,00,00)
userEndTime = [starttime]*num_users
defaultRunTime = {'short':5, 'movie':120, 'tvMovie':100, 'tvSeries':40, 'tvEpisode':40, 'tvShort':20, 'tvMiniSeries':5, 'tvSpecial':60, 'video':20, 'videoGame':10}

def notWatching(user_index,current_time):
	'''tell if the user is watching or not
	not watching, return 1, watching return 0'''
	if userEndTime[user_index] <= current_time:
		return 1
	else:
		return 0

def watchOrNot(current_time):
	'''return whether the user will watch or not based on some probability distribution function'''
	hour = current_time.hour
	angle = (hour-17)/12*math.pi
	prob = round(40 + 45*math.sin(angle) - 10*math.sin(angle))
	randnum = random.randint(1,100)
	# print('{},{}'.format(randnum,prob))
	if randnum <= prob:
		return 1
	else:
		return 0

	# # 75% chance to watch movies during these hours
	# if hour > 20 or hour < 1:
	# 	randnum = random.randint(1,4)
	# 	if randnum < 4:
	# 		return 1
	# 	else:
	# 		return 0
	# else:
	# 	# 10% chance to watch movies
	# 	randnum = random.randint(1,10)
	# 	if randnum < 2:
	# 		return 1
	# 	else:
	# 		return 0

def movieRunTime(movie):
	'''return the runtime of a movie. if not given, use the default values'''
	if movie['runtimeMinutes'] != '\\N':
		runTime = int(movie['runtimeMinutes'])
	else:
		runTime = defaultRunTime[movie['type']]
	return runTime

def data_generator():
	'''generating events with user and movie information and save it to hdfs
	'''
	current_time = starttime
	# fout = open('output.txt','w')
	while current_time < endtime:
		# timestamp = current_time.timestamp()
		timestamp = current_time.strftime('%Y%m%d%H%M%S')
		# print(timestamp)
		for user_index, user in enumerate(users):
			event = {}
			# note: watchOrNot function generates random boolean number
			if notWatching(user_index,current_time) and watchOrNot(current_time):
				movie = random.choice(movies)
				runTime = movieRunTime(movie)
				userEndTime[user_index] = current_time + timedelta(minutes=runTime)
				# print('{}, {}'.format(user['name'],userEndTime[user_index]))

				# each event includes an event key, a user and a movie
				event['key'] = user['usrid'] + '_' + timestamp
				event['user'] = user
				event['movie'] = movie
				# print(event['key'])
		current_time += timedelta(minutes=3)
	# fout.close()

if __name__ == '__main__':
	data_generator()