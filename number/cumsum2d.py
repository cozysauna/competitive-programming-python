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

    # [y, y + dy), [x, x + dx)の区間の和
    def get(self, y, x, dy, dx):
        ny = y + dy
        nx = x + dx
        return self.cum[ny][nx] - self.cum[ny][x] - self.cum[y][nx] + self.cum[y][x]
