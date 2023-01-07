def z_algorithm(S):
    N = len(S)
    A = [0] * N 
    i = 1
    j = 0
    A[0] = N 
    l = N
    while i < l:
        while i + j < l and S[j] == S[i + j]: j += 1
        if not j:
            i += 1
            continue 
        A[i] = j
        k = 1
        while k < l - i and k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k 
    return A
