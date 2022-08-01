# distance of ax + by + c = 0 and (x, y)
def point_line_distance(a, b, c, x, y):
    return abs(a * x + b * y + c) / (a ** 2 + b ** 2) ** .5
