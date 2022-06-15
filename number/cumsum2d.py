class cumsum2d:
    def __init__(self, A):
        H = len(A)
        W = len(A[0])
        self.cum = [[0] * (W + 1) for _ in range(H + 1)] 

        for i in range(H):
            for j in range(W):
                self.cum[i + 1][j + 1] += self.cum[i + 1][j] + A[i][j]

        for j in range(W):
            for i in range(H):
                self.cum[i + 1][j + 1] += self.cum[i][j + 1]

    # i <= y < ii and j <= x < jj
    def get(self, i, ii, j, jj): return self.cum[ii][jj] - self.cum[i][j]
