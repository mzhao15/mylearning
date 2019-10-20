
### use warcinio to stream warc files

import warc
# import json
from datetime import datetime
import time
import re

pre = "https://commoncrawl.s3.amazonaws.com/"
# pre = "s3://commoncrawl/"

with open("warc.paths","r") as paths:
	# count = 0
	# for path in paths:
	# 	path = pre + path
	# 	count += 1
	# 	print(path)
	# print(count)

	# only process the first file for practice
	path = paths.readline()
	path = pre + path
	print(path)

	with warc.open("CC-MAIN-20160205193905-00000-ip-10-236-182-209.ec2.internal.warc.gz","r") as records:
		
		recordnum = 0
		with open("warc_output.txt","w") as fout:
			for record in records:
				# WARC records have three different types:
        		#  ["application/warc-fields", "application/http; msgtype=request", "application/http; msgtype=response"]
        		# We're only interested in the HTTP responses
				if record.header['content-type'] != 'application/http; msgtype=response':
					continue

				if recordnum < 1000000:
					try:
						content = record.payload.read().decode("utf-8")
						# print(content)
						# The HTTP response is defined by a specification: first part is headers (metadata)
	            		# and then following two CRLFs (newlines) has the data for the response
						header, body = content.strip().split('\r\n\r\n', 1)
						# print(header)
						# fout.write(content)

						# print(record.header['WARC-Target-URI'])
						domain = re.compile(r'amazon\.com')
						match = re.search(domain,record.header['WARC-Target-URI'])
						if match:
							print("Yes")
					except:
						# print("there is a decoding error")
						pass
					recordnum += 1
				else:
					break

	
def fun_timestamp():					
	# create unix timestamp
	print(datetime.now())  
	tt = datetime.utcnow().timestamp()
	print(tt)
	ut = datetime.utcfromtimestamp(tt)
	print(ut)
	time.sleep(1)