# P[i]:= i has P[i] kinds of prime_factors
 # P[60] = 3 (2, 3, 5)  
# O(NloglogN)

def prime_factors(n):
    P = [0]*(n+1)
    for i in range(2, n+1):
        if P[i] != 0: continue
        for j in range(i, n+1, i): P[j] += 1

    return P[n] # or return P