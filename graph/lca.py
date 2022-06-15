class LCA:
    def __init__(self, node, root = 0):
        self.node = node
        self.root = root
        self.N = len(node)
        self.logn = (self.N - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.N)]
        self.parent = [[-1] * self.N for _ in range(self.logn)]
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.node[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que.append(v)

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.N):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get(self, u, v):
        if self.depth[v] < self.depth[u]: u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):
            if (dv - du) >> i % 2:
                v = self.parent[i][v]
        if u == v: return u
        for i in range(self.logn - 1, -1, -1):
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv: u, v = pu, pv

        return self.parent[0][u]
