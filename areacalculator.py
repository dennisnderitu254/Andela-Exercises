

shape = raw_input('Enter a shape:')

if shape == C:
	radius = raw_input('Enter radius:')
	area = radius*radius*3.142
	print "area"
elif shape == (rectangle or R or RECTANGLE or Rectangle):
	length = raw_input('Enter length:')
	width = raw_input('Enter width:')
	area_r = length*width
	print 'area_r'
else:
	print 'empty'
