def to_int(x, base): # also supports negative base
    if not x: return ''
    r = (x % abs(base) + abs(base)) % abs(base)
    x = (x - r) // base
    return to_int(x, base) + str(r)