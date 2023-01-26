from math import atan2
'''
    A(x_1, y_2)、B(x_2, y_2)
    B = A * (cosθ + isinθ)となるθを求める
'''
def get_two_points_rad(x_1, y_1, x_2, y_2):
    rad = atan2(y_1, x_1) - atan2(y_2, x_2)
    return rad
