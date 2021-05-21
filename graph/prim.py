def prim(node):
    from heapq import heappush, heappop
    ans = 0
    cnt = 0
    q = [(0, 0)] #cost, start_node
    done = [0]*n
    while q:
        c, v = heappop(q)
        if done[v]: continue
        done[v] = 1
        cnt += 1
        ans += c
        if cnt == n: break
        for cost, nx in node[v]: heappush(q,(cost, nx))

    return ans