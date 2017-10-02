value = eval(input("Please enter an integer value in the range 0...10:"))
if value >= 0:
	if value <= 10:
		print(value, "Is in range")
	else:
		print(value, "is too small")
else:
	print(value, "Is too small")
print("Done")