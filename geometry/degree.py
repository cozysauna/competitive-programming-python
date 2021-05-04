def degree_2(ox, oy, x1, y1, x2, y2): # Origin, P1, P2
    import math
    d1 = (math.atan2(ox-x1, oy-y1)*180/math.pi+180)%180
    d2 = (math.atan2(ox-x2, oy-y2)*180/math.pi+180)%180
    return (d1-d2+360)%180

# print(degree_2(0, 0, 1, 0, 0, 1))

def degree_3(ox, oy, oz, x1, y1, z1, x2, y2, z2):
    import math
    o, p1, p2 = [ox, oy, oz], [x1, y1, z1], [x2, y2, z2]
    v1, v2 = [p1[i]-o[i] for i in range(3)], [p2[i]-o[i] for i in range(3)]
    n1, n2 = sum(map(lambda x: x**2, v1))**.5, sum(map(lambda x: x**2, v2))**.5
    ip = sum([v1[i]*v2[i] for i in range(3)])
    cos = ip / (n1 * n2)
    return math.degrees(math.acos(cos))

# print(degree_3(0, 0, 0, 1, 0, 0, 0, 1, 0))