def strSubsets(str):
	if not str:
		return [""]
	#store the result for str[1:]
	arr = strSubsets(str[1:])
	#for elem in arr, add str[0]+elem as a subset
	return [str[0]+s for s in arr] + arr

s = "abc"
print strSubsets(s)#return ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']