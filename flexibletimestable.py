# Print a MAX x MAX multiplication table
MAX = 18

# First, Print heading
print(end="     ")
#print column heading numbers

for column in range(1, MAX+1):
	print(end=" %2i "% column)
print() # Go down to the next Line

# Print line separator; a portion for each column
print(end="  +")

for column in range(1, MAX+1):
	print(end="----") #Print portion of line
print()

#Print table contents

for row in range(1, MAX+1):
	print(end="%2i | "% row)
	for column in range(1, MAX+1):
		product = row*column;
		print(end="%3i "% product)
	print()