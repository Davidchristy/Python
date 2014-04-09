factors = [1]

def doesFactorsContain(x):
	for i in range(len(factors)):
		if factors[i] == x:
			return True
	return False

def factor(num,factors):
	for x in range(2,num+1):
		if(num%x==0):
			if not doesFactorsContain(x):
				factors += [x]
			# print(num)
			factor(int(num/x),factors)

high = 0

for x in range(28):
	factor(x,factors)
	if (len(factors)>high):
	 	high = len(factors)
	 	print(high)
	if len(factors)>500:
		print(x)
		break
	# factors = [1]


print(factors)
print(len(factors))