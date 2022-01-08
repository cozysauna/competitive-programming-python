class comb():
    def __init__(self, N, MOD):
        self.N = N 
        self.MOD = MOD 
        self.F = [1, 1]
        self.FI = [1, 1]
        self.INV = [0, 1]
        for i in range(2, self.N+1):
            self.F.append((self.F[-1] * i) % MOD)
            self.INV.append((-self.INV[MOD % i] * (MOD // i)) % MOD)
            self.FI.append((self.FI[-1] * self.INV[-1]) % MOD)

    def get(self, n, r):
        if r < 0 or n < r: return 0
        r = min(r, n - r)
        return self.F[n] * self.FI[r] * self.FI[n-r] % self.MOD