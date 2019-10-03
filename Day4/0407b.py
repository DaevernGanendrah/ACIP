with open('primes.txt') as f:
    primes = f.read()
    for prime in primes.split('\n'):
        print(prime)
f.close()
