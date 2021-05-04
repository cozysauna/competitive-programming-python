def prime_fac(n):
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
    return p

print(prime_fac(10))

import collections
def prime_fac2(n):
    p = []
    while n % 2 == 0:
        p.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            p.append(f)
            n //= f
        else: f += 2
    if n != 1: p.append(n)
    return p

c = collections.Counter(prime_fac2(24))
s = c.values()
k = c.keys()