#Example improve code using List Comprehensions
def showMatrix(m):
    for r in range(len(m)):
        for c in range(len(m[0])): print(m[r][c],end='\t')
        print()

mA = [[1,2],\
      [3,4],\
      [5,6]]

NRowA = len(mA)
NColA = len(mA[0])
'''
m  = []
for r in range(NColA):
   m.append([])
   for c in range(NRowA): m[r].append(mA[c][r])
'''
m = [[row[c] for row in mA] for c in range(NColA)]

showMatrix(mA)
print("  ",u"\u2193")
showMatrix(m)
