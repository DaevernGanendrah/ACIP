def showMatrix(m):
    for r in range(len(m)):
        for c in range(len(m[0])): print(m[r][c],end='\t')
        print()

mA = [[1,2],\
      [3,4],\
      [5,6]]

mB = [[1,2],\
      [3,4]]

NRowA = len(mA)
NColA = len(mA[0])
NRowB = len(mB)
NColB = len(mB[0])

if NColA==NRowB:
    mC  = []
    for r in range(NRowA):
        mC.append([])
        for c in range(NColB):
            mC[r].append(0)
            for i in range(NRowB):
                mC[r][c] += mA[r][i] * mB[i][c]
    showMatrix(mA)
    print("  X")
    showMatrix(mB)
    print("  =")
    showMatrix(mC)
else:
    print("Cannot Multiply!")
