# File: teach03_instructor.py
# Author: Group13 CSE110
# Purpose: Areas of shapes


# Area of a square
import math
side = float(input("What is the length of a side of the square? "))
area = side ** 2
print(f"The area of the square is: {area}")

# Area of a rectangle
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print(f"The area of the rectangle is: {area}")

# Area of a circle
radius = float(input("What is the radius of the circle? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area}")

# Stretch 1: Using the math library
radius = float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")

# Stretch 2: Many areas from one value
value = float(input("What is the value to be used? "))

# calculate areas
area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)

# display results
print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {volume_sphere}")

# Stretch 3: cm -> m conversion
# For this stretch challenge, the code above could simply be updated, but it is
# duplicated here so that the above code is not confusing when it is viewed.

# Area of a square
side = float(input("What is the length of a side of the square (in cm)? "))
area = side ** 2

print(f"The area of the square is: {area} cm^2")

# In the above example, the area was computed first and saved into a variable,
# but the code for computation can also be put right into the print statement
# if you would rather do that. In the next example, the computation is
# included right in the print statement.
# Also, please note that you do NOT put commas in numbers in code (use: 10000, not: 10,000)
print(f"The area of the square is: {area / 10000} m^2")

# Area of a rectangle
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

# Area of a circle
radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")
