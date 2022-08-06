from heapq import heappush, heappop, heappushpop
class SlopeTrick:
    # f(x) = 0
    def __init__(self):
        INF = 10 ** 18
        self.L = [INF]
        self.R = [INF]
        self.mn = 0

    # f(x) += |x - a| + b
    def add_ablsolute_value(self, a, b):
        self.mn += max(0, -self.L[0] - a)
        heappush(self.R, -heappushpop(self.L, -a))
        self.mn += max(0, a - self.R[0])
        heappush(self.L, -heappushpop(self.R, a))
        self.mn += b

    # f(x) = mn
    def get_min(self):
        x = -self.L[0]
        return x, self.mn
