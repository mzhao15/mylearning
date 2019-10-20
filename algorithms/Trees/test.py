# Python program to for tree traversals 
# A class that represents an individual node in a 
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key

# A function to do preorder tree traversal 
def printPreorder(root): 
	if root: 
		print(root.val)
		printPreorder(root.left)
		printPreorder(root.right) 

# A function to do inorder tree traversal 
def printInorder(root): 
	if root: 
		printInorder(root.left) 
		print(root.val) 
		printInorder(root.right) 
  
# A function to do postorder tree traversal 
def printPostorder(root): 
	if root: 
		printPostorder(root.left) 
		printPostorder(root.right)  
		print(root.val)

# Function to  print level order traversal of tree 
def printLevelOrder(root): 
	h = height(root) 
	for i in range(1, h+1): 
		printGivenLevel(root, i)

# Print nodes at a given level 
def printGivenLevel(root , level): 
	if root is None: 
		return
	if level == 1: 
		print("%d"%(root.val))
	elif level > 1 : 
		printGivenLevel(root.left , level-1) 
		printGivenLevel(root.right , level-1)
 
""" Compute the height of a tree--the number of nodes 
	along the longest path from the root node down to 
	the farthest leaf node 
"""
def height(node): 
	if node is None: 
		return 0 
	else : 
		# Compute the height of each subtree  
		lheight = height(node.left) 
		rheight = height(node.right) 
		#Use the larger one 
		if lheight > rheight: 
			return lheight+1
		else: 
			return rheight+1

def inorder(root,ans):
	if not root:
		return
	inorder(root.left,ans)
	ans.append(str(root.val))
	inorder(root.right,ans)

def preorder(root,ans):
	if not root:
		return
	ans.append(str(root.val))
	preorder(root.left,ans)
	preorder(root.right,ans)
	

def deserialize_pre(vals):
	if len(vals) == 0:
		return
	left = []
	right = []
	for i in range(1,len(vals)):
		if int(vals[i]) < int(vals[0]):
			left.append(vals[i])
		else:
			right.append(vals[i])
	root = Node(int(vals[0]))
	root.left = deserialize_pre(left)
	root.right = deserialize_pre(right)

	return root

root = Node(8) 
root.left = Node(3) 
root.right = Node(10) 
root.left.left = Node(1) 
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
# print("\nInorder traversal of binary tree is")
# printInorder(root)
# ans = []
# inorder(root,ans)
# ans = ' '.join(ans)
# print(ans)
ans = []
preorder(root,ans)
ans = ' '.join(ans)
print(ans)

vals = ans.split()
newroot = deserialize_pre(vals)
printInorder(newroot)



