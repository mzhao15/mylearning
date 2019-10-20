
import gzip

def ratinginfo(rating_path):
	num_rating = 0
	with gzip.open(rating_path,'r') as ratings:
		for line in ratings:
			# skip the header
			if num_rating == 0:
				num_rating += 1
				continue
			else:
				rating = line.decode('utf-8').strip()
				yield rating.split('\t')
				# ID, averageRating, numVotes

def titleinfo(title_path):
	num_title = 0
	with gzip.open(title_path,'r') as titles:
		for line in titles:
			# skip the header
			if num_title == 0:
				num_title += 1
				continue
			else:
				title = line.decode('utf-8').strip()
				yield title.split('\t')
				# ID, type, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres

def movie_generator(title_path,rating_path):
	# title.basics.tsv.gz
	# title.ratings.tsv.gz
	movies = []
	titles = titleinfo(title_path)
	ratings = ratinginfo(rating_path)
	types = ['short','tvEpisode','movie', 'tvMovie', 'tvSeries','tvShort','tvMiniSeries', 'tvSpecial', 'video']
	# 'short','tvEpisode'
	num = 0

	for title, rating in zip(titles,ratings):
		movie = {}
		# print(title)
		# print(rating)
		if num < 1000000:
			if title[1] in types:
				movie['ID'] = title[0]
				movie['type'] = title[1]
				movie['primaryTitle'] = title[2]
				movie['originalTitle'] = title[3]
				movie['isAdult'] = title[4]
				movie['startYear'] = title[5]
				movie['endYear'] = title[6]
				movie['runtimeMinutes'] = title[7]
				movie['genres'] = title[8]
				movie['rating'] = rating[1]
				movie['numVotes'] = rating[2]
				movies.append(movie)
				num += 1
				print('{},{},{}'.format(movie['genres'],movie['runtimeMinutes'],movie['rating']))
		else:
			break
	return movies

if __name__ == '__main__':
	title_path = 'title.basics.tsv.gz'
	rating_path = 'title.ratings.tsv.gz'
	movies = movie_generator(title_path,rating_path)
	print(len(movies))
	# print(movies[-1])


# movie types:
#['short', 'movie', 'tvMovie', 'tvSeries', 'tvEpisode', 'tvShort', 'tvMiniSeries', 'tvSpecial', 'video', 'videoGame']




