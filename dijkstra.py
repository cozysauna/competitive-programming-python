from heapq import heappush, heappop

# node, edge, start
v, e, r = map(int, input().split())
node = [[] for _ in range(v+1)]
for i in range(e):
    s, t, d = map(int, input().split())
    node[s].append((t, d))
    
INF = 10 ** 9
def dijkstra(s, n): # start and number of nodes
    dist = [INF] * n
    hq = [(0, s)] # (cost, node)
    dist[s] = 0
    checked = [False] * n 
    while hq:
        v = heappop(hq)[1] # get a node
        checked[v] = True
        for to, cost in node[v]: 
            if checked[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist