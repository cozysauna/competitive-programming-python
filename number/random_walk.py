from math import comb
# p:+1, m:-1
def random_walk(p, m, k):
    if m <= k: return comb(p+m, m)
    if p - m > k: return 0
    return comb(p+m, p) - comb(p+m, p+k+1)