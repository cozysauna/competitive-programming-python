from collections import defaultdict
from heapq import heappop, heappush

class RemovableHeapq:
    def __init__(self):
        self.que = []
        self.cnt = defaultdict(int)

    def push(self, x):
        heappush(self.que, x)
        self.cnt[x] += 1

    def pop(self):
        self._clean_que()
        x = heappop(self.que)
        self.cnt[x] -= 1
        return x 
    
    def remove(self, x): self.cnt[x] = max(0, self.cnt[x] - 1)

    def remove_all(self, x): self.cnt[x] = 0

    def min(self):
        self._clean_que()
        return self.que[0]
    
    def is_empty(self): 
        self._clean_que()
        return len(self.que) == 0

    def _clean_que(self):
        while self.que and self.cnt[self.que[0]] == 0: 
            heappop(self.que)