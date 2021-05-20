MOD = 10**9+7
F, FI,INV = [1, 1], [1, 1], [0, 1]  
n = 10**6
for i in range(2, n + 1):
    F.append((F[-1] * i) % MOD)
    INV.append((-INV[MOD % i] * (MOD // i)) % MOD)
    FI.append((FI[-1] * INV[-1]) % MOD)

def nCr(n, r, MOD):
    if r < 0 or n < r: return 0
    r = min(r, n - r)
    return F[n] * FI[r] * FI[n-r] % MOD