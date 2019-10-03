#Example improve code using List Comprehensions
def showMatrix(m):
    for r in range(len(m)):
        for c in range(len(m[0])): print(m[r][c],end='\t')
        print()

mA = [[1,2],\
      [3,4],\
      [5,6]]

mB = [[2,2],\
      [3,3],\
      [4,4]]

NRowA = len(mA)
NColA = len(mA[0])
NRowB = len(mB)
NColB = len(mB[0])

if (NRowA==NRowB) and (NColA==NColB):
    '''
    mC  = []
    for r in range(NRowA):
        mC.append([])
        for c in range(NColA):
            mC[r].append(mA[r][c] + mB[r][c])
    '''
    mC = [[mA[r][c]+mB[r][c] for c in range(NColA)] for r in range(NRowA)]
    showMatrix(mA)
    print("  +")
    showMatrix(mB)
    print("  =")
    showMatrix(mC)
else:
    print("Cannot Add-lah!")
