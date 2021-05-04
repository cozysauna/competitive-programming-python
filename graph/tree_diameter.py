def bfs(s, node): # s: start node
    from collections import deque
    d = [-1]*(n+1)
    q = deque([s])
    d[s] = 0
    mx_d, mx_idx = 0, 0
    while q:
        v = q.popleft()
        for nx, c in node[v]:
            if d[nx] != -1: continue
            q.append(nx)
            d[nx] = d[v]+c
            if mx_d < d[nx]: mx_d, mx_idx = d[nx], nx
    return mx_d, mx_idx

# node = [[], [(2, 4), (4, 2)],...] (nx, cost) # ex 1→2 with cost of 4
def tree_d(node): return bfs(bfs(1, node)[1], node)[0]

n = int(input())
node = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    node[a].append((b, c))
    node[b].append((a, c))

print(tree_d(node))