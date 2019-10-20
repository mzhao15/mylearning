
import json
import gzip
import os
import re
# import warc
# from gzipstream import GzipStreamFile

pre = "https://commoncrawl.s3.amazonaws.com/"
# pre = "s3://commoncrawl/"

with open("wat.paths","r") as paths:
	# for path in paths:
	# 	path = pre + path
	# 	print(path)
	path = paths.readline()
	path = pre + path
	# print(path)

	# key = "CC-MAIN-20160624154951-00000-ip-10-164-35-72.ec2.internal.warc.wat.gz"
	# with warc.WARCFile(fileobj=GzipStreamFile(key)) as data:
	with gzip.open("CC-MAIN-20160624154951-00000-ip-10-164-35-72.ec2.internal.warc.wat.gz","r") as data:
		# print(dir(data))	
		linenum = 1
		recordnum = 0
		k = 0

		sample = []
		# for line in data:
		# 	print(line)
		with open("output.txt","w") as fout:
			for line in data:
				# fout.write(line.decode("utf-8"))
				# skip file header
				if linenum < 27:
					pass
				elif linenum%22 == 1:
					if recordnum < 100:
						try:
							fout.write(line.decode("utf-8"))
							record = json.loads(line)
							title = record['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']["HTML-Metadata"]["Head"]["Title"]
							# IPad = record['Envelope']['WARC-Header-Metadata']['WARC-IP-Address']
							metas = record['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']["HTML-Metadata"]["Head"]["Metas"]
							
							# r'\s[Mm]ovies?' r'\sAI\s' r'https?(www.)?\w+\.\w+' r'[Ee]ducation'
							pattern = re.compile(r'\s[Mm]ovies?')

							# if re.search(pattern,title):
							# # if "Movie" in title:
							# 	k += 1
							# 	sample.append(title)

							# matches = re.findall(pattern,title)
							# if matches:
							# 	# print(type(matches))
							# 	count = len(matches)
							# 	print(count)
							
							for num_meta in range(len(metas)):	
								if 'name' in metas[num_meta].keys():
									if metas[num_meta]['name'] == 'keywords':
										try:
											# print(metas[num_meta]['name'])
											matches = re.findall(pattern, metas[num_meta]["content"])
											if matches:
												print(len(matches))
										except:
											print('this web does not have keywords')
							recordnum += 1
						except:
							pass
					else:
						break
				linenum += 1

		# print("The number of movies are {}".format(k))
		# for num in range(len(sample)):
		# 	print(sample[num])

