def isPrime(v:int)->bool:
    if v<0: v = -v
    if (v<2): return False
    for i in range (2,v):
        if (v%i)==0: return False
    return True

for i in range(1000):
    if isPrime(i): print(i)

f = open('primes.txt','w')
for i in range(1000):
    if isPrime(i):f.write(str(i)+'\n')
f.close()    