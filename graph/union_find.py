class UnionFind:
    def __init__(self, n):
        self.n = n
        self.P = [-1] * n # parents

    def find(self, x):
        if self.P[x] < 0: return x
        self.P[x] = self.find(self.P[x])
        return self.P[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.P[x] > self.P[y]: x, y = y, x
        self.P[x] += self.P[y]
        self.P[y] = x

    def size(self, x): return -self.P[self.find(x)]

    def same(self, x, y): return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self): return [i for i, x in enumerate(self.P) if x < 0]

    def group_count(self): return len(self.roots())

    def all_group_members(self):
        from collections import defaultdict
        G = defaultdict(list)
        for member in range(self.n): G[self.find(member)].append(member)
        return G

    def __str__(self): return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())