import math

class Circle():
    def getArea(self):
        return math.pi*self.r*self.r
    def getCircumference(self):
        return 2*math.pi*self.r

r = float((input("Radius?>>"))
if r<0.0: raise Exception ("Invalid radius!")

c = Circle()
c.r = r


print("Radius:{0:.2f}".format(c.r))
print("Circumference:{0:.2f}".format(c.getCircumference()))
print("Area:{0:.2f}".format(c.getArea()))