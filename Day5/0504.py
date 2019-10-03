from MyMath import Matrix

mA = Matrix(3,2,  \
        1,2,  \
        3,4,  \
        5,6)

mB = Matrix(3,2,  \
        2,1,  \
        5,7,  \
        8,0)

mC = Matrix(3,3,  \
        1,5,0,  \
        2,3,1,  \
        4,1,2)

try:
    #((mA.Multiply(mB.Transpose())).Add(mC)).Show()
    ((mA.__mul__(mB.__invert__())).__add__(mC)).Show() #Function format
    print()
    ((mA * ~mB) + mC).Show()  #Operator overloading format
except Exception as ex:
    print(ex)
