
from math import *

def numsquares(n):
	cnt = 0
	sq = sqrt(n)
	if sq*sq == sqrt(n):
		return 1
	total = floor(sq)*floor(sq)
	diff = sqrt(n) - total   
	while diff != 0:
		sq = floor(sq)
		while diff > sq:
			total += sq
			cnt += 1
		sq = floor(sqrt(diff))
		diff = diff - 
	return cnt

print(numsquares(13))