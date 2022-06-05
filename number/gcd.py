def gcd(x, y):
    if x == 0: return y
    return gcd(y % x, x)

# gcd without recursions is faster
def gcd(x, y):
    while x: x, y = y % x, x 
    return y