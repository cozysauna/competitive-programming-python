def mat_mul(A, B):
    y1, x1 = len(A), len(A[0])
    y2, x2 = len(B), len(B[0])
    assert x1 == y2 
    mat = [[0] * x2 for _ in [None] * y1]

    for i, mati in enumerate(mat):
        for k, aik in enumerate(A[i]):
            for j, bkj in enumerate(B[k]):
                # mati[j] ^= aik & bkj
                mati[j] += aik * bkj

    return mat 