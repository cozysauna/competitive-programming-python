def divs(n):
    i, divs1, divs2 = 1,[],[]
    while i*i <= n:
        if n % i == 0:
            divs1.append(i)
            if i != n // i: divs2.append(n//i)
        i += 1
    return divs1 + divs2[::-1]