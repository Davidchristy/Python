'''
This is a pay of using geometric rules for triangles and circles to find pi.
It's super slow and isn't perfect, but one saturday morning I missed my bus
and needed something to fill my time.
'''

import random
import math
total = 0
inside = 0
aprx = 1000000
for x in range(aprx):
	if math.sqrt(random.random()**2+random.random()**2) < 1: inside+=1
	pi = (inside/(x+1))*4
print(pi)
