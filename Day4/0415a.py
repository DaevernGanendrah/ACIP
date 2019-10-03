import math

r = float(input("Radius?>>"))

if r<0.0: raise Exception ("Invalid radius!")

print("Radius:{0:.2f}".format(r))
print("Circumference:{0:.2f}".format(2* math.pi*r))
print("Area:{0:.2f}".format(math.pi*r*r))