a = 1
b = 2
total = 2
'''
Go up to 4000000
'''
def fib(a,b):
	total = 2
	for x in range(1000):
		c = a+b
		a = b
		b = c
		if(c>4000000):
			break
		if(c % 2==0):
			total += c
			print(total)
	return total

print(fib(a,b))


