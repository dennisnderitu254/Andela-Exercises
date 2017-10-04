done = False

while not done:
	entry = eval(raw_input())
	if entry == 99:
		done = True
	else:
		print(entry)