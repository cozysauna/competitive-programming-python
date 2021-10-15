def quick_sort(A):
    if len(A) <= 1: return A
    L, M, R = [], [], []
    X = len(A)//2
    for a in A:
        if a == A[X]: M.append(a)
        elif a < A[X]: L.append(a)
        else: R.append(a)
    L = quick_sort(L)
    R = quick_sort(R)
    return L + M + R  