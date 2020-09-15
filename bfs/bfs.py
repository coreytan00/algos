import collections
#simple bfs

#undirected graph - what's given
g = [[1,2], [0,3], [0,3], [1,2,4], [3,5,6], [4], [4]]

visited = [False] * 7
q = collections.deque()
starting = 0
q.append(0)
#append, appendleft, pop, popleft 

#iterative
def bfsI():
	visited[starting] = True
	while len(q) != 0:
		base = q.popleft()
		for node in g[base]:
			if visited[node] == False:
				q.append(node)
				visited[node] = True

bfsI()
print(visited)

#recursive??