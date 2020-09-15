lst = ['a', 'b', 'c', 'd']
string = "abc"

def perm(lst):
	res = [] 
	print("current lst is: ", lst)
	if len(lst) == 0: #empty input
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		for i in range(len(lst)):
			x = lst[i] #takes current element "a"
			xs = lst[:i] + lst[i+1:] #all the other elemnts "bc"
			for p in perm(xs):
				res.append([x] + p)
		return res

def perm2(lst):
	#switch
	pass


for p in perm2(lst):
	print(p)
