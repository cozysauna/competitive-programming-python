# l < x, y <= r, gcd(x, y) = 1
def coprime_pairs(l, r):
    ret = (r - l)**2
    R = r
    while R > 1:
        a, b = l // R, r // R
        L = max(l // (a + 1), r // (b + 1))
        ret += (L - R) * coprime_pairs(a, b)
        R = L
    return ret