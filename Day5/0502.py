mA = [[1,2],
      [3,4],
      [5,6]]

mB = [[1,2],
      [3,4]]

def showMatrix(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            print("{}".format(m[r][c]),end="\t")
        print()

if (len(mA[0])==len(mB)):
    mC = [[0 for c in range(len(mB[0]))] for r in range(len(mA))]

    for r in range(len(mC)):
        for c in range(len(mC[0])):
            for i in range(len(mB)):
                mC[r][c] += mA[r][i] * mB[i][c]

    showMatrix(mA)
    print("  X")
    showMatrix(mB)
    print("  =")
    showMatrix(mC)
else:
    print("Cannot multiply-lah!")

