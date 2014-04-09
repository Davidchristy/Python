def factor(num):
	for x in range(2,num+1):
		if(num%x==0):
			print(num)
			num = factor(int(num/x))
			return num
print(factor(600851475143))