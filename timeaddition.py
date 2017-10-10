from time import clock

sum  = 0  #initialize sum accumulator
start = clock() #start the stopwatch

for n in range(1, 100000001):
	sum += n

elapsed = clock() - start # Stop the stopwatch
print("sum: ", sum, "time:", elapsed) # Report results