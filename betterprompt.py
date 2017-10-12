# Definition of the prompt function

def prompt():
	value = int(input("Please enter an integer value:"))
	return value

print("This program adds together two integers.")
value1 = prompt()  # Call the function
value2 = prompt()  # Call the function again
sum = value1 + value2

print(value1, "+" , value2, "=", sum) 