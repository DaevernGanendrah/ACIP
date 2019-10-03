#Debugging Example #1

def GCD(x,y)->int:
    """
    This function implements the Euclain's Algorithm
    :param x: integer value > 0
    :param y: integer value > 0
    :return: The Greatest Common Divisor of x,y
    """
    while y!=0:
        # x, y = y, x % y
        oldX = x
        x = y
        y = y % oldX
    return x

n, d = 60, 96   #expected resuklt is 12
print('GCD({},{}) is {}'.format(n,d,GCD(n,d)))
'''
n, d = 48, 120  #expected resuklt is 24
print('GCD({},{}) is {}'.format(n,d,GCD(n,d)))

n, d = 7, 11 #expected resuklt is 1
print('GCD({},{}) is {}'.format(n,d,GCD(n,d)))

n, d = 11, 7 #expected resuklt is 1
print('GCD({},{}) is {}'.format(n,d,GCD(n,d)))
'''

print(GCD.__doc__)

