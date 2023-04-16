class Compress:
    def __init__(self, A, start = 0):
        self.compress = {}
        self.original = {}
        for i, e in enumerate(sorted(set(A)), start):
            self.compress[e] = i
            self.original[i] = e 
        self.N = len(self.compress)

    # 座圧後の要素を取得する object[x] -> compress[x]
    def __getitem__(self, x):
        return self.compress[x]

    # 座圧前の要素を取得する
    def rev(self, x):
        return self.original[x]

    # 座圧後のサイズを取得する
    def get_size(self):
        return self.N
