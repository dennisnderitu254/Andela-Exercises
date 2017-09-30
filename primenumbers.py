# write a program that prompts input for n prime numbers

n = int(input("Enter the number:"))

def primenumber(n):
	print 1
	for i in range(2,n):
		numberprime=True

		for j in range(2,i):
			if(i%j==0):
				numberprime=False
				break
		if numberprime:
			print(i)

primenumber(n)
