from collections import deque
n, e = map(int, input().split()) # node, edge

node_go = [[] for _ in [0] * n]
node_come = [[] for _ in [0] * n]

for _ in [0] * e:
    a, b = map(int, input().split())
    node_go[a].append(b)
    node_come[b].append(a)

s = deque(i for i in range(n) if node_come[i] == [])

ans = []
while s:
    v = s.popleft()
    ans.append(v)
    for nx_v in node_go[v]:
        node_come[nx_v].remove(v)
        if node_come[nx_v] == []: s.append(nx_v)

print(ans)