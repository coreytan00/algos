class TN:
	def __init__(self, value=0):
		self.val = value
		self.left = None
		self.right = None

t1 = TN(1)
t1.left = TN(2)
t1.right = TN(3)
t1.left.left = TN(4)
t1.left.right = TN(5)
t1.right.left = TN(6)
t1.right.right = TN(7)

t2 = TN(1)
t2.left = TN(2)
t2.right = TN(3)
t2.left.left = TN(4)
t2.left.right = TN(5)
t2.right.left = TN(6)
t2.right.right = TN(7)


def merge(t1, t2):
	if t1 and t2:
		#if both are not none and are tree nodes
		root = TN(t1.val + t2.val)
		root.left = merge(t1.left, t2.left)
		root.left = merge(t1.right, t2.right)

		return root
	else:
		# return the node that isn't none
		return t1 or t2

merge(t1, t2)



