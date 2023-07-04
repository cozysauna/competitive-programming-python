def compare(l, r):
    pass

def merge_sort(A):
    N = len(A)
    stack = [(1, 0, N)]
    while stack:
        t, l, r = stack.pop()
        mid = l + r >> 1
        if t:
            if r - l <= 1: continue
            stack.append((0, l, r))
            stack.append((1, mid, r))
            stack.append((1, l, mid))
        else: 
            # merge
            sorted_array = []
            li = l 
            ri = mid 
            while li < mid and ri < r:
                if compare(A[li], A[ri]):
                    sorted_array.append(A[li])
                    li += 1
                else:
                    sorted_array.append(A[ri])
                    ri += 1
            for i in range(li, mid):
                sorted_array.append(A[i])
            for i in range(ri, r):
                sorted_array.append(A[i])
            
            for i in range(r - l):
                A[l + i] = sorted_array[i]
    return A
