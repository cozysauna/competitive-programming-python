'''
    [0, N)のN個の数字を2個ずつの組に分ける
    ex) N = 4
    [
        [0, 1, 2, 3], 
        [0, 2, 1, 3], 
        [0, 3, 1, 2]
    ]
'''
def two_pairs(N):
    pairs = []
    pair = []
    def _search(bit):
        if bit == (1 << N) - 1:
            return pairs.append(pair[::])
        ok = [i for i in range(N) if not bit >> i & 1]
        p = ok[0]
        pair.append(p)
        for q in ok[1:]:
            pair.append(q)
            _search(bit | 1 << p | 1 << q)
            pair.pop()
        else:
            pair.pop()

    _search(0)

    return pairs
