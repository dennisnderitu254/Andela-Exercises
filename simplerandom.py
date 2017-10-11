from random import randrange, seed

seed(23)   # Set random number seed
for i in range(0, 100): #Print 100 random numbers
	print(randrange(1, 1000), end=' ') # Range 1.....1000

print()  # Print newline
