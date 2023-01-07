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

    def group_cnt(self): return len(self.roots())

    def group_and_members(self):
        group_info = dict()
        for member in range(self.n): 
            g_id = self.find(member)
            if g_id not in group_info: group_info[g_id] = []
            group_info[g_id].append(member)
        return group_info
