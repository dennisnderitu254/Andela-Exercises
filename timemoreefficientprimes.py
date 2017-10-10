from math import sqrt
from time import clock


max_value = 10000
count = 0
value = 2
# Smallest prime number
start = clock() # Start the stopwatch
while value <= max_value:
	# See if value is prime
	is_prime = True # Provisionally, value is prime
	# Try all possible factors from 2 to value - 1
	trial_factor = 2
	root = sqrt(value)
	while trial_factor <= root:
		if value % trial_factor == 0:
			is_prime = False;
			break
		trial_factor += 1
	if is_prime:
		count += 1
	value += 1
elapsed = clock() - start
print("Count:", count , " Elapsed time:", elapsed, "sec")