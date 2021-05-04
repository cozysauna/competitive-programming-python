def to_int(x, base): # supports also negative base
    if not x: return ''
    r = (x%abs(base)+abs(base))%abs(base)
    x = (x-r)//base
    return to_int(x, base) + str(r)

print(to_int(n, -2))