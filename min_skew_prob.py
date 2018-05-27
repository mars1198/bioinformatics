def skew(s):
	c = 0
	g = 0
	min_skew = 0
	skew_list = []
	index = 0
	for i in s:
		index += 1
		if i == 'C':
			c += 1
		if i == 'G':
			g += 1
		skew = g-c
		if skew < min_skew:
			skew_list = [index]
			min_skew = skew
		if skew == min_skew and index not in skew_list:
			skew_list.append(index)	
	print(skew_list)

print (skew('GCATACACTTCCCAGTAGGTACTG'))
