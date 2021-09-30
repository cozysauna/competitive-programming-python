def mat_pow(A, n):
    if not n: return [[1, 0], [0, 1]]
    m = mat_pow(A, n//2)
    if n % 2:
        return mat_mul(A, mat_mul(m, m))
    else:
        return mat_mul(m, m)