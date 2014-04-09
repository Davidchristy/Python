def sum_of_Sqaure(num):
	total = 0
	for x in range(1,num+1):
		total += x**2
	return total

def square_of_sum(num):
	total = 0
	for x in range(1,num+1):
		total += x
	total=total**2
	return total

temp = square_of_sum(100)
temp2 = sum_of_Sqaure(100)
print(temp,"-",temp2,"=",(temp-temp2))