# 60 = 2 * 2 * 3 * 5 
# number of prime factors: K[60] = 3
# kinds of prime factors: P[60] = 2, 3, 5  

def prime_factors(N):
    K = [0] * (N + 1)
    P = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        if K[i]: continue
        for j in range(i, N + 1, i): 
            P[j].append(i)
            K[j] += 1

    return K[N] 