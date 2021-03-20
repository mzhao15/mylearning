from collections import Counter

a = [1, 2, 2]

print(a.count(1))

b = Counter(a)
print(b)
print(type(b))
print(b[2])
