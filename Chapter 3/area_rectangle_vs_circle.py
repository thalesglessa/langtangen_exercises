from math import pi

r = 10.6
Sc = pi * r**2 #Area of the circle

a = 1.3
b = 0

while a*b < Sc:
    b += 1
b -= 1

print(b)
