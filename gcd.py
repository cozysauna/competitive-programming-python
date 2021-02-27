def gcd(x, y):
    if x == 0: return y
    else: return gcd(y % x, x)