class find_cycle():
    from collections import defaultdict
    def __init__(self, n_iter, start):
        self.n_iter = n_iter
        self.start = start
        self.M = dict() # {value: index}
        self.G = dict() # {index: value}
        # if cycle doesn't appear, cycle_size is -1
        self.cycle_size, self.end_index, self.end_value = self.find()

    def find(self):
        now = self.start
        M = defaultdict(int)
        G = defaultdict(int)
        for i in range(k):
            if now in M:
                cycle_size = i-M[now]
                reminder = k-i
                end_index = M[now]+reminder % cycle_size
                end_value = G[end_index]
                self.M = M
                self.G = G
                return cycle_size, end_index, end_value
            M[now] = i
            G[i] = now
            now = self.change(now)
        end_index = k-1
        end_value = now
        self.M = M
        self.G = G
        return -1, end_index, end_value

    # the way how a number changes
    def change(self, x):
        return (x+sum(map(int, list(str(x)))))%10**5