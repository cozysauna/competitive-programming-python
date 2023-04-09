#SにWが含まれるかをO(N)で判断
class KMP:
    # Wについてのtableを構築する
    def __init__(self, W):
        N = len(W)
        table = [0] * (N + 1)
        table[0] = -1
        i = 0
        for p in range(1, N):
            if W[p] == W[i]:
                table[p] = table[i]
            else:
                table[p] = i
                i = table[i]
                while i >= 0 and W[p] != W[i]:
                    i = table[i]
            i += 1

        table[N] = i
        self.table = table
        self.W = W

    # WがSに含まれているか
    def find(self, S):
        W = self.W
        table = self.table
        ret = []
        S_length = len(S)
        W_length = len(W)
        i = 0
        j = 0
        while i < S_length:
            if S[i] == W[j]:
                i += 1
                j += 1
                if j == W_length:
                    ret.append(i - j)
                    j = table[j]
            else:
                j = table[j]
                if j < 0:
                    i += 1
                    j += 1
        return ret
