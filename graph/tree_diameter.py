from collections import deque

class TreeDiameter:
    def __init__(self, N, node):
        self.node = node 
        self.N = N

    def get(self):
        _, mx_idx = self.bfs()
        mx_d, _ = self.bfs(mx_idx)
        return mx_d

    def bfs(self, start = 0):
        dist = [10 ** 18] * self.N
        q = deque([start])
        dist[start] = 0
        while q:
            v = q.popleft()
            for nx, c in self.node[v]:
                if dist[nx] > dist[v] + c:
                    q.append(nx)
                    dist[nx] = dist[v] + c
        
        mx_d = max(dist)
        mx_idx = dist.index(mx_d)
        return mx_d, mx_idx