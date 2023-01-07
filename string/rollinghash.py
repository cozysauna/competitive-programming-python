class RollingHash:
    def __init__(self, string, base = 1237, mod = 10 ** 9 + 7):
        N = len(string)
        self.base = base
        self.mod = mod 
        self.hash = [0] * (N + 1)
        self.p = [1] * (N + 1)
        for i, c in enumerate(string):
            num = ord(c) - ord('a') + 1 
            self.hash[i + 1] = (self.hash[i] * self.base + num) % self.mod 
            self.p[i + 1] = self.p[i] * base % self.mod

        
    def get_hash(self, l, r): #[l, r)
        return (self.hash[r] - self.hash[l] * self.p[r - l]) % self.mod