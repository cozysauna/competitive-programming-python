class BIT(): # 1-indexed
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
        self.arr = [0] * (N + 1)
 
    # A[i] += x
    def add(self, i, x):
        self.arr[i] += x
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # A[i] = x 
    def update(self, i, x):self.add(i, x - self.arr[i])

    # A[1] + A[2] + ... + A[i]
    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    # A[i]
    def get(self, i): return self.arr[i]

    # max_i (i <= x and A[i] > 0)
    def less_than_x(self, x):
        base = self.sum(x)
        if base == 0: return None 
        ng, ok = 0, x
        while ok - ng > 1:
            mid = ok + ng >> 1
            if self.sum(mid) == base: ok = mid 
            else: ng = mid 
        return ok 

    # min_i (i >= x and A[i] > 0)
    def more_than_x(self, x):
        base = self.sum(x - 1)
        if self.get_all_sum() - base == 0: return None 
        ng, ok = x - 1, self.size
        while ok - ng > 1:
            mid = ng + ok >> 1
            if self.sum(mid) - base == 0: ng = mid 
            else: ok = mid 
        return ok

    def get_all_sum(self): return self.sum(self.size)

    def display_all(self): print(*self.arr[1:])
