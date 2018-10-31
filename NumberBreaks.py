
def find_break_points(p):
	p = [0] + p + [len(p)+1]
	num = 0
	for i in range(len(p)-1):
		if p[i+1]-p[i] != 1:
			num += 1
	return num

if __name__ == '__main__':
	P = ''
	P = list(map(int,P[1:-1].split(' ')))
	print (find_break_points(P))
