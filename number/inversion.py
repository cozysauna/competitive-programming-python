class Inv():
    def __init__(self, N, A):
        self.size = N
        self.tree = [0] * (N + 1)
        self.A = A 
        if 0 in A: raise('make the array in 1-indexd')
 
    # A[i] += x
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # A[i] = x 
    def update(self, i, x):
        old = self.get(i)
        self.add(i, x - old)

    # A[1] + A[2] + ... + A[i]
    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    # A[i]
    def get(self, i): return self.sum(i) - self.sum(i - 1)

    def find(self):
        cnt = 0
        for i, a in enumerate(self.A):
            self.add(a, 1)
            cnt += i + 1 - self.sum(a)
        return cnt