def rle(S):
    ret = []
    cnt = 1
    pre = S[0]
    for e in S[1:]:
        if e != pre:
            ret.append([pre, cnt])
            cnt = 0
        cnt += 1
        pre = e 
    else:
        ret.append([pre, cnt])
    return ret
