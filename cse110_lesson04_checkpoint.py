"""
File: teach04_sample.py
Author: Brother Burton

Purpose: Calculate the speed of a falling object using the formula:

v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))

"""
import math

# while you don't _have to_, it's considered good practice to import libraries
# at the top of your program, so that others know exactly which libraries
# you are using.

print("Welcome to the velocity calculator. Please enter the following:\n")

# Note: In this example, I chose to use single letter variable names, because they
# map directly to variables in the physics equation, so it seemed like it would
# actually be more clear in this case to use the single letter variables than to
# try to use the more descriptive names of "mass" or "gravity".

m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# First calculate c = 1/2 p A C
c = (1 / 2) * p * A * C

# Now calculate the velocity v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))

print()  # display a blank line
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")
