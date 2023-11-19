def rle(S):
    N = len(S)
    i = 0
    while i < N:
        j = i
        while j < N and S[i] == S[j]: j += 1
        yield S[i], j - i
        i = j

