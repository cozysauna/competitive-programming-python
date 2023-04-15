def mat_pow(A, n):
    e = 1
    L = len(A)
    ret = [[0] * L for _ in range(L)]
    for i in range(L):
        ret[i][i] = e

    while n > 0:
        if n & 1:
            ret = mat_mul(A, ret)
        A = mat_mul(A, A)
        n >>= 1

    return ret
