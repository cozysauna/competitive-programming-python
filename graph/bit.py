class BIT():
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # A[i] = x 
    def update(self, i, x):
        old = self.get(i)
        self.add(i, x - old)

    # A[1] + A[2] + ... + A[i]
    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    # A[i]
    def get(self, i):
        return self.sum(i) - self.sum(i - 1)

    # max i (i <= x and 0 < A[i])
    def less_than_x(self, x):
        base = self.sum(x)
        if base == 0: return None 
        bot, top = 0, x 
        while top - bot > 1:
            mid = top + bot >> 1
            if self.sum(mid) == base: top = mid 
            else: bot = mid  
        return top