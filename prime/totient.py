#　O(√N)
#  You can find totient number with the order of √N
def totient(n):
    from collections import defaultdict
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
        ans *= k-1
        ans *= k**(v-1)

    return ans

# when you need totient(k)(1<=k<=n)
# if used the function above, it takes O(N * N * √N) ...
# totient_2 is to get totient num of k with O(N * loglogN)!!!
# O(N * loglogN)
def totient_2(n):
    from math import gcd   
    K = [0]*(n+1)
    P = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        if K[i]: continue
        for j in range(i, n+1, i): 
            P[j].append(i)
            K[j] += 1
    ret = []
    for i, E in enumerate(P):
        top, bot = i, 1
        for p in E:
            top *= p-1
            bot *= p
            d = gcd(top, bot)
            top //= d
            bot //= d
        ret.append(top//bot)
    return ret