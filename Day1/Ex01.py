def GCD(x,y):
    while(y!=0):
        x, y = y, x % y
    return x

print("GCD(60,96) is ",  GCD(60, 96))
print("GCD(48,120) is ", GCD(48,120))
print("GCD(7,11) is ",   GCD(7,  11))
print("GCD(11,7) is ",   GCD(11,  7))

def LCM(x,y):
    return (x * y) / GCD(x,y)


def Fibonacci(n):
    if type(n) is int:
        if n>1:
            x, y = 0, 1
            while(n>0):
                print(x,end='\t')
                x, y = y, x + y
                '''
                y = x + y
                x = y - x
                n -= 1
                '''
            print()
        else:
            print("n must be >1")
    else:
        print("n must be int type")
        
Fibonacci("Hello")
Fibonacci(1)
Fibonacci(10)


#SDADNASIUBUIABCUYASJBDASUBUBAS
