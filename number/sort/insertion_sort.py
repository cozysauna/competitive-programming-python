def insertion_sort(A):
    for k in range(1, len(A)):
        pos = k 
        while pos != 0 and A[pos-1] > A[pos]:
            A[pos-1], A[pos] = A[pos], A[pos-1]
            pos -= 1
    return A