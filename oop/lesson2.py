
class Employee():

	# class variables, cannot be changed thru instance
	# can be changed thru class: Empoyee.raise_amount = 1.05
	raise_amount = 1.04
	num_of_emps = 0

	# constructor function
	def __init__(self, first, last, pay):
		# instance variables
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last +'@company.com'
		Employee.num_of_emps += 1

	# require to pass 'self' argument 
	def full_name(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	# class methods
	@classmethod
	# first argument is always cls
	def set_raise_amount(cls,amount):
		cls.raise_amount = amount

	# additional constructor
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)



emp1 = Employee('meng', 'zhao', 100)
emp2 = Employee('test', 'user', 200)
# emp1.apply_raise()
# print(emp1.pay)
# print(emp2.num_of_emps)

Employee.set_raise_amount(1.05)
print(emp1.raise_amount)



## subclass

class Developer(Employee):
	# override this attribute in Employee. but it wont change Employee's attribute
	raise_amount = 1.10
	def __init__(self, first, last, pay，prog_lang):
		super().__init__(first,last,pay)
		## above method and below method is equivalent
		# Employee._init__(first,last,pay)
		self.prog_lang = prog_lang

dev_1 = Developer('meng', 'zhao', 100,'python')
dev_2 = Developer('test', 'user', 200,'java')

print(dev_1.email)
print(dev_2.email)