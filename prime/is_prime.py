def is_prime(x):
    if not x-1 or not x%2: return int(x==2)
    f = 3
    while f*f <= x:
        if not x%f: return 0
        f += 2
    return 1