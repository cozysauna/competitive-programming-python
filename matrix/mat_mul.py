def mat_mul(A, B):
    y, x = len(A), len(A[0])
    yy, xx = len(B), len(B[0])
    if not yy == x: 
        raise Exception('({}, {}) and ({}, {}) cannot be multipled'.format(y, x, yy, xx))
    mat = [[0] * xx for _ in range(y)]
    for i in range(y):
        for j in range(xx):
            mat[i][j] = sum(A[i][k] * B[k][j] for k in range(x))
    return mat 