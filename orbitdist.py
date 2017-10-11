# computing the difference in the distances
# Use some functions and values from the math package
from math import sqrt, sin, cos, pi
# Location of orbiting point is (x,y)
# Location of fixed point is always (100, 0),
# AKA (p_x, p_y). Change these as necessary.
p_x = 100
p_y = 0
# Radians in 10 degrees
radians = 10 * pi/180
# Precompute the cosine and sine of 10 degrees
COS10 = cos(radians)
SIN10 = sin(radians)
# Get starting point from user
x, y = eval(input("Enter initial satellite coordinates (x,y):"))
# Compute the initial distance
d1 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y))
# Let the satellite orbit 10 degrees
x_old = x;
# Remember x's original value
x = x*COS10 - y*SIN10 # Compute new x value
# x's value has changed, but y's calculate depends on
# x's original value, so use x_old instead of x.
y = x_old*SIN10 + y*COS10
# Compute the new distance
d2 = sqrt((p_x - x)*(p_x - x) + (p_y - y)*(p_y - y))
# Print the difference in the distances
print("Difference in distances: %.3f" % (d2 - d1))