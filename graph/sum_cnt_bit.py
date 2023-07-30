'''
    SumCntBIT

    【説明】
        要素の挿入、削除、K番目に大きい、小さい要素
        上位、下位K個の要素の和の取得がO(logN)でできるデータ構造です
        座標圧縮をしているため、要素が大きい場合にも対応しています
        ABC
            306E
            287G
            281E
            062D etc...
        で利用可能です
    
    【コンストラクタ】
        add_items : add, removeされる要素のリスト(座圧用)

    【メソッド】
        add(x, y) O(logN)             : xの要素をy個追加する
        remove(x, y) O(logN)          : xの要素をy個削除する
        kth_smallest_value(k) O(logN) : k番目に小さい要素を獲得する
        kth_biggest_value(k) O(logN)  : k番目に大きい要素を獲得する
        kth_smallest_sum(k) O(logN)   : 大きい要素上位K個の和を取得する
        kth_biggest_sum(k) O(logN)    : 小さい要素上位K個の和を取得する
        print()                       : 詳細を表示（デバッグ用）
'''

class SumCntBIT:
    def __init__(self, add_items):
        add_items = sorted(set(add_items))
        self.N = len(add_items)
        self.compress = dict(zip(add_items, range(1, self.N + 1)))
        self.original = dict(zip(range(1, self.N + 1), add_items))
        self.sum_data = [0] * (self.N + 1)
        self.cnt_data = [0] * (self.N + 1)
        self.all_cnt = 0
        self.all_sum = 0

    def _add(self, data, i, x):
        while i <= self.N:
            data[i] += x
            i += i & -i

    def add(self, x, y):
        self.all_sum += x * y
        self.all_cnt += y

        self._add(self.sum_data, self.compress[x], x * y)
        self._add(self.cnt_data, self.compress[x], y)

    def remove(self, x, y):
        self.add(x, -y)

    def _lower_bound(self, data, w):
        if w <= 0: return 1
        i = 0
        size = 1 << self.N.bit_length()
        while size > 0:
            if i + size <= self.N and data[i + size] < w:
                w -= data[i + size]
                i += size 
            size >>= 1
        return i + 1
    
    def _sum(self, data, i):
        ret = 0
        while i > 0:
            ret += data[i]
            i -= i & -i
        return ret

    def kth_smallest_value(self, k):
        i = self._lower_bound(self.cnt_data, k)
        return self.original[i]
    
    def kth_biggest_value(self, k):
        return self.kth_smallest_value(self.all_cnt - k + 1)

    def kth_smallest_sum(self, k):
        k = min(k, self.all_cnt)
        i = self._lower_bound(self.cnt_data, k)
        cnt = self._sum(self.cnt_data, i)
        return self._sum(self.sum_data, i) - self.original[i] * (cnt - k)

    def kth_biggest_sum(self, k):
        k = min(k, self.all_cnt)
        return self.all_sum - self.kth_smallest_sum(self.all_cnt - k)

    def print(self):
        print(*[self.kth_smallest_value(i) for i in range(1, self.all_cnt + 1)])
