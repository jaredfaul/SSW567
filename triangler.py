import unittest
#  scalene, isosceles, or equilateral,
def classifyTriangle(a, b, c):
    x = "sides: (" + str(a) + ", " + str(b) +  ", " + str(c) +  ")\t "
    #check if its equilateral
    if a == b and b == c:
      x = x + "equilateral"
    #check if its isoscoles
    elif a == b or b == c:
      x = x + "isosceles"
    else:
      x = x + "scalene"

    if pow(a,2) + pow(b,2) == pow(c,2):
        x = x + "\t RIGHT"
    return x

class TrianglerTester(unittest.TestCase):

    def testRightSided(self):
        self.assertIn("RIGHT", classifyTriangle(3,4,5))
        self.assertIn("RIGHT", classifyTriangle(3,5,3))
        self.assertNotIn("RIGHT", classifyTriangle(3,5,5))

    def testIsosceles(self):
        self.assertIn("isosceles", classifyTriangle(3,5,5))
        self.assertNotIn("isosceles", classifyTriangle(3,4,5))

    def testEquilateral(self):
        self.assertIn("equilateral", classifyTriangle(55,55,55))
        self.assertNotIn("equilateral", classifyTriangle(45,55,55))

    def testScalene(self):
        self.assertIn("scalene", classifyTriangle(3,4,5))
        self.assertNotIn("scalene", classifyTriangle(4,4,5))

if __name__ == '__main__':
    unittest.main()
    sys.exit(0)

##print classifyTriangle(3,4,5)
##print classifyTriangle(3,5,4)
##print classifyTriangle(1.2,1.2,3)
##print classifyTriangle(55,55,55)
##print classifyTriangle(23,13,13)
##print classifyTriangle(23,23,13)
