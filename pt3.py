import math
#Task 3: Import module utils
import utils

#Task 1: Declare a function calculating the factorial (n! = n) of a given int value
def calcFactorial(num):
    return(math.factorial(num))

x = 5
value = calcFactorial(x)
print("The Factorial of ", x ,  " is: " , value)

#Task 2-3: Calculate Circle Area & triangle
circle_radius = 5
circle_area = utils.calcCircleArea(circle_radius)
print("The area of a circle with the radius of", circle_radius, "is: ", circle_area)

tri_base = 4
tri_height = 3
triangle_area = utils.calcTriangleArea(tri_base, tri_height)
print("The are of a triangle with the base of " , tri_base, " and height of", tri_height, "is: ", triangle_area)

