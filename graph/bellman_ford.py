def bellman_ford(N, node, start = 0):
    dist = [10 ** 18] * N
    dist[start] = 0
    for _ in range(N):
        update = False
        for x, y, c in node:
            if dist[y] > dist[x] + c:
                dist[y] = dist[x] + c
                update = True
        if not update: break
        
    # find negative cycle
    negative_flag = [0] * N
    for _ in range(N):
        for x, y, c in node:
            if dist[x] == 10 ** 18: continue
            if dist[y] > dist[x] + c:
                dist[y] = dist[x] + c
                negative_flag[y] = 1
            if negative_flag[x]: 
                negative_flag[y] = 1

    return dist, negative_flag
