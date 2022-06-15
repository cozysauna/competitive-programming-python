from collections import defaultdict

def totient(n):
    p = defaultdict(int)
    while n % 2 == 0:
        p[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            p[f] += 1
            n //= f
        else: f += 2
    if n != 1: p[n] += 1
    ans = 1
    for k, v in p.items():
        ans *= k - 1
        ans *= k ** (v - 1)

    return ans

def totient_sieve(N): 
    K = [0] * (N + 1)
    P = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        if K[i]: continue
        for j in range(i, N + 1, i): 
            P[j].append(i)
            K[j] = 1

    sieve = []
    for i, E in enumerate(P):
        ans = i
        for p in E:
            ans //= p
            ans *= p - 1
        sieve.append(ans)
    return sieve
