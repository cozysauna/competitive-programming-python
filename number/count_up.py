# 0 <= i, j < N && T = i + j となる(i, j)のペアの数
def get_double_cnt(N, T):
    return max(0, min(T + 1, 2 * N - 1 - T))

# 0 <= i, j, k < N && T = i + j + k となる(i, j, k)のペアの数
def get_triple_cnt(N, T):
    if 0 <= T < N:
        return (T + 1) * (T + 2) // 2
    if N <= T <= 2 * N - 3:
        return (9 * N - 3 * N * N + 6 * N * T - 6 * T - 2 * T * T - 4) // 2
    if 2 * N - 3 < T <= 3 * N - 3:
        return (3 * N - T - 1) * (3 * N - T - 2) // 2
    return 0
