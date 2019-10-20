def zigzagLevelOrder(root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	ans = []
	if not root:
		return ans
	queue = [root,]
	row = []
	rownum = 0
	currnum = 1
	nextnum = 0
	while queue:
		if currnum and queue:
			node = queue.pop(0)
			row.append(node.val)
			currnum -= 1
			children = []
			if node.left:
				nextnum += 1
				children.append(node.left)
			if node.right:
				nextnum += 1
				children.append(node.right)
			if rownum%2 != 0 and len(children) == 2:
				print("%d %d"%(rownum,1))
				children.reverse()
			queue.extend(children)
		elif not currnum:
			queue.reverse()
			ans.append(row)
			row = []
			currnum = nextnum
			nextnum = 0
			rownum += 1
	ans.append(row)
	return ans


print(zigzagLevelOrder(root))