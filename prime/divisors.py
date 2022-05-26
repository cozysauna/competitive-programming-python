def divs(N):
    i, d, dd = 1, [], []
    while i * i < N:
        if N % i == 0:
            d.append(i)
            dd.append(N // i)
        i += 1
    else:
        if i * i == N and N % i == 0: d.append(i)
    return d + dd[::-1]