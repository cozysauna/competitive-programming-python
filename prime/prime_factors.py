# 60 = 2 * 2 * 3 * 5 
# number of prime factors: K[60] = 3
# kinds of prime factors: P[60] = 2, 3, 5  
# O(NloglogN)
def prime_factors(n):
    K = [0]*(n+1)
    P = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        if K[i]: continue
        for j in range(i, n+1, i): 
            P[j].append(i)
            K[j] += 1

    return K[n] 