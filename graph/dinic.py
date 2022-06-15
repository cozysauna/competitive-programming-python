class Dinic:
    def __init__(self, N):
        self.N = N
        self.node = [[] for _ in range(N)]

    def add_edge(self, x, y, capacity): # x -> y
        self.node[x].append([y, capacity, len(self.node[y])]) # to, capacity, rev
        self.node[y].append([x, 0, len(self.node[x]) - 1])

    def bfs(self, start):
        self.level = [-1] * self.N 
        self.level[start] = 0
        que = deque([start])
        while que:
            v = que.popleft()
            for to, capacity, _ in self.node[v]:
                if capacity > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    que.append(to)

    def dfs(self, s, t, flow):
        if s == t: return flow 
        for i in range(self.iter[s], len(self.node[s])):
            self.iter[s] = i 
            to, capacity, rev = self.node[s][i]
            if capacity > 0 and self.level[s] < self.level[to]:
                pre_flow = self.dfs(to, t, min(flow, capacity))
                if pre_flow > 0:
                    self.node[s][i][1] -= pre_flow
                    self.node[to][rev][1] += pre_flow
                    return pre_flow
        return 0

    def flow(self, s, t):
        mx_flow = 0
        while True:
            self.bfs(s)
            if self.level[t] < 0: break
            self.iter = [0] * self.N 
            while True:
                f = self.dfs(s, t, 10 ** 18)
                if f == 0: break 
                mx_flow += f
    
        return mx_flow
