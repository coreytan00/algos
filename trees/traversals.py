"""
A Tree is typically traversed in two ways:

Breadth First Traversal (Or Level Order Traversal)
Depth First Traversals
	Inorder Traversal (Left-Root-Right)
	Preorder Traversal (Root-Left-Right)
	Postorder Traversal (Left-Right-Root)
"""
#remember, trees are basically directed graphs.
#think about whether breadth or depth suits the problem more!

#root -1, 0
class TN:
	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

root = TN(1)
root.left = TN(2)
root.right = TN(3)
root.left.left = TN(4)
root.left.right = TN(5)
root.right.left = TN(6)
root.right.right = TN(7)
#        1
#       / \
#      2   3
#     / \  / \
#    4   5 6  7
#preorder - root, left, right
def preorder(root):
	if root != None:
		print(root.val, end='')
		preorder(root.left)
		preorder(root.right)

preorder(root)
print() 

def inorder(root):
	if root != None:
		inorder(root.left)
		print(root.val, end='')
		inorder(root.right)

inorder(root)
print() 

def postorder(root):
	if root != None:
		postorder(root.left)
		postorder(root.right)
		print(root.val, end='')

postorder(root)
print() 