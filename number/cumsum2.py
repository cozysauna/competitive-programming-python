class cumsum2():
    def __init__(self, arr):
        self.arr = arr
        self.H = len(arr)
        self.W = len(arr[0])
        self.cum_arr = self.find_cum_arr()

    def find_cum_arr(self):
        ret = [[0] * self.W for _ in range(self.H)]
        for i in range(self.H):
            for j in range(self.W):
                ret[i][j] = self.arr[i][j]
                if j: ret[i][j] += ret[i][j-1]
        
        for j in range(self.W):
            for i in range(1, self.H):
                ret[i][j] += ret[i-1][j]
        return ret

    # i <= y <= ii & j <= x <= jj
    def find(self, i, j, ii, jj):
        ret = self.cum_arr[ii][jj]
        if i > 0: ret -= self.cum_arr[i-1][jj]
        if j > 0: ret -= self.cum_arr[ii][j-1]
        if i > 0 and j > 0: ret += self.cum_arr[i-1][j-1]
        return ret