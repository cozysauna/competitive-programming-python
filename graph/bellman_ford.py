def bellman_ford(s): # x => y with cost c
    d = [INF] * n
    d[s] = 0
    for i in range(n):
        update = False
        for x, y, c in edge:
            if d[y] > d[x] + c:
                d[y] = d[x] + c
                update = True
        if not update: break
        
    # find negative cycle
    negative_flag = [0] * n
    for i in range(n):
        for x, y, c in edge:
            if d[x] == INF: continue
            if d[y] > d[x] + c:
                d[y] = d[x] + c
                negative_flag[y] = 1
            if negative_flag[x]: 
                negative_flag[y] = 1
    return d, negative_flag