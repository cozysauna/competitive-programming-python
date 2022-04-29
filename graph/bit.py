class BIT(): # 1-indexed
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
 
    # A[i] += x
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # A[i] = x #TOO SLOW(Use add if possible)
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

    # max_i (i <= x and 0 < A[i])
    def less_than_x(self, x):
        base = self.sum(x)
        if base == 0: return None 
        bot, top = 0, x 
        while top - bot > 1:
            mid = top + bot >> 1
            if self.sum(mid) == base: top = mid 
            else: bot = mid  
        return top

    # min_i (i >= x and 0 < A[i])
    def more_than_x(self, x):
        base = self.sum(x - 1)
        if self.get_all_sum() - base == 0: return None 
        bot, top = x - 1, self.size
        while top - bot > 1:
            mid = top + bot >> 1
            if self.sum(mid) - base == 0: bot = mid 
            else: top = mid 
        return top 

    def get_all_sum(self): return self.sum(self.size)

    def display_all(self): print(*[self.get(i) for i in range(1, self.size + 1)])