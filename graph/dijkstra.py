class Dijkstra:
    def __init__(self, N, node):
        self.node = node 
        self.N = N 

    def get(self, start):
        dist = [INF] * self.N
        hq = [(0, start)] # (cost, node)
        dist[start] = 0
        while hq:
            c, v = heappop(hq)
            if dist[v] < c: continue
            for to, cost in self.node[v]: 
                nx_cost = dist[v] + cost
                if nx_cost < dist[to]:
                    dist[to] = nx_cost
                    heappush(hq, (nx_cost, to))
        return dist
