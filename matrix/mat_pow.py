def mat_pow(A, n):
    if not n: 
        identity_matrix = [[1 if i == j else 0 for i in range(len(A))] for j in range(len(A))]
        return identity_matrix

    m = mat_pow(A, n//2)
    if n % 2:
        return mat_mul(A, mat_mul(m, m))
    else:
        return mat_mul(m, m)