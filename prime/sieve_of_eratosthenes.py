# primes less than N
# sieve(10) = 2, 3, 5, 7
# O(NloglogN)

def sieve(N): 
    P = []
    check = [1] * (N + 1)
    check[1] = 0
    for p in range(2, N + 1):
        if not check[p]: continue
        P.append(p)
        for i in range(p * p, N + 1, p): check[i] = 0
    
    return P 