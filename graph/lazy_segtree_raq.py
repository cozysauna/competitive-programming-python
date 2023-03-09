# Range Add Query (0-indexed)
class RAQ:
    def __init__(self, N, func, e):
        self.N = N
        self.func = func
        self.e = e
        self.height = (N - 1).bit_length()
        self.num = 1 << self.height
        self.data = [0] * (2 * self.num)
        self.lazy = [0] * (2 * self.num)

    def gindex(self, l, r):
        L = (l + self.num) >> 1
        R = (r + self.num) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range(self.height):
            if rc <= i: yield R
            if L < R and lc <= i: yield L
            L >>= 1
            R >>= 1

    def propagate(self, *ids):
        for i in ids[::-1]:
            v = self.lazy[i - 1]
            if not v: continue
            self.lazy[2 * i - 1] += v 
            self.data[2 * i - 1] += v 
            self.lazy[2 * i] += v
            self.data[2 * i] += v
            self.lazy[i - 1] = 0

    # A[i] += x [l, r)
    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagate(*ids)

        L = self.num + l
        R = self.num + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] += x 
                self.data[R - 1] += x

            if L & 1:
                self.lazy[L - 1] += x 
                self.data[L - 1] += x
                L += 1

            L >>= 1
            R >>= 1

        for i in ids:
            self.data[i - 1] = self.func(self.data[2 * i - 1], self.data[2 * i])

    def query(self, l, r):
        self.propagate(*self.gindex(l, r))

        L = self.num + l
        R = self.num + r
        ret = self.e
        while L < R:
            if R & 1:
                R -= 1
                ret = self.func(ret, self.data[R - 1])

            if L & 1:
                ret = self.func(ret, self.data[L - 1])
                L += 1

            L >>= 1
            R >>= 1

        return ret

    def get(self, x): return self.query(x, x + 1)
    
    def print(self):
        print("[index]", " ".join(map(str, [i for i in range(1, self.N + 1)])))
        print("[value]", " ".join(map(str, [self.get(i) for i in range(1, self.N + 1)])))
