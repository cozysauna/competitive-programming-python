# node, edge, start
v, e, r = map(int, input().split())
node = [[] for _ in range(v+1)]
for _ in [0] * e:
    s, t, d = map(int, input().split())
    node[s].append((t, d))
    
INF = 10 ** 9
def dijkstra(s): # start and number of nodes
    from heapq import heappush, heappop
    dist, done = [INF] * (n+1), [0]*(n+1)
    hq = [(0, s)] # (cost, node)
    dist[s] = 0
    while hq:
        v = heappop(hq)[1] # get a node
        done[v] = 1
        for to, cost in node[v]: 
            if done[to] == 0 and dist[v]+cost < dist[to]:
                dist[to] = dist[v]+cost
                heappush(hq, (dist[to], to))
    return dist