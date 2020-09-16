arr = [1,1,1,1,2,2,3]
arr2 = [2,2,3,4,5,2,2,2,2]
#majority element -- > n/2 and assume there is always majority 

#initial solution -- can also be done with defaultdict
def majority(arr):
	hm = {}
	for num in arr:
		if num not in hm:
			hm[num] = 1
		else:
			hm[num] += 1
	return max(hm, key=lambda x:hm[x])

print(majority(arr))
print(majority(arr2))

#O(1) space O(N) time - Boyer-Moore Majority Vote Algorithm
def moore(arr):
    major=arr[0]
    count = 1
    for i in range(len(arr)):
    	if count == 0:
    		count += 1
    		major = arr[i]
    	elif major==arr[i]:
    		count+=1
    	else:
        	count-=1
    return major;

print(moore(arr))
print(moore(arr2))
