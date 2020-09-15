#simple dfs

#undirected graph - what's given
g = [[1,2], [0,3], [0,3], [1,2,4], [3,5,6], [4], [4]]

visited = [False] * 7
starting = 0
stack = [starting]

# iterative
def dfsI():
	visited[starting] = True
	# [0]
	while len(stack) != 0:
		base = stack.pop()
		for node in g[base]:
			#for node 0, we see children 1, 2
			if visited[node] == False:
				stack.append(node)
				visited[node] = True

dfsI()
print(visited)

visited = [False] * 7
starting = 0
stack = [starting]

#recursive
def dfsR(base):
	visited[base] = True
	for node in g[base]:
		if visited[node] == False:
			dfsR(node)

def dfsR2(base):
	if visited[base]:
		return
	visited[base] = True
	for node in g[base]:
		dfsR(node)

dfsR2(starting)
print(visited)