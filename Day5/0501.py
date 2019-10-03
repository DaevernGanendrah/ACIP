import math

class Circle:
    def __init__(self,radius):
        self.Radius = radius
    def __getattr__(self, attr):
        if (attr=='Radius'):
            return self._radius
        elif (attr=='Area'):
            return math.pi * self._radius ** 2
        elif (attr=='Circumference'):
            return 2*math.pi * self._radius
        #else: #This else section is only needed if we use __getattribute__ instead of __getattr__
        #    return super.__getattribute__(attr)
    def __setattr__(self, attr, value):
        if (attr=='Radius'):
            if not isinstance(value,(int,float)):
                raise Exception('Invalid value type for Radius')
            if (value<0):
                raise Exception('Radius cannot be negative!')
            self._radius = float(value)
        elif (attr in ('Area','Circumference')):
            raise Exception("Attribute {} is read-only!".format(attr))
        else:
            super.__setattr__(self,attr, value)

c = Circle(100)
c.Radius = 200
#c.Area = 1000
print("Radius:{:.4f}".format(c.Radius))
print("Area:{:.4f}".format(c.Area))
print("Circumference:{:.4f}".format(c.Circumference))
c.OtherAttr = "ABC"
print(c.OtherAttr)


