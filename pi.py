import random
import math
total = 0
inside = 0
for x in range(1000000):
	if math.sqrt(random.random()**2+random.random()**2) < 1: inside+=1
	pi = (inside/(x+1))*4
print(pi)
