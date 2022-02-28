def is_prime(x):
    if x == 1 or x % 2 == 0: return x == 2
    f = 3
    while f * f <= x:
        if x % f == 0: return False 
        f += 2
    return True 