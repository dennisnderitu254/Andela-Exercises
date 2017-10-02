"""
A Fibonacci sequence is a sequence of two numbers where each successive number is the sum of the previous two.
The class Fibonacci sequence begins 1,1,2,3,5,8,13,.. ..

Write a program that computes the nth Fibonacci number where n is a value input by the user.For Example
n=6, then the result is 8.
"""

n = int(raw_input("Enter the number to use:"))
fib = [0,1]

for i in range(1,n):
	fib.append(fib[i] + fib[i-1])
print(fib[n])

"""
OR

while True:
	try:
		n=int(input("Enter the number of the fib sequence you need:"))
		break
	except:
		print("Enter a valid number!")

fib=[1,1]
for i in range(1,n):
	fib.append(fib[i] + fib[i-1])
print(fib[n-1])

"""