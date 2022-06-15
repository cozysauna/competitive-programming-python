class SCC:
    def __init__(self, N, node):
        self.N = N
        self.node = node
        self.inv_node = [[] for _ in range(self.N)]
        for i in range(N):
            for v in node[i]:
                self.inv_node[v].append(i)

        self.order = []
        self.done = [0] * N
        for i in range(N):
            if not self.done[i]: 
                self.dfs(i)

        self.inv_done = [0] * N
        self.group_members = {}
        self.group = [None] * N
        self.g = 0 # group count
        for v in self.order[::-1]:
            if not self.inv_done[v]:  
                self.group_members[self.g] = []
                self.inv_dfs(v)
                self.g += 1

    def dfs(self, x):
        self.done[x] = 1
        for nx in self.node[x]:
            if not self.done[nx]: 
                self.dfs(nx)
        self.order.append(x)

    def inv_dfs(self, x):
        self.inv_done[x] = 1
        self.group_members[self.g].append(x)
        self.group[x] = self.g
        for nx in self.inv_node[x]:
            if not self.inv_done[nx]: 
                self.inv_dfs(nx)

    def get_group(self, x): return self.group[x]

    def same(self, x, y): return self.group[x] == self.group[y]
