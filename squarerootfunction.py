# Computes the appriximate square root of val
# Val is a number

def square_root(val):
	# Compute a provisional sqaure root
	root = 1.0

	# How far off is our provisional root?
	diff = root*root - val 

	# Loop until the provisional root
	# is close enough to the actual

	while diff > 0.00000001 or diff < -0.00000001:
		root = (root + val/root) / 2
		# How bad is your current approximation?
		diff = root*root - val
	return root

def main():
	# Get value from the user
	num = float(input("Enter number: "))
	# Report square root
	print("Square root of", num, "=",square_root(num))

main()