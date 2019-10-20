# definListNode class
class ListNode:
	def __init__(self, dataval=None):
		self.val = dataval
		self.next = None

# define a linked list
def listprint(head):
	arr = []
	while head:
		arr.append(head.val)
		head = head.next
	print(arr)