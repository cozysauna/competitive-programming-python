class MinCostFlow:
    def __init__(self, N):
        self.N = N 
        self.node = [[] for _ in [0] * N]

    def add_edge(self, x, y, capacity, cost): # x -> y
        self.node[x].append([y, capacity, cost, len(self.node[y])])
        self.node[y].append([x, 0, -cost, len(self.node[x]) - 1])

    def min_cost_flow(self, x, y, flow):
        ret = 0
        H = [0] * self.N
        prev_v = [0] * self.N 
        prev_e = [0] * self.N
        while flow:
            dist = [INF] * self.N 
            dist[x] = 0
            que = [(0, x)]
            while que:
                c, v = heappop(que)
                if dist[v] < c: continue 
                for i, (to, capacity, cost, _) in enumerate(self.node[v]):
                    new_cost = dist[v] + cost + H[v] - H[to]
                    if capacity > 0 and dist[to] > new_cost:
                        dist[to] = new_cost
                        prev_v[to] = v 
                        prev_e[to] = i
                        heappush(que, (new_cost, to))

            if dist[y] == INF: return None
            for i in range(self.N): H[i] += dist[i]

            _flow = flow 
            _y = y 
            while _y != x:
                _flow = min(_flow, self.node[prev_v[_y]][prev_e[_y]][1])
                _y = prev_v[_y]

            flow -= _flow 
            ret += _flow * H[y]
            _y = y 
            while _y != x:
                e = self.node[prev_v[_y]][prev_e[_y]]
                e[1] -= _flow
                self.node[_y][e[3]][1] += _flow 
                _y = prev_v[_y]
        return ret 
