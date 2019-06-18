import math
'''
Import the math module which allows us
to use tangent and the number pi

The function takes two integers or floats
n and s, n which is the number of sides the
polygon has, and s which is the length of each side.

Then, it returns the sum of the area and
the perimeter squared. 
'''
def polysum(n, s):
    a = (0.25*n*(s**2))/(math.tan(math.pi/n))
    p = n*s
    return round(a + p**2, 4)
