# cost: 2d-array, v: the number of nodes
# if cost[i][i] is less than 0, this graph has a negative cycle
def warshall_floyd(cost, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
    return cost
