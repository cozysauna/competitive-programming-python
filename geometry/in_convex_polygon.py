class Polygon:
    def __init__(self, points):
        self.base_point = points[0]
        self.points = [self._A_to_B_vector(self.base_point, p) for p in points]
        self.N = len(points)

    # ABベクトルを返す
    def _A_to_B_vector(self, A, B):
        return (B[0] - A[0], B[1] - A[1])

    # 外積を求める
    def _cross(self, P1, P2):
        return P1[0] * P2[1] - P1[1] * P2[0]

    def in_convex_polygon(self, xy):
        # (x, y)がpointsで作られる多角形の中に存在するか
        # 多角形は反時計周りに列挙されている必要がある
        xy = self._A_to_B_vector(self.base_point, xy)
        cross1 = self._cross(self.points[1], xy)
        cross2 = self._cross(self.points[self.N - 1], xy)

        if cross1 < 0 or cross2 > 0: return "OUT"

        L = 1
        R = self.N - 1
        while R - L > 1:
            mid = R + L >> 1
            if self._cross(xy, self.points[mid]) >= 0:
                R = mid
            else:
                L = mid

        cross = self._cross(
            self._A_to_B_vector(xy, self.points[L]), 
            self._A_to_B_vector(xy, self.points[R])
        )

        if cross == 0: return "ON"
        elif cross < 0: return "OUT"
        elif cross1 == 0 or cross2 == 0: return "ON"
        else: return "IN"