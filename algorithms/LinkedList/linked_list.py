from LinkList import ListNode,listprint

def deleteDuplicates(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	if not head or not head.next: return head
	l1,l2 = head, head.next
	dummynode = l1
	while l2:
		if l1 != l2:
			l1.next = l2
			l1 = l1.next
		l2 = l2.next
	l1.next = None
	return dummynode

# leetcode 24: swap pairs
def swapPairs(head):
	if not head or not head.next:
		return head
	
	dummynode = ListNode(0)
	dummynode.next = head
	pre = dummynode
	first = head
	second = head.next
	while first and second:
		pre.next = second
		nex = second.next
		second.next = first
		first.next = nex

		pre = first
		if first.next:
			second = first.next.next
			first = first.next
		else:
			break
	return dummynode.next

#leetcode 725: Split Linked List in Parts
def splitListToParts(root,k):
	
	nlist = 0
	lis = root
	while lis:
		nlist += 1
		lis = lis.next
	n = nlist//k
	rem = nlist%k
	size = [0]*k
	for i in range(k):
		if i<rem:
			size[i] = n+1
		else:
			size[i] = n
	res = []
	for i in range(k):
		temp = []
		if size[i] != 0:
			while root and size[i]!=0:
				temp.append(root.val)
				root = root.next
				size[i] -= 1
		res.append(temp)
	return res

def rotateRight(head,k):
	nlist = 0
	cur = head
	while cur:
		nlist += 1
		if cur.next == None:
			end = cur
		cur = cur.next
	n = nlist - k%nlist
	cur = head
	for i in range(n-1):
		cur = cur.next
	listprint(cur)
	end.next = head
	head = cur.next
	cur.next = None
	return head

# leetcode 143: Reorder List
def reorderList(head):
	pass

# leetcode 19: Remove Nth Node From End of List
def removeNthFromEnd(head,n):
	dummy = ListNode(0)
	dummy.next = head
	fast = dummy
	while n:
		fast = fast.next
		n -= 1
	listprint(fast)
	slow = dummy
	while fast.next:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return dummy.next

e1 = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
e4 = ListNode(4)
e5 = ListNode(5)
e6 = ListNode(6)
e7 = ListNode(7)
head = e1
e1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
listprint(head)
print('-----')

listprint(removeNthFromEnd(head,7))



