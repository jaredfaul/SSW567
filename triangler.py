import unittest
#  scalene, isosceles, or equilateral,
def classifyTriangle(a, b, c):
    x = "Triangle sides: " + str(a) + ", " + str(b) +  ", " + str(c) +  " "
    #check if its equilateral
    if a == b and b == c:
      x = x + "equilateral"
    #check if its isoscoles
    elif a == b or b == c:
      x = x + "isosceles triangle"
    else:
      x = x + "scalene"

    if pow(a,2) + pow(b,2) == pow(c,2):
        x = x + " ** RIGHT **"
    return x

print classifyTriangle(3,4,5)
print classifyTriangle(3,5,4)
print classifyTriangle(1.2,1.2,3)
print classifyTriangle(55,55,55)
print classifyTriangle(23,13,13)
print classifyTriangle(23,23,13)
