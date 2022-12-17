from functools import cmp_to_key
def degree_sort(points):
    def quadrant(x, y):
        if x >= 0 and y >= 0: return 1
        if x <= 0 and y >= 0: return 2
        if x <= 0 and y <= 0: return 3
        if x >= 0 and y <= 0: return 4

    def points_cmp(p, q):
        p_qua = quadrant(*p)
        q_que = quadrant(*q)
        if p_qua == q_que:
            px, py = p
            qx, qy = q
            op = px * qy - py * qx
            return -1 if op > 0 else 1 if op < 0 else 0
        else:
            return -1 if p_qua < q_que else 1

    return sorted(points, key = cmp_to_key(points_cmp))