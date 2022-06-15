# num(x) -> num(y)
def base_conversion(num, x, y):
    k = int(str(num), base = x)
    m = []
    while k:
        d = k % y 
        m.append(d)
        k //= y 
    return ''.join(map(str, m[::-1]))