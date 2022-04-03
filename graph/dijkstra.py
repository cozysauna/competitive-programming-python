from heapq import heappush, heappop
class Dikstra:
    def __init__(self, N, node):
        self.node = node 
        self.N = N 

    def get(self, start, goal):
        dist, done = [10 ** 18] * self.N, [0] * self.N
        hq = [(0, start)] # (cost, node)
        dist[start] = 0
        while hq:
            c, v = heappop(hq)
            done[v] = 1
            for to, cost in self.node[v]: 
                if done[to] == 0 and dist[v] + cost < dist[to]:
                    dist[to] = dist[v]+cost
                    heappush(hq, (dist[to], to))
        return dist[goal]