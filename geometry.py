from math import pi as PI
from math import sqrt, sin, asin, acos, degrees, radians

class Circle:
    ''' Generates attributes of a circle based on its radius '''

    def __init__(self, radius):
        self.r = radius
        self.d = radius*2 # diamater of the circle
        self.area = PI*radius**2
        self.circumf = 2*PI*radius # circumference

    def printAttributes(self):
        print('''\
        Radius: {}
        Diameter: {}
        Area: {}
        Circumference: {}'''.format(self.r, self.d, self.area, self.circumf))

class rTriangle:
    ''' Generates attributes of a right triangle based on the length of side a and b '''

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = sqrt(a**2 + b**2) # length of the hypothenuse 
        self.p = a + b + self.c # perimeter
        self.area = (a * b)/2 
        self.bAngle = degrees(asin(b/self.c)) # angle between a and hyp
        self.aAngle = degrees(asin(a/self.c)) # angle between b and hyp

    def printAttributes(self):
        print('''\
        Sides:
            a: {}
            b: {}
            c: {}
        Perimeter: {}
        Area: {}
        A Angle: {}°
        B Angle: {}°'''
        .format(self.a, self.b, self.c, self.p, self.area, self.aAngle, self.bAngle))

class sssTriangle:
    ''' Generates attributes of a triangle with its three sides provided '''

    def __init__(self, s1, s2, s3):

        if (s1+s2>s3 and s2+s3>s1 and s1+s2>s3) : # if true, side do make a triangle
            # Side lengths, 'a' = side with the obtuse angle, 'c' = smallest angle
            self.a = sorted([s1,s2,s3])[2] 
            self.b = sorted([s1,s2,s3])[1]
            self.c = sorted([s1,s2,s3])[0]
        else:
            print("The length of the sides cannot make a triangle")
            return None

        self.p = self.a + self.b + self.c # perimeter
        self.sp = self.p/2 # semi-perimeter
        # get area using heron's formula
        self.area = sqrt(self.sp*(self.sp-self.a)*(self.sp-self.b)*(self.sp-self.c))

        # get largest (internal) angle first using law of cosines
        self.aAngle = degrees(acos((self.b**2 + self.c**2 - self.a**2) / (2*self.b*self.c)))
        # get angle of second largest side using law of cosines
        self.bAngle = degrees(acos((self.a**2 + self.c**2 - self.b**2) / (2*self.a*self.c)))
        #self.cAngle = 180 - self.aAngle - self.bAngle
        self.cAngle = 180 - self.aAngle - self.bAngle

    def printAttributes(self):
        print('''\
        Sides:
            a: {}
            b: {}
            c: {}
        Perimeter: {}
        Area: {}
        A Angle: {}°
        B Angle: {}°
        C Angle: {}°'''.format(self.a, self.b, self.c, self.p, self.area, 
                        self.aAngle, self.bAngle, self.cAngle))

def main():
    t = sssTriangle(11.6,7.4,15.2)
    t.printAttributes()

if __name__ == "__main__":
    main()