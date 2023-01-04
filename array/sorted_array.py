'''
    arrはソートされている必要がある
    lower_bound(x) : x以上の要素を返す
    upper_bound(x) : xより大きい要素を返す
    rev_lower_bound(x) : x以下の要素を返す
    rev_upper_bound(x) : x未満の要素を返す
    get_cnt(x) : x以下の要素の個数を返す
    get_cnt_range(L, R) : L <= x < Rを満たす要素の個数を返す
'''
class SortedArray:
    def __init__(self, arr):
        self.arr = arr 
        self.N = len(arr)
   
    def lower_bound(self, x):
        ng = -1
        ok = self.N 
        while ok - ng > 1:
            mid = ok + ng >> 1 
            if self.arr[mid] >= x: ok = mid 
            else: ng = mid 
        
        if ok == self.N: return None 
        return self.arr[ok]

    def upper_bound(self, x):
        return self.lower_bound(x + 1)

    def rev_lower_bound(self, x):
        ok = -1
        ng = self.N
        while ng - ok > 1:
            mid = ng + ok >> 1
            if self.arr[mid] <= x: ok = mid 
            else: ng = mid 
        if ok == -1: return None
        return self.arr[ok]
    
    def rev_upper_bound(self, x):
        return self.rev_lower_bound(x - 1)

    def get_cnt(self, x):
        ok = -1
        ng = self.N 
        while ng - ok > 1:
            mid = ng + ok >> 1
            if self.arr[mid] <= x: ok = mid 
            else: ng = mid 
        return ok + 1

    def get_cnt_range(self, L, R):
        assert L <= R
        return self.get_cnt_x(R - 1) - self.get_cnt_x(L - 1)