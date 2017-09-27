# Area calculation program
# Also included the area of a triangle

print "=====WELCOME============="
print "Area Calculation Program"
print "========================="
print "1. Circle"
print "2. Rectangle"
print "3. Quit"
print

from math import pi
from time import sleep
from datetime import datetime

# now holds current date and time
now = datetime.now()  

print("Calculator is starting: ")

#print current date and time
print("Current time: %s/%s/%s %s:%s") % (now.month, now.day, now.year, now.hour, now.minute) 
sleep(1)
hint = "Don't forget to include the correct units! \nExiting"

#prompt user for shape
option = raw_input("Enter C for Circle or T for Triangle: ")
# force uppercase letter
option = option.upper()

#calculate area of shape
#determine shape
#area if option is C for circle
if option == 'C':  
    #get radius
    radius = float(raw_input("Enter the radius of the circle: "))
    #area is equal to 2 times radius times pi
    area = pi * radius**2
    print("The pie is baking...")
    sleep(1)
    print("Area: %.2f. \n%s" % (area, hint))
  
  
#area if option is T for Triangle  
elif option == 'T':
    #get base of triangle
    base = float(raw_input("Enter the base of the triangle: "))
    #get height of triangle
    height = float(raw_input("Enter the height of the triangle: "))
    #find area of triangle
    #area equals 1/2 of base times height
    area = 0.5 * base * height
    print("Uni Bi Tri...")
    sleep(1)
    print("Area: %.2f. \n%s" % (area, hint))
  
#option when user inputs garbage
#notify user that input is garbage, exit
else:
	print("Your input is invalid, exiting the program.")
