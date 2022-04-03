class WarshallFloyd:
    def __init__(self, N, cost): # (a, b, c) dist[a][b] = c
        self.dist = [[1 << 30] * N for _ in range(N) ]
        for i in range(N): self.dist[i][i] = 0
        for a, b, c in cost:
            self.dist[a][b] = c 
            self.dist[b][a] = c

        self.prev = [[i] * N for i in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.prev[i][j] = self.prev[k][j]
                
    def get(self, a, b): return self.dist[a][b]

    def way(self, start, goal):
        cur = goal
        ret = [goal]
        while cur != start:
            cur = self.prev[start][cur]
            ret.append(cur)
        return ret[::-1]