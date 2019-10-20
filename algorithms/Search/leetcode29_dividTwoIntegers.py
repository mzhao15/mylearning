
def divide(dividend, divisor):
	if dividend*divisor>0:
		sign = 1
	else:
		sign = -1
	dividend = abs(dividend)
	divisor = abs(divisor)
	res = 0
	while dividend >= divisor:
		temp = divisor
		i = 1
		while dividend >= temp:
			dividend -= temp
			res += i
			temp <<= 1
			i <<= 1
	return sign*res

dividend = 10
divisor = 3
print(divide(dividend,divisor))