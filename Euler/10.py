import timeit
primes = [2,3]

def is_prime(curnum,primes):
	for x in range(len(primes)):
		if curnum**(4/8)>=primes[x]:
			if(curnum%primes[x]==0):
				return False
		else:
			break
	primes+=[curnum]
	return True
def main():	
	for x in range(2,2000000):
		is_prime(x,primes)

print(timeit.timeit(main,number=1))
print(len(primes))