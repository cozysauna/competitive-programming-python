 # ax + by = d return (x, y, d); d = gcd(a, b)
def extgcd(a, b):
    if not b: return (1, 0, a)
    x, y, d = extgcd(b, a % b)
    return y, x - a // b * y, d