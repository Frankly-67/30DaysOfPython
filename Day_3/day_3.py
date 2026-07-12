#Exercise 3
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
m1 = 2
b = -2
interception_x = -b/m1

print("The slope is: ", m1)
print("The x-intercept is: (", interception_x,"0)")
print("The y-intercept is: (0,", b,")")


#Slope and Euclidean distance
a = (2,2)
b = (6,10)
m2 = (b[1]-a[1])/(b[0]-a[0])
distance_euclidean = ((b[1]-a[1])**2+(b[0]-a[0])**2)**0.5
print("The slope is:", m2)
print("The euclidean distance is:", distance_euclidean)

#Compare Slope
print("Are the slopes m1 and m2 equal?:", m1 == m2)

#Find the value of y
x = -3
y = x**2 + 6*x + 9
print("The value of y is:", y)
print("and the value where y equals 0 is: -3" )

#lenght of a python and dragon
print(len("Python") != len("Dragon"))

#check if it´s on
print("Is \"on\" in Python and in Dragon?:", "on" in "python" and "on" in "Dragon")

#I hope this course is not full of jargon
print("is jargon in the sentence \" I hope this course is not full of jargon\"?", "jargon" in "I hope this courseis not full of jargon")

#No "on" in both dragon and python
print("on" not in "Python" and "Dragon")

#Lenght Python
print(str(float(len("python"))))

#check if it is 0
print("Enter a number to check if it is even.")
number = int(input())
even = number % 2
print("The number", number, "is even:", even == 0)

#check if the floor division
print(7//3 == int(2.7))

#Type 10
print(type("10") == type(10))

#Check 9.8 equal 10
print(int(float(("9.8"))) == 10)

#Script hours
print(" Enter hours")
hour = float(input())
print("Enter rate per hour")
rate = float(input())
print("Your weekly earning is:", hour*rate)

#Script year
print("Enter number of years you have lived:")
year = float(input())
print("You have lived for", year*365*24*60*60, "seconds")

#table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")