class SegTree2D:
    def __init__(self, arrays, func, e):
        N = len(arrays)
        M = len(arrays[0])
        self.e = e
        self.func = func
        self.N = N
        self.M = M
        self.KN = (N - 1).bit_length()
        self.KM = (M - 1).bit_length()
        self.N2 = 1 << self.KN
        self.M2 = 1 << self.KM
        self.dat = [[0] * (2**(self.KM + 1)) for i in range(2**(self.KN + 1))]
        for i in range(self.N):
            for j in range(self.M):
                self.dat[self.N2 + i][self.M2 + j] = arrays[i][j]
        self.build()

    def build(self):
        for j in range(self.M):
            for i in range(self.N2 - 1, 0, -1):
                self.dat[i][self.M2 + j] = self.func(self.dat[i << 1][self.M2 + j], self.dat[i << 1 | 1][self.M2 + j])

        for i in range(2 ** (self.KN + 1)):
            for j in range(self.M2 - 1, 0, -1):
                self.dat[i][j] = self.func(self.dat[i][j << 1], self.dat[i][j << 1 | 1])

    def query(self, Lx, Ly, Rx, Ry):
        # [Lx, Ly) and [Rx, Ry)
        #     Ly     Ry
        # Lx  ######
        #     ######
        # Rx
        Lx += self.N2
        Rx += self.N2
        Ly += self.M2
        Ry += self.M2
        vLx = self.e
        vRx = self.e       
        while Lx < Rx:
            if Lx & 1:
                vLy = self.e
                vRy = self.e
                Ly1 = Ly
                Ry1 = Ry
                while Ly1 < Ry1:
                    if Ly1 & 1:
                        vLy = self.func(vLy, self.dat[Lx][Ly1])
                        Ly1 += 1
                    if Ry1 & 1:
                        Ry1 -= 1
                        vRy = self.func(self.dat[Lx][Ry1], vRy)
                    Ly1 >>= 1
                    Ry1 >>= 1
                vy = self.func(vLy, vRy)
                vLx = self.func(vLx,vy)
                Lx += 1
            if Rx & 1:
                Rx -= 1
                vLy = self.e
                vRy = self.e
                Ly1 = Ly
                Ry1 = Ry
                while Ly1 < Ry1:
                    if Ly1 & 1:
                        vLy = self.func(vLy, self.dat[Rx][Ly1])
                        Ly1 += 1
                    if Ry1 & 1:
                        Ry1 -= 1
                        vRy = self.func(self.dat[Rx][Ry1], vRy)
                    Ly1 >>= 1
                    Ry1 >>= 1 
                vy = self.func(vLy, vRy)               
                vRx = self.func(vy, vRx)
            Lx >>= 1
            Rx >>= 1
        return self.func(vLx, vRx)
