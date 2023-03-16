from collections import deque

class ConvexHullTrick:
    def __init__(self):
        self.lines = deque()

    # y = a * x + b
    def add_line(self, a, b):
        lines = self.lines

        while len(lines) >= 2:
            a1, b1 = lines[-2]
            a2, b2 = lines[-1]
            if (a2 - a1) * (b - b2) < (b2 - b1) * (a - a2): break 
            lines.pop()

        lines.append((a, b))

    # min(ai * x + bi)
    def query(self, x):
        def _f(a, b): return a * x + b

        lines = self.lines
        while len(lines) >= 2 and _f(*lines[0]) >= _f(*lines[1]):
            lines.popleft()

        return _f(*lines[0])
            