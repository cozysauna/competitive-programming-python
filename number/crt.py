# x == b1(mod m1) and x == b2(mod m2) 0 <= r < m1 * m2
def crt(b1, m1, b2, m2): 
    d, p, q = ext_gcd(m1, m2)
    if b1 % d != b2 % d: return 0, -1
    m = lcm(m1, m2)
    t = (b2 - b1) // d * p % (m2 // d)
    r = (b1 + m1 * t) % m 
    return r, m 

def ext_gcd(a, b):
    if a == 0: return (b, 0, 1)
    g, y, x = ext_gcd(b % a, a)
    return g, x - (b // a) * y, y

def gcd(x, y):
    if x == 0: return y 
    return gcd(y % x, x)

def lcm(a, b):
    return a // gcd(a,b) * b