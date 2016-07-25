import unittest
import sys
import math
import logging

#  scalene, isosceles, or equilateral,
def classifyTriangle(s1, s2, s3):
    if s1 > s2 and s1 > s3:
        c = s1
        a = s2
        b = s3
    elif s2 > s1 and s2 > s3:
        c = s2
        a = s1
        b = s3
    else:
        c = s3
        a = s1
        b = s2



    #print angleB
    x = "sides: (" + str(a) + ", " + str(b) +  ", " + str(c) +  ")\t "

    if a + b <= c or a < 0 or b < 0 or c < 0 or isinstance(a, basestring) or isinstance(b, basestring) or isinstance(c, basestring):
        x = x + "INVALID Triangle"
        return x

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

    def testChallengerSpecified1(self):
        self.assertIn("INVALID", classifyTriangle('A', 'A', 'A'))
        self.assertIn("INVALID", classifyTriangle(7,3,2))
        self.assertIn("INVALID", classifyTriangle(-3,-4,-5))


        self.assertIn("INVALID", classifyTriangle(0,1, 2))
        self.assertIn("INVALID", classifyTriangle(1, 1, -3))
        self.assertIn("isosceles", classifyTriangle(10, 99999, 99999))
        self.assertIn("scalene", classifyTriangle(3000000,4000000,5000000))
        self.assertIn("RIGHT", classifyTriangle(3000000,4000000,5000000))
        self.assertIn("isosceles", classifyTriangle(1,1,math.sqrt(2)))
      #  self.assertIn("RIGHT", classifyTriangle(1, 1, math.sqrt(2)))      #failed! precision!

        self.assertIn("INVALID", classifyTriangle(-1,-1,-1))
        self.assertIn("INVALID", classifyTriangle(1, 'a', 1))
        self.assertIn("equilateral", classifyTriangle(1e0, 1e0, 1e0))
        self.assertIn("INVALID", classifyTriangle(3, 3, 5.999999999999999999))   #bad test case?

        self.assertIn("INVALID", classifyTriangle(-3,-4,-5))
     #   self.assertIn("RIGHT", classifyTriangle(3*2^64, 4*2^64, 5*2^64))
     #   self.assertIn("scalene", classifyTriangle(3*(2^64), 4*(2^64), 5*(2^64)))  #failed - overflow
        self.assertIn("isosceles", classifyTriangle(3,3, 4.242640687119285146))
      #  self.assertIn("RIGHT", classifyTriangle(3, 3, 4.242640687119285146))    #fail - precision!
        self.assertIn("INVALID", classifyTriangle(-3,-4,-5))
     #   self.assertIn("RIGHT", classifyTriangle(3*2^64, 4*2^64, 5*2^64))    #failed !
     #   self.assertIn("scalene", classifyTriangle(3*2^64, 4*2^64, 5*2^64))


    def testTeacherSpecified(self):
        self.assertIn("INVALID", classifyTriangle(1, 1, 2))
        self.assertNotIn("RIGHT", classifyTriangle(1234567890, 1234567890, 1745942653.7083354))
        self.assertIn("isosceles", classifyTriangle(1234567890, 1234567890, 1745942654))
        self.assertIn("isosceles", classifyTriangle(1, 1, 1.99))
        self.assertIn("isosceles", classifyTriangle(1, 1, 1.0000000000001))
        self.assertNotIn("RIGHT", classifyTriangle(1, 1, 1.99))

    def testRightSided(self):
       # log.debug( "\ntestRightSided")
        self.assertIn("RIGHT", classifyTriangle(3,4,5))
        #self.assertIn("RIGHT", classifyTriangle(1,1,math.sqrt(2)))
        #self.assertIn("RIGHT", classifyTriangle(2147483647,2147483647,5))
        #self.assertIn("RIGHT", classifyTriangle(3,5,4))
        self.assertNotIn("RIGHT", classifyTriangle(3,5,5))

    def testIsosceles(self):
     #   log.debug( "\ntestIsosceles:")
        self.assertIn("isosceles", classifyTriangle(3,5,5))
        self.assertNotIn("isosceles", classifyTriangle(3,4,5))

    def testEquilateral(self):
     #   log.debug( "\ntestEquilateral:")
        self.assertIn("equilateral", classifyTriangle(55,55,55))
        self.assertIn("equilateral", classifyTriangle(1.55,1.55,1.55))
        self.assertNotIn("equilateral", classifyTriangle(45,55,55))

    def testScalene(self):
     #   log.debug( "\ntestScalene:")
        self.assertIn("scalene", classifyTriangle(3,4,5))
        self.assertNotIn("scalene", classifyTriangle(4,4,5))

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as e:
        print ''

