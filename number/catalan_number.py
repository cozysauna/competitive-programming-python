def catalan_number(N, MOD):
    F = [1, 1]
    FI = [1, 1]
    INV = [0, 1]
    for i in range(2, 2 * N + 1):
        F.append((F[-1] * i) % MOD)
        INV.append((-INV[MOD % i] * (MOD // i)) % MOD)
        FI.append((FI[-1] * INV[-1]) % MOD)
    return F[2 * N] * FI[N] ** 2 * INV[N + 1] % MOD
