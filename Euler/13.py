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

for x in range(5,2000000,primes[0]):
	is_prime(x,primes)

print(primes)
total = 0
for x in range(len(primes)):
	total+=primes[x]
print(total)
"""
def is_prime(curnum,primes):
	for x in range(len(primes)):
		if(curnum%primes[x]==0):
			return False
	primes+=[curnum]
	return True
"""