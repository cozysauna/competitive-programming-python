def mat_mul(A, B):
    y1, x1 = len(A), len(A[0])
    y2, x2 = len(B), len(B[0])
    assert x1 == y2 
    mat = [[0] * x2 for _ in range(y1)]
    for i in range(y1):
        for j in range(x2):
            for k in range(x1):
                # mat[i][j] ^= A[i][k] & B[k][j]
                mat[i][j] += A[i][k] * B[k][j]

    return mat 
    