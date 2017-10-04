print("Help! My computer doesn't work!")
done = False

while not done:
	print("Does the computer make any sounds(fans, etc.)")
	choice = input("or show any lights? (y/n):")
	# This is the trouble shooting control logic

	if choice == 'n':
		choice = raw_input("Is it plugged in?(y/n)")
		if choice == 'n':
			print("Plug it in.")
		else:
			choice = raw_input("Is the switch in the \"on\" position? (y/n):")
			if choice == 'n':
				print ("Turn it on.")
			else:
				choice = raw_input("Does the computer have a fuse?(y/n):")
				if choice == 'n':
					choice = input("Is the outlet OK?(y/n):")
					if choice == 'n':
						print("Check the outlet's circuit")
						print("breaker or fuse. Move to a")
						print("new outlet, if neccesary.")
					else:
						print("Please consult a servive technician.")
						done = True
				else:
					print("Check the fuse.Replace if")
					print("necessary.")

	else:
		print("Please consult a service technician.")
		done = True 