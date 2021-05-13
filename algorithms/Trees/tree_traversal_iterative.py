
# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printPreorder(root):
    tree = []
    if not root:
        return tree

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        tree.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return tree

# A function to do postorder tree traversal


def printPostorder(root):
    tree = []
    stack1 = []
    stack2 = []
    if not root:
        return tree
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack2.append(node.right)
    while stack2:
        node = stack2.pop()
        tree.append(node.val)
    return tree


def printInorder(root):
    tree = []
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if stack:
                curr = stack.pop()
                tree.append(curr.val)
                curr = curr.right
            else:
                break
    return tree


def treeleverorder(root):
    if not root:
        return
    queue = []
    queue.append(root)

    while queue:
        print(queue[0].val)
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        queue.pop(0)
    return


def treeleverorder2(root):
    if not root:
        return
    queue = []
    res = []
    queue.append(root)
    numofnodes = 1
    while queue:
        temp = 0
        level = []
        while numofnodes:
            print(queue[0].val)
            level.append(queue[0].val)
            numofnodes -= 1
            if queue[0].left:
                queue.append(queue[0].left)
                temp += 1
            if queue[0].right:
                queue.append(queue[0].right)
                temp += 1
            queue.pop(0)
        res.append(level)
        numofnodes = temp
    return res


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# print("Preorder traversal of binary tree is")
# print(printPreorder(root))

# print("\nInorder traversal of binary tree is")
# printInorder(root)

print("\nPostorder traversal of binary tree is")
print(printPostorder(root))

# print(treeleverorder2(root))
