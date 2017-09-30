""" program that approximates the value of pie by summing the terms of the series:
  program should  prompt user for n,the number of therms to sum, and gitve tn n terms of the series

  """
from math import pi

numerator=4
denomenator=1

while True:
	try:
		n=int(input("Enter the number of terms for estimation:"))
		break
	except:
		print("Enter a valid number")



approx = 4/1

for i in range(n-1):
	denomenator+=2

	if (i)%2==0:
		approx=approx-(numerator/denomenator)
	else:
		approx=approx+(numerator/denomenator)

print (" Your value is " + str(approx) + " and is off the mark by " + str(pi-approx))



