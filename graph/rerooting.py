class Rerooting:
    def __init__(self, N, node, e):
        self.dp = [None] * N
        self.node = node 
        self.e = e
        self.ans = [0] * N

    # Abstraction
    def merge(self, a, b): return max(a, b)
    def fin(self, a): return a + 1
    def build(self, start = 0, initial_cost = 0):
        self._dfs1(start)
        self._dfs2(start, initial_cost)

    def _dfs1(self, v, p = -1):
        self.dp[v] = [self.e]  * len(self.node[v])
        ret = self.e
        for i, nx in enumerate(self.node[v]):
            if nx == p: continue
            self.dp[v][i] = self._dfs1(nx, v)
            ret = self.merge(ret, self.dp[v][i])
        return self.fin(ret)

    def _dfs2(self, v, cost, p = -1):
        size = len(self.node[v])

        for i, nx in enumerate(self.node[v]):
            if nx == p: self.dp[v][i] = cost 

        cumL = [self.e] * (size + 1)
        cumR = [self.e] * (size + 1)
        for i in range(size): 
            cumL[i + 1] = self.merge(cumL[i], self.dp[v][i])
        for i in range(size)[::-1]:
            cumR[i] = self.merge(cumR[i + 1], self.dp[v][i])
            
        for i, nx in enumerate(self.node[v]):
            if nx == p: continue
            self._dfs2(nx, self.fin(self.merge(cumL[i], cumR[i + 1])), v)
