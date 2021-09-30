def fibonacci(x):
    return mat_mul(mat_pow([[1, 1], [1, 0]], x), [[1], [0]])[0][0]