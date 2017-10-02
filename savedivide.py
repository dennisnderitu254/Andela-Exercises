# Get the dividend and divisor from the user
dividend, divisor = eval(input('Enter dividend, divisor: '))
# We want to divide only if divisor is not zero; otherwise,
# we will print an error message
if divisor != 0:
	print(dividend/divisor)
else:
	print('Error, cannot divide by zero')
	