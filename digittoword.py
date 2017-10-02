value = eval(input("Please enter an integer in the range 0...5: "))
if value < 0:
	print("Too small")
else:
	if value == 0:
		print("Zero")
	else:
		if value == 1:
			print("One")
		else:
			if value == 2:
				print("Two")
			else:
				if value == 3:
					print("Three")
				else:
					if value == 4:
						print("Four")
					else:
						if value == 5:
							print("Five")
						else:
							print("Too large")

print("Done")