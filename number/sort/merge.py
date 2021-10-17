def merge_sort(A):
    if len(A) <= 1: return A
    X = len(A)//2 
    L = merge_sort(A[:X])
    R = merge_sort(A[X:])
    L += R[::-1]
    l, r = 0, len(L)-1
    B = []
    while l <= r:
        if L[l] <= L[r]:
            B.append(L[l])
            l += 1
        else:
            B.append(L[r])
            r -= 1
    return B