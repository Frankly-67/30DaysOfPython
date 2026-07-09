#Exercise 3
"""
age = 24
height = 1.78
complex_number = 1 + 2j

#calculate the area of thes triangle
print("To calculate the area of a triangle, please")
print("Enter the base")
base = float(input())
print("Enter the height")
height = float(input())
print("The height is ", int(height), " and base is ", int(base))
print("The area of the triangle is ", 0.5 * base * height)

#Calculate the perimeter of this triangle
print("to calculate the perimeter of a triangle, please")
print("Enter the first side of the triangle")
side_1 = float(input())
print("Enter the second side of the triangle")
side_2 = float(input())
print("Enter the third side of the triangle")
side_3 =float(input())
print("The first side of the triangle is: ", side_1, "the second is: ", side_2, "and the third is:", side_3)
print("The perimeter of the triangle is", side_1+side_2+side_3)

#Area and perimeter of a rectangle
print("To calculate the area and the perimeter of a rectangle, please")
print("Enter the base")
base = float(input())
print("Enter the lenght")
lenght = float(input())
print("The base of the rectangle is: ", base, "and the lenght is: ", lenght)
print("The area of the rectangle is:", base*lenght, "and perimeter is: ", 2*(base+lenght))

#Area and circumference of a circle
print("To calculate the area and the circumference of a circle, please")
pi = float(3.14)
print("Enter the radius")
radius = float(input())
print("The radius of the circle is: ", radius)
print("The area of the circle is: ", pi*(radius**2), "and the circumference is:", 2*pi*radius)

#Slope calculation
m = 2
b = -2
interception_x = -b/m

print("The slope is: ", m)
print("The x-intercept is: (", interception_x,"0)")
print("The y-intercept is: (0,", b,")")
"""

#Slope and Euclidean distance
a = (2,2)
b = (6,10)
m = (b[1]-a[1])/(b[0]-a[0])
print(m)
