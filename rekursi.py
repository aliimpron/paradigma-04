def fact_recursion(n):

	if n == 1:
		return 1
	
	return n * fact_recursion(n-1)

factorial = fact_recursion(6)
print("6! = "+str(factorial))

