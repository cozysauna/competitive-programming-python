def lis(arr):
    import bisect
    ans = [arr[0]]
    for i in range(len(arr)):
        if arr[i] > ans[-1]:
            ans.append(arr[i])
        else:
            ans[bisect.bisect_left(ans, arr[i])] = arr[i]
    
    return len(ans)