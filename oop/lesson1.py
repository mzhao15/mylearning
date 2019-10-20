
# empty class
# class employee:
# 	pass

"""class name always starts with capital letter"""

class Employee():
	# constructor function
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last +'@company.com'

	# require to pass 'self' argument 
	def full_name(self):
		return '{} {}'.format(self.first,self.last)


emp1 = Employee('meng', 'zhao', 100)

print(emp1)
print(emp1.email)
print(emp1.full_name())
