class BIT():
   def __init__(self, n, a):
       self.n = n
       self.tree = [0]*(n + 1)
       self.update(1, a[0])
       for i in range(1, n):
           self.update(i + 1, a[i] - a[i - 1])
 
   def update(self, i, x):
       while i <= self.n:
           self.tree[i] += x
           i += i & -i
 
   def at(self, i):
       ret = 0
       while i > 0:
           ret += self.tree[i]
           i -= i & -i
       return ret
 
   def range_update(self, l, r, x):
       self.update(l, x)
       self.update(r, -x)