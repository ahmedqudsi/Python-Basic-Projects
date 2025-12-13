# Basic math functions to be used 
# area and perimeter of circle

import math
# rad = float(input("Enter radius:"))
# A = math.pi * pow(rad,2)
# P = 2 * math.pi * rad 
# print(f"Area of circle is: {round(A,2)}cm²")
# print(f"Perimeter of circle is: {round(P,2)}cm")

# calculate hypotenus of right angle triangle
# c = sqrt(a² + b²)

a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c=math.sqrt(pow(a,2) + pow(b,2))
print(f"Hypotenus of right angle triangle is: {round(c,2)}cm")