def func(x, y): return max(x, y)
e = 0

class SegTree:
    def __init__(self, array, func, e):
        n = len(array)
        self.func = func
        self.e = e
        self.num = 1 << (n-1).bit_length()
        self.tree = [e] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = array[i]

        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.func(self.tree[2*i], self.tree[2*i+1])

    def update(self, k, x): # A[k-1] = x
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.func(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r): # [l, r)
        ret = self.e
        l += self.num
        r += self.num

        while l < r:
            if l & 1:
                ret = self.func(ret, self.tree[l])
                l += 1
            if r & 1:
                ret = self.func(ret, self.tree[r-1])
            l >>= 1
            r >>= 1
        return ret