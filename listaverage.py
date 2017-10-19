def main():
	# Set up variables

	sum = 0.0
	NUMBER_OF_ENTRIES = 5
	numbers = []


	# Get input from user
	print("Please enter", NUMBER_OF_ENTRIES, "numbers: ")

	for i in range(0, NUMBER_OF_ENTRIES):
		num = eval(input("Enter number " + str(i) + ": "))
		numbers += [num]
		sum += num;

	# Print the numbers entered
	print(end="Numbers entered: ")
	for num in numbers:
		print(num, end=" ")
	print() # Print New line

	# Print average

	print("Average :", sum/NUMBER_OF_ENTRIES)

main()