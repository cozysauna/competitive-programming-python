def check(k):
    pass

def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        mid = ok + ng >> 1
        if check(mid):
            ok = mid
        else:
            ng = mid
    return ok
