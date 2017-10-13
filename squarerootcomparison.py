from math import fabs, sqrt

"""
Consider two floating-point numbers equal when
the difference between them is very small.
equals(a, b, tolerance)
Returns true if a = b or |a - b| < tolerance.
If a and b differ by only a small amount
(specified by tolerance), a and b are considered
"equal." Useful to account for floating-point
round-off error.
The == operator is checked first since some special
floating-point values such as floating-point infinity
require an exact equality check.
"""

def equals(a,b, tolerance):
	return a == b or fabs(a - b) < tolerance;

# Computes the approximate square root of val
# val is a number

def square_root(val):
	# Compute a provisional square root
	root = 1.0;

	# How far off is our provisional root?
	diff = root*root - val

	# Loop until the provisional root
	# is close enough to the actual root

	while diff > 0.00000001 or diff < -0.00000001:
		root = (root + val/root) / 2		# Compute new provisional root
		# How bad is our current approximation?
		diff = root*root - val
	return root

def main():
	d = 0.0
	while d < 100000.0:
		if not equals(square_root(d), sqrt(d), 0.001):
			print(d, ":Expected", sqrt(d), "but computed", square_root(d))
		d += 0.0001 # Consider next value

main()

