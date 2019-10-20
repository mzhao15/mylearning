class Node:
	def __init__(self, dataval=None):
		self.val = dataval
		self.next = None

def deleteDuplicates(self, head):

	if not head and not head.next:
		return head
	cur = head
	while cur:
		node = cur
		while node == node.next and node:
			node = node.next
		cur.next = node.next
		cur = cur.next
	return head

head = Node(1)
head.next = Node(1)
head.next.next = Node(2)

while head:
	print(head.val)
	head = head.next