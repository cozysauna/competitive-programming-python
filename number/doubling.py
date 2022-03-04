class Doubling():
    def __init__(self, A):
        self.logK = 65
        N = len(A)
        self.db = [[0] * N for _ in range(self.logK)]
        for i in range(N): self.db[0][i] = A[i]
        for k in range(self.logK-1):
            for i in range(N):
                self.db[k+1][i] = self.db[k][self.db[k][i]]
 
    # start -> A[start] -> A[A[start]] ... (loop times)
    def move(self, start, loop):
        now = start
        for k in range(self.logK):
            if loop >> k & 1: now = self.db[k][now]
        return now