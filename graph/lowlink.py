class LowLink:
    def __init__(self, N, node, root = 0):
        self.N = N 
        self.node = node 
        self.ord = [None] * N
        self.low = [None] * N
        self.k = 0
        self.root = root 
        self.articulation_points = []
        self.bridges = []
        self.dfs(root)

    def dfs(self, x, p = -1):
        self.ord[x] = self.k
        self.low[x] = self.k
        self.k += 1
        child = 0
        ap_flag = False 
        for nx in self.node[x]:
            if nx == p: continue 
            if self.ord[nx] == None:
                self.dfs(nx, x)
                self.low[x] = min(self.low[x], self.low[nx])
                child += 1
                if self.ord[x] <= self.low[nx]: ap_flag = True
                if self.ord[x] < self.low[nx]: self.bridges.append((x, nx))
            else:
                self.low[x] = min(self.low[x], self.ord[nx])
        
        if (x == self.root and child > 1) or (x != self.root and ap_flag):
            self.articulation_points.append(x)

    def get_bridges(self): return self.bridges
    
    def get_articulation_points(self): return self.articulation_points
