score = 0
ans = [None] * Q 

def mo_sort(Ls, Rs):
    l_max = max(Ls)
    r_max = max(Rs)
    bucket_size = max(1, int(r_max / max(1, (Q * 2 / 3) ** .5)))
    bucket_queries = [[] for _ in range(l_max // bucket_size + 1)]
    order = []

    for i, l in enumerate(Ls):
        bucket_queries[l // bucket_size].append(i)

    for i, bucket_query in enumerate(bucket_queries):
        if i & 1:
            bucket_query.sort(key = lambda x: -Rs[x])
        else:
            bucket_query.sort(key = lambda x: Rs[x])

        order.extend(bucket_query)

    return order

def _add(i):
    global score

def _del(i):
    global score

# [L, R)
L = 0; R = 0
for i in mo_sort(Ls, Rs):
    l = Ls[i]
    r = Rs[i]

    while L < l:
        _del(L)
        L += 1

    while L > l:
        _add(L - 1)
        L -= 1

    while R < r:
        _add(R)
        R += 1

    while R > r:
        _del(R - 1)
        R -= 1

    ans[i] = score 
 