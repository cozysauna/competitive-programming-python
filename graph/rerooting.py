class Rerooting:
    def __init__(self, N, node, e, func, start = 0):
        self.dp = [[e] * len(node[i]) for i in range(N)]
        self.node = node 
        self.e = e 
        self.func = func
        self.start = start

        self._dfs(x = start)
        self._bfs(x = start)

    def _dfs(self, x = 0, p = -1):
        k = self.e 
        dpx = self.dp[x]
        for i, nx in enumerate(self.node[x]):
            if nx == p: continue
            # 変更点
            dpx[i] = self._dfs(nx, x) + 1
            # 変更点
            k = self.func(k, dpx[i])
        return k

    def _bfs(self, x = 0, p = -1, pre_cost = 0):
        edge_size = len(self.node[x])
        dpx = self.dp[x]
        for i, nx in enumerate(self.node[x]):
            if nx == p:
                # 前の部分木の情報を使いdpテーブルを更新する、変更点
                dpx[i] = pre_cost + 1

        cum_L = [self.e] * (edge_size + 1)
        cum_R = [self.e] * (edge_size + 1)

        # 変更点
        for i in range(edge_size):
            cum_L[i + 1] = self.func(cum_L[i], dpx[i])
        for i in range(edge_size)[::-1]:
            cum_R[i] = self.func(cum_R[i + 1], dpx[i])


        for i, nx in enumerate(self.node[x]):
            if nx != p:
                # 変更点
                self._bfs(nx, x, self.func(cum_L[i], cum_R[i + 1]))
