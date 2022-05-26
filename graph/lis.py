from bisect import bisect_left

def lis(A):
    table = [A[0]]
    for a in A:
        if a > table[-1]: table.append(a)
        else: table[bisect_left(table, a)] = a
    
    return len(table)

def lis2(A): # slower lis
    INF = 1 << 60
    table = [INF] * len(A)
    for a in A: 
        table[bisect_left(table, a)] = a

    return bisect_left(table, INF)