def div(num):
	for y in range(1,21):
		if(num%y!=0):
			return False
	return True

for x in range(1, 1000000000000000):
	if(div(x)):
		print(x)
		break