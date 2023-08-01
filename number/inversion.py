# 1-indexed A[i] > A[j] (i, j)
def inversion(A):

    N = len(A)
    data = [0] * (N + 1)

    def _sum(i):
        ret = 0
        while i > 0:
            ret += data[i]
            i -= i & -i
        return ret

    def _add(i, x):
        while i <= N:
            data[i] += x
            i += i & -i

    inv = 0
    for a in A[::-1]:
        inv += _sum(a - 1)
        _add(a, 1)
    return inv