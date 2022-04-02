func = min
e = 1 << 30

class LazySegTree: #RMQ
    # 0-indexed
    def __init__(self, N, func, e):
        self.LV = (N-1).bit_length()
        self.CNT = 2**self.LV
        self.arr = [0]*(2*self.CNT)
        self.lazy = [None]*(2*self.CNT)
        self.func = func
        self.e = e
        self.N = N 

    def gindex(self, l, r):
        L = (l + self.CNT) >> 1; R = (r + self.CNT) >> 1
        lc = 0 if l % 2 else (L & -L).bit_length()
        rc = 0 if r % 2 else (R & -R).bit_length()
        for i in range(self.LV):
            if rc <= i: yield R
            if L < R and lc <= i: yield L
            L >>= 1; R >>= 1

    def propagates(self, *ids):
        for i in ids[::-1]:
            v = self.lazy[i-1]
            if v == None: continue
            self.lazy[2*i-1] = self.arr[2*i-1] = self.lazy[2*i] = self.arr[2*i] = v
            self.lazy[i-1] = None

    # A[i] = x (l <= i < r)
    def update(self, l, r, x):
        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L = self.CNT + l; R = self.CNT + r
        while L < R:
            if R % 2:
                R -= 1
                self.lazy[R-1] = self.arr[R-1] = x
            if L % 2:
                self.lazy[L-1] = self.arr[L-1] = x
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.arr[i-1] = self.func(self.arr[2*i-1], self.arr[2*i])

    def query(self, l, r):
        self.propagates(*self.gindex(l, r))
        L = self.CNT + l; R = self.CNT + r
        s = self.e
        while L < R:
            if R % 2:
                R -= 1
                s = self.func(s, self.arr[R-1])
            if L % 2:
                s = self.func(s, self.arr[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    def get(self, x): return self.query(x, x + 1)

    def display_all(self): print(*[self.get(i) for i in range(self.N)])