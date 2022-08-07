class BIT_2d:
    # 0-indexed
    def __init__(self, H, W):
        self.H = H + 1
        self.W = W + 1
        self.arr = [0] * self.W * self.H
        
    def add(self, i, j, x):
        i += 1
        j += 1
        _j = j
        arr = self.arr
        H = self.H
        W = self.W
        while i < H:
            j = _j
            while j < W:
                arr[i * W + j] += x
                j += j & - j
            i += i & -i

    def sum(self, i, j):
        arr = self.arr
        ret = 0
        _j = j
        W = self.W
        while i:
            j = _j
            while j:
                ret += arr[i * W + j]
                j -= j & -j
            i -= i & - i
        return ret

    # x0 <= x < x1 and y0 <= y < y1
    def range_sum(self, x0, x1, y0, y1):
        return self.sum(x1, y1) - self.sum(x1, y0) - self.sum(x0, y1) + self.sum(x0, y0)
