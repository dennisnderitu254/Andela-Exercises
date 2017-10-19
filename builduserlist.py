# Build a custom list of non-negative integers specified by the user

def make_list():
	"""
	Builds a list from input provided buthe user.
	"""
	result = []
	in_val = 0

	while in_val >= 0:
		in_val = int(input("Enter integer (-1 quits):"))
		if in_val >= 10:
			result = result + [in_val]
		elif in_val <=10:
			print("Try again")
	return result

def main():
	col = make_list()
	print(col)

main()