class Cumsum:
    def __init__(self, A):
        t, self.cum = 0, [0]
        for a in A: 
            t += a
            self.cum.append(t)

    #[l, r)
    def get(self, l, r): return self.cum[r] - self.cum[l]
