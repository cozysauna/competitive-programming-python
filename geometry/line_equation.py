# Equation which passes through the two points (x1, y1), (x2, y2)
# (a, b, c) (ax + by + c = 0)
def line_equation(x1, y1, x2, y2): 
    a = y1 - y2 
    b = x2 - x1 
    c = y1 * (x1 - x2) - x1 * (y1 - y2)
    return a, b, c 
