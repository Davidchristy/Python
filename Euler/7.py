primes = [2,3]

def is_prime(curnum,primes):
	for x in range(len(primes)):
		if curnum**(1/2)>=primes[x]:
			if(curnum%primes[x]==0):
				return False
		else:
			break
	primes+=[curnum]
	return True

x = 5
while len(primes)<10001:
	is_prime(x,primes)
	x=x+1
print(primes[-1])