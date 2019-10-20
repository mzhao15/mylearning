import os
from datetime import datetime,date,time

print(os.getcwd())

if not os.path.exists('test'):
	os.mkdir('test')

path = os.path.join(os.getcwd(),'test')
filename = os.path.basename(path)
print(filename)
pathname = os.path.dirname(path)
print(pathname)

print(os.path.split(os.path.join(os.getcwd(),'test')))


print(datetime.now())
print(date.today())
tdy = datetime.today()
print(tdy.day)

str_tdy = tdy.strftime('%m %d,%Y')
print(str_tdy)

tdy2 = datetime.strptime(str_tdy,'%m %d,%Y')
print(tdy2)