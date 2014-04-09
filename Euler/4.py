def is_Pal(string):
	for x in range(len(string)):
		if(len(string)==1):
			return True
		if(len(string)<=2):
			if(string[0]==string[1]):
				return True
			else:
				return False
		if(string[0]==string[-1]):
			return is_Pal(string[1:-1])
		else:
			return False

high =0
for x in range(1000,0,-1):
	for y in range(1000,0,-1):
		if(is_Pal(str(x*y))):
			if(x*y)>high:
				high=x*y
				print(high)
	