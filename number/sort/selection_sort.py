def selection_sort(A):
    for k in range(len(A)-1):
        mn = 10 ** 10
        idx = -1
        for i in range(k, len(A)):
            if mn > A[i]:
                mn = A[i]
                idx = i 
        
        A[k], A[idx] = A[idx], A[k]
    return A