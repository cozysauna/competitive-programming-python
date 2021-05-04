from sys import setrecursionlimit
from collections import defaultdict
setrecursionlimit(200000)

class SCC():
    def __init__(self, n, node, inv_node):
        self.n = n
        self.node = node
        self.inv_node = inv_node
        self.order = []
        self.done = [0]*(n+1)
        self.inv_done = [0]*(n+1)
        self.group = defaultdict(list) # group 
        self.g = 0 # group count
        for i in range(0, n): # 0-indexed
            if not self.done[i]: self.dfs(i)

        for v in self.order[::-1]:
            if not self.inv_done[v]:  
                self.inv_dfs(v, self.g)
                self.g += 1

    def dfs(self, x):
        self.done[x] = 1
        for nx in self.node[x]:
            if not self.done[nx]: self.dfs(nx)
        self.order.append(x)

    def inv_dfs(self, x, g):
        self.inv_done[x] = 1
        self.group[self.g].append(x)
        for nx in self.inv_node[x]:
            if not self.inv_done[nx]: self.inv_dfs(nx, self.g)

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]
inv_node = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    inv_node[b].append(a)

S = SCC(n, node, inv_node)