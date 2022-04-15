def prim(node, N):
    ans = 0
    cnt = 0
    que = [(0, 0)]
    done = [0] * N
    while que:
        c, v = heappop(que)
        if done[v]: continue
        done[v] = 1
        cnt += 1
        ans += c
        if cnt == N: break
        for nx, cost in node[v]: 
            if done[nx]: continue
            heappush(que, (cost, nx))

    return ans