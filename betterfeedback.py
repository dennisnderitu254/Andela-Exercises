# Get two integers from the user
dividend, divisor = eval(input('Please enter two numbers to divide: '))
# If possible, divide them and report the result
if divisor != 0:
print(dividend, '/', divisor, "=", dividend/divisor)
else:
print('Division by zero is not allowed')