'''
    Fenwick-Tree

    【説明】
        1-indexed

    【コンストラクタ】
        N : 配列のサイズ

    【メソッド】
        add(i)          : A[i] += x
        update(i, x)    : A[i] = x
        sum(i)          : A[1] + A[2] + ... + A[i]
        range_sum(l, r) : A[l] + A[l + 1] + ... + A[r]
        get(i)          : A[i]を取得
        get_all_sum()   : A[1] + A[2] + ... + A[N]
        lower_bound(w)  : A[1] + A[2] + ... + A[i] >= w となる最小のi
        more_than_x(x)  : i >= x && A[i] > 0となる最小のiを取得
        less_than_x(x)  : i <= x && A[i] > 0となる最大のiを取得
        print()         : Aを表示
'''

class BIT():
    def __init__(self, N):
        self.N = N
        self.data = [0] * (N + 1)
        self.A = [0] * (N + 1)
        self.all_sum = 0
 
    def add(self, i, x):
        self.all_sum += x
        self.A[i] += x
        while i <= self.N:
            self.data[i] += x
            i += i & -i

    def update(self, i, x): self.add(i, x - self.A[i])

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.data[i]
            i -= i & -i
        return ret
    
    def range_sum(self, l, r): return self.sum(r) - self.sum(l - 1)

    def get(self, i): return self.A[i]
    
    def less_than_x(self, x): return self.lower_bound(self.sum(x))
    
    def more_than_x(self, x): return self.lower_bound(self.sum(x - 1) + 1)

    def lower_bound(self, w):
        if w <= 0: return None
        if w > self.get_all_sum(): return None
        i = 0
        size = 1 << self.N.bit_length()
        while size > 0:
            if i + size <= self.N and self.data[i + size] < w:
                w -= self.data[i + size]
                i += size 
            size >>= 1

        return i + 1

    def get_all_sum(self): return self.all_sum

    def print(self):
        for i in range(1, self.N + 1):
            print(f"[{i}] : {self.A[i]}")
