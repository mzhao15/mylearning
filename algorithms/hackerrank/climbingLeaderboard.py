def climbingLeaderboard(scores, alice):
	rank = {}
	count = 1
	for score in scores:
		if score not in rank:
			rank[score] = count
			count += 1
	res = []
	for score in alice:
		if score >= scores[0]:
			res.append(1)
			continue
		if score < scores[-1]:
			res.append(rank[scores[-1]]+1)
			continue
			
		l = 0
		r = len(scores)-1
		while l+1<r:
			mid = l + (r-l)//2
			if scores[mid] == score:
				res.append(rank[score])
				break
			elif scores[mid] > score:
				l = mid
			else:
				r = mid
		if scores[mid] != score:
			res.append(rank[scores[r]])
	return res


scores = [100,100, 50, 40, 40, 20, 10] 
alice = [5, 25, 50, 120]
print(climbingLeaderboard(scores,alice))