
# backtracking
# def restoreIpAddresses(s):
# 	res = []
# 	if not s:
# 		return res
# 	temp = []
# 	helper(s,0,res,temp)
# 	return res

# def helper(s,pos,res,temp):
# 	if pos == 4:
# 		if not s:
# 			res.append('.'.join(temp[:]))
# 		return
# 	for i in range(1,4):
# 		if i<=len(s):
# 			if i==1:
# 				temp.append(''.join(s[:1]))
# 				helper(s[1:],pos+1,res,temp)
# 				temp.pop()
# 			elif i==2 and s[0]!='0':
# 				temp.append(''.join(s[:2]))
# 				helper(s[2:],pos+1,res,temp)
# 				temp.pop()
# 			elif i==3 and s[0]!='0' and int(''.join(s[:3]))<256:
# 				temp.append(''.join(s[:3]))
# 				helper(s[3:],pos+1,res,temp)
# 				temp.pop()

# brutal force
def restoreIpAddresses(s):
	res = []
	for i in range(1,4):
		for j in range(1,4):
			for k in range(1,4):
				temp = [s[:i],s[i:i+j],s[i+j:i+j+k],s[i+j+k:]]
				if len(temp[3])<4:
					flag = True
					for i in range(4):
						if len(temp[i])>1 and temp[i][0]=='0':
							flag = False
						if len(temp[i]) == 3 and int(''.join(temp[i]))>255:
							flag = False
					if flag:
						res.append('.'.join(temp[:]))
	return res

s = '25525511135'
print(restoreIpAddresses(s))