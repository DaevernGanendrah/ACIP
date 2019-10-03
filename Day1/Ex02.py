def GCD(x:int, y:int)->int:
    """
    This function implements the Euclean's Algorithm
    :param x: integer value > 0
    :param y: integer value > 0
    :return: The Greatest Common Divisor of x,y
    """
    while(y!=0):
        x,y = y,x % y
        '''   
        oldX = x
        x = y
        y = oldX % y
        '''
    return x

def Fibonacci(n:int)->None:
    if type(n) is int:
        if n>1:
            x, y = 0, 1
            while(n>0):
                print(x,end='\t')
                x, y = y, x % y
                '''   
                y = y + x
                x = y - x = x
                '''
                n -= 1
            print()
        else:
            print("n must be >1")
    else:
        print("n must be int type")

n, d = 60, 96   #expected result is 12
print('GCD({},{}) is {}'.format(n, d, GCD(n, d)))

n, d = 48, 120  #expected result is 24
print('GCD({},{}) is {}'.format(n, d, GCD(n, d)))

n, d = 7, 11 #expected result is 1
print('GCD({},{}) is {}'.format(n, d, GCD(n, d)))

n, d = 11, 7 #expected result is 1
print('GCD({},{}) is {}'.format(n, d, GCD(n, d)))

print(GCD.__doc__)

#sdadasda
