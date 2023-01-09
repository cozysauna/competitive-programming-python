class WeightedUnionFind:
    def __init__(self, N):
        self.N = N 
        self.P = [-1] * N 
        self.WEIGHT = [0] * N 

    def find(self, x):
        if self.P[x] < 0: return x
        self.WEIGHT[x] += self.WEIGHT[self.P[x]]
        self.P[x] = self.find(self.P[x])
        return self.P[x]

    # x + w = y
    def union(self, x, y, w):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            assert self.diff(x, y) == w
            return 

        if self.P[x] < self.P[y]:
            x, y = y, x 
            w = - w

        self.P[x] = y 
        self.P[y] += self.P[x]
        self.WEIGHT[x] = w - self.WEIGHT[x] + self.WEIGHT[y]
            
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.WEIGHT[x] - self.WEIGHT[y]