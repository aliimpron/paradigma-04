def fact_iteration(number):

	fact_val = 1
	
	for n in range(number, 1,-1):
		fact_val = fact_val * n
	return fact_val

factorial = fact_iteration(6)
print("6! = "+str(factorial))

