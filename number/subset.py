def subset(s):
    t = s 
    while t:
        yield t 
        t = (t - 1) & s 
