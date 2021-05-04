def nCr(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

M = 10 ** 9 + 7
fact = [1, 1]  # fact[n] = (n! mod M)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod M)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % M)
    inv.append((-inv[M % i] * (M // i)) % M)
    factinv.append((factinv[-1] * inv[-1]) % M)

