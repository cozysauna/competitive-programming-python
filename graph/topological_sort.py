from collections import deque
def topological_sort(node, N):
    incnt = [0] * N 
    for nxs in node:
        for nx in nxs:
            incnt[nx] += 1

    que = deque([i for i in range(N) if not incnt[i]])
    ret = []
    while que:
        v = que.popleft()
        ret.append(v)
        for nx in node[v]:
            incnt[nx] -= 1
            if not incnt[nx]:
                que.append(nx)

    return ret