from MyMath import Matrix

mA = Matrix(3,2,  \
        1,2,  \
        3,4,  \
        5,6)

mB = Matrix(3,2,  \
        2,1,  \
        5,0,  \
        7,9)

mC = Matrix(3,3,  \
        1,2,5,  \
        2,0,1,  \
        1,8,2)

m = (mA * ~mB) + mC
m.Show()

print("m[2][1] is",m[2][1])
print(m[2][1])
