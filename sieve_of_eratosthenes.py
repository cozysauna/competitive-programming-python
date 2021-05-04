# primes less than N
# primes(10) = 2, 3, 5, 7
 # O(NloglogN)

def primes(n): 
    P = []
    check = [1]*(n+1)
    check[1] = 0
    for p in range(2, n+1):
        if not check[p]: continue
        P.append(p)
        for i in range(p*p, n+1, p): check[i] = 0
    
    return P 