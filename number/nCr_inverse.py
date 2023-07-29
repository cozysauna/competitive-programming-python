F = [1, 1]
FI = [1, 1]
INV = [0, 1]
for i in range(2, N + 1):
    F.append((F[-1] * i) % MOD)
    INV.append((-INV[MOD % i] * (MOD // i)) % MOD)
    FI.append((FI[-1] * INV[-1]) % MOD)

def nCr(n, r):
    if r < 0 or n < r: return 0
    r = min(r, n - r)
    return F[n] * FI[r] * FI[n - r] % MOD