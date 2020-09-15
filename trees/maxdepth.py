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
root.left.left.left = TN(8)
#        1
#       / \
#      2   3
#     / \  / \
#    4   5 6  7
#   /
#  8

#recursive dfs
def maxdepth(root):
	if not root:
		return 0
	return max(maxdepth(root.left), maxdepth(root.right)) + 1


from collections import deque
#iterative. bfs
def maxdepth2(root):
	q = deque()
	if not root:
		return 0
	q.append(root)
	depth = 0
	layer = 1

	while len(q) != 0:
		tn = q.popleft()
		if tn.left:
			q.append(tn.left)
		if tn.right:
			q.append(tn.right)
		layer -=1
		if layer == 0:
			depth +=1
			layer = len(q)
	return depth

print(maxdepth(root))
print(maxdepth2(root))