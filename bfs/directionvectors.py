from collections import deque

grid = [
	["S", ".", ".", "#", ".", ".", "."],
	[".", "#", ".", ".", ".", "#", "."],
	[".", "#", ".", ".", ".", ".", "."],
	[".", ".", "#", "#", ".", ".", "."],
	["#", ".", "#", "E", ".", "#", "."]
]

dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]
visited = [
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False]
]

prev = [
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False],
	[False,False,False,False,False,False,False]
]

#assume they give starting node.
R = 5 #total rows
C = 7 #total columns
starting = (0,0)
r = 0 #x
c = 0 #y

q = deque()
q.append(starting)
visited[r][c] = True

def bfs():
	end = False
	move_count = 0
	nodes_left_in_layer = 1
	nodes_in_next_layer = 0
	while len(q) > 0:
		node = q.popleft()
		r = node[0]
		c = node[1]
		print(node)
		#check for end path
		if grid[r][c] == "E":
			end = True
			break
		for i in range(4):
			rr = r + dr[i]
			cc = c + dc[i]
			if rr < 0 or cc < 0:
				continue
			if rr >= R or cc >= C:
				continue
			else:
				if grid[rr][cc] != "#" and visited[rr][cc] == False:
					#add to queue
					q.append((rr, cc))
					#make visited
					visited[rr][cc] = True
					nodes_in_next_layer += 1
		nodes_left_in_layer -=1 
		if nodes_left_in_layer == 0:
			nodes_left_in_layer = nodes_in_next_layer
			nodes_in_next_layer = 0
			move_count += 1
	if end:
		return move_count
	else:
		return -1
#search layers
print(bfs())
				