#from Ex03 import GCD
import Ex03

n = int(input("numerator="))
d = int(input("denominator="))

#gcd = GCD(n,d)
gcd = Ex03.GCD(n,d)
print('{}/{}=>{}/{}'.format(n, d, n//gcd, d//gcd))
