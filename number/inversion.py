class Inv():
    def __init__(self, array):
        self.arr = array
        self.l = max(len(array), max(array))+1
        self.bit = [0]*(self.l+1)
        self.cnt = dict()

    def add(self, x):
        x += 1
        while x < self.l+1:
            self.bit[x] += 1
            x += x & -x
            
    def accum(self, x):
        x += 1
        s = x
        ret = 0
        while x:
            ret += self.bit[x]
            x -= x & -x
        return ret

    def find(self):
        ret = 0
        for a in self.arr[::-1]:
            ret += self.accum(a)
            if a in self.cnt: 
                ret -= self.cnt[a]
                self.cnt[a] += 1
            else:
                self.cnt[a] = 1
            self.add(a)
        return ret