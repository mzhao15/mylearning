def readBinaryWatch(num):
	res = []
	temp = [0]*10
	if num <= 0 or (num > 10):
		return
	readBinaryWatchHelper(0,num,res,temp)
	return res 

def gettime(r):
	hour = 0
	minute = 0
	power = 3
	for i in range(4):
		hour += r[i]*(2**power)
		power -= 1
	power = 5
	for i in range(4,10):
		minute += r[i]*(2**power)
		power -= 1
	minute = str(minute).zfill(2)
	return [str(hour),minute]


def readBinaryWatchHelper(st_num,num,res,temp):
	if num == 0:
		# hour,minute = gettime(temp)
		# if int(hour) < 12 and int(minute) < 60:
		# 	res.append(':'.join([hour,minute]))
		res.append(temp[:])
	else:
		for i in range(st_num,10):
			temp[i] = 1
			readBinaryWatchHelper(i+1,num-1,res,temp)
			temp[i] = 0


res = readBinaryWatch(2)
for result in res:
	print(result)