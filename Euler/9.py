for a in range(1001):
	for b in range(1001):
		for c in range(1001):
			if(a+b+c==1000 and (a<b and b<c) and ((a**2+b**2)==c**2)):
				print(a*b*c)
				break
