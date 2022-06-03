from heapq import heappush, heappop
class Dikstra:
    def __init__(self, N, node):
        self.node = node 
        self.N = N 
        self.start_node = None
        self.prev = [None] * N 

    def get(self, start):
        self.start_node = start
        dist, done = [10 ** 18] * self.N, [0] * self.N
        hq = [(0, start)] # (cost, node)
        dist[start] = 0
        while hq:
            c, v = heappop(hq)
            if done[v]: continue
            done[v] = 1
            for to, cost in self.node[v]: 
                new_cost = dist[v] + cost
                if not done[to] and new_cost < dist[to]:
                    dist[to] = new_cost
                    self.prev[to] = v
                    heappush(hq, (dist[to], to))
        return dist

    def init_prev(self): self.prev = [None] * self.N

    def get_path(self, start, to):
        if self.start_node != start:
            self.init_prev()
            self.get(start)
        
        path = []
        while to != None:
            path.append(to)
            to = self.prev[to]

        return path[::-1]