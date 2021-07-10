from collections import defaultdict, deque
from itertools import permutations, combinations, product
from functools import lru_cache
def pprint(E): 
  for e in E: print(e)
from sys import setrecursionlimit, stdin
setrecursionlimit(500000)
readline = stdin.readline
# @lru_cache(maxsize=None)
INF = 10 ** 18
MOD = 1000000007
MOD2 = 998244353
cnt = ans = tmp = 0
yes, no = 'Yes', 'No'
yay = None
def I(): return int(readline())
def S(): return readline()[:-1]
def LI(): return list(map(int, readline().split()))
def SPI(): return map(int, readline().split())
def FIE(x): return [readline()[:-1] for _ in [0]*x]
def ENU(x): return enumerate(x)
def NODE(x): return [[] for _ in [0]*(x+1)]
def ZERO(x): return [0]*x
def ZEROS(y, x): return [[0]*x for _ in [0]*y]
def ZEROSS(z, y, x): return [[[0]*x for _ in [0]*y] for _ in [0]*z]
####################################################################
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