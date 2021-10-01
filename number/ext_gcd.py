def extgcd(a, b): # ax + by = d (x, y, d)
    if not b: return (1, 0, a)
    x, y, d = extgcd(b, a % b)
    return y, x - a // b * y, d