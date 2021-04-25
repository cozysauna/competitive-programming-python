class Inv():
    def __init__(self, array):
        self.arr = array
        self.l = len(array)+1
        self.bit = [0]*(self.l+1)

    def add(self, x):
        x += 1
        while x < self.l+1:
            self.bit[x] += 1
            x += x & -x
    def accum(self, x):
        x += 1
        ret =0
        while x:
            ret += self.bit[x]
            x -= x & -x
        return ret

    def find(self):
        ret = 0
        for a in self.arr[::-1]:
            ret += self.accum(a)
            self.add(a)

        return ret

I = Inv(A) # [4, 3, 2, 1] ans: 6
print(I.find())