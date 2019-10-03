from MyMath import Matrix

mA = Matrix(3,2,  \
        1,2,  \
        3,4,  \
        5,6)

mB = Matrix(2,2,  \
        1,2,  \
        3,4)

try:
    mC = mA.Multiply(mB)
    mA.Show()
    print("  X")
    mB.Show()
    print("  =")
    mC.Show()
except Exception as ex:
    print(ex)

