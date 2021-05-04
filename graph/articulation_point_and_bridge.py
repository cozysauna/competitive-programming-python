from sys import setrecursionlimit
setrecursionlimit = 5000

class art_bri():
    # node = [[], [4, 2], [1, 3]] 1-4, 1-2, 2-1, 2-3,
    # edge = [(1, 4), (1, 2), (1, 3)]...
    def __init__(self, n, node, edge):
        self.ords = [-1]*(n+1)
        self.lowlink = [-1]*(n+1)
        self.used_node = set()
        self.back_node = set()
        self.edge = edge
        self.s = 1 # if 0-indexed, change this num to 0
        self.find_ord(self.s, self.s, self.s)
        self.find_lowerlink()
        self.bridge = self.find_bridge()
        self.art = self.find_art()
    
    def find_ord(self, u, v, cnt): # u →　v
        v1, v2 = min(u, v), max(u, v)
        if self.ords[v] != -1: 
            if (v1, v2) not in self.used_node and (v1, v2) not in self.back_node: self.back_node.add((v1, v2))
            return
        if v1-v2: self.used_node.add((v1, v2))
        self.ords[v], self.lowlink[v] = cnt, cnt
        for nx in node[v]: self.find_ord(v, nx, cnt+1)

    def back_to_root(self, x, cost):
        for nx in node[x]:
            if self.ords[nx] > self.ords[x]: continue
            if self.lowlink[nx] > cost:
                self.lowlink[nx] = cost
                self.back_to_root(nx, cost)

    def find_lowerlink(self):
        self.back_node = list(self.back_node)
        self.back_node.sort(key = lambda x: min(self.ords[x[0]], self.ords[x[1]]))
        for u, v in self.back_node: # u →　v
            if self.ords[u] > self.ords[v]: u, v = v, u
            if self.lowlink[v] > self.ords[u]: self.lowlink[v] = self.ords[u] 
            self.back_to_root(v, self.ords[u])

    def find_bridge(self):
        ret = []
        for u, v in self.edge:
            if self.ords[u] > self.ords[v]: u, v = v, u
            if self.ords[u] < self.lowlink[v]: ret.append((u, v))
        return ret

    def find_art(self):
        ret = []
        for e in range(1, n+1): # if 0-indexed, change this range into 0, n
            if e == self.s: 
                cnt = 0
                for nx in node[e]:
                    if (min(e, nx), max(e, nx)) not in self.back_node: cnt += 1
                if cnt >= 2: ret.append(e)
                continue
            tmp = -1
            for nx in node[e]:
                if self.ords[nx] > self.ords[e] and (min(e, nx), max(e, nx)) not in self.back_node: tmp = max(tmp, self.lowlink[nx])
            if self.ords[e] <= tmp: ret.append(e)
        return ret            

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]
edge = []

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
    edge.append([a, b])

U = art_bri(n, node, edge)
print(len(U.bridge))