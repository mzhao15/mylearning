from faker import Faker
import random
import math

def randphn():
	'''generate a random phone number: 10 digits'''
	phn = str(random.randint(100,999))
	for _ in range(7):
		phn = phn + str(random.randint(0,9))
	# print(len(phn))
	return phn

def clean_name(name):
	''' remove the prefix and suffix: Mr. Dr. Mrs. Jr. Sr. etc.'''
	if '.' not in name:
		return name
	else:
		words = name.split()
		for i, word in enumerate(words):
			if '.' in word:
				del words[i]
		return ' '.join(words)

def user_generator(num_user):
	users = []
	fake = Faker('en_US')
	domains = ('@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com', '@msn.com', '@comcast.net',
		'@live.com', '@att.net', '@facebook.com', '@rocketmail.com', '@outlook.com', '@ymail.com')
	digits = int(math.log10(num_user))+1
	# f_user = open('users.json','w')
	for i in range(num_user):
		user = {}

		user['usrid'] = 'id' + str(i).zfill(digits)
		name = fake.name()
		user['name'] = name
		user['phone_number'] = randphn()
		user['address'] = fake.address().replace('\n',', ')
		user['age'] = randint(15)

		if '.' in name:
			name = clean_name(name)
		user['email'] = name.replace(' ','_') + str(i) + random.choice(domains)
		# print(user['email'])
		# address = fake.address().replace('\n',', ')
		# location = address.split()
		# user['state'] = location[-2]
		# user['address'] = address

		users.append(user)
		# f_user.write(json.dumps(user))
		# f_user.write('\n')
	# f_user.close()
	return users

if __name__ == '__main__':
	users = user_generator(100)
	# print(len(users))
	# print(users[-1]['usrid'])

