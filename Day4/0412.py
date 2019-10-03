#Exception Handling #1

def GCD(x:int,y:int)->int:
    if not isinstance(x, int):
        raise Exception('Argument x is not integer type')
    if not isinstance(y, int):
        raise Exception('Argument y is not integer type')

    while y!=0:
      x, y = y, x % y
    return x

def getInput(prompt)->int:
    while True: #Busy loop
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Opps. Invalid int value")

        print("Try Again...")


n = getInput("numerator: ")
d = getInput("denominator: ")

gcd = GCD(n,d)

print("{}/{}->{}/{}".format(n,d,n//gcd,d//gcd))


