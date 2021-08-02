def divs(n):
    i, d, dd = 1,[],[]
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if i != n // i: dd.append(n//i)
        i += 1
    return d + dd[::-1]