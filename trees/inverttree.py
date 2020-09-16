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

# initial solution
def invertTree(root: TN) -> TN:
    if root:
        temp = root.left
        root.left = root.right
        root.right = temp
        invertTree(root.left)
        invertTree(root.right)
        return root
        
# another solution
def invertTree2(root):
	if root:
		root.left, root.right = invertTree2(root.right), invertTree2(root.left) #need to be written together.
		return root

tn = invertTree2(root)

print(tn.val)
print(tn.left.val)
print(tn.right.val)
print(tn.left.left.val)
print(tn.left.right.val)
print(tn.right.left.val)
print(tn.right.right.val)


#      1
#    3   2
#  7  6 5  4
#
#
