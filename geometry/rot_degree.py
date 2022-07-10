from math import pi, sin, cos

def rot_degree(x, y, d):
    rad = d * pi / 180
    _x = x * cos(rad) - y * sin(rad)
    _y = y * cos(rad) + x * sin(rad)
    return (_x, _y)
