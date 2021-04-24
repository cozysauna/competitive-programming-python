def rec_dec(x): # (length, recurring decimal)
    r, ix, rs, s = 1, 0, [0]*x, ''
    while 1:
        q, r = r//x, r%x  # x = q*y + r
        ix, s = ix+1, s+str(q)
        if not r: return (0, s)
        if rs[r]: return (ix-rs[r], s[rs[r]:])
        rs[r] = ix
        r *= 10 