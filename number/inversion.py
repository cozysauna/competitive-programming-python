class Inv:
    def __init__(self, N, A):
        self.size = N
        self.tree = [0] * (N + 1)
        if 0 in A: 
            for i in range(N): A[i] += 1
        self.A = A

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def get(self):
        cnt = 0
        for i, a in enumerate(self.A):
            self.add(a, 1)
            cnt += i + 1 - self.sum(a)
        return cnt
