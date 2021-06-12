class LIS():
    def __init__(self, arr):
        self.arr = arr
        self.lis = self.find_lis(arr)
    
    def find_lis(self, arr):
        def bis(idx, a, DP):
            bot = -1
            top = idx
            while top - bot > 1:
                mid = (top+bot) // 2
                if DP[mid] < a: bot = mid
                else: top = mid
            return bot+1

        INF = 10 ** 10
        DP = [INF]*n
        lis = 0
        for i, a in enumerate(arr):
            if not i: 
                DP[i] = a
                continue
            cnt = bis(i, a, DP)
            DP[cnt] = a
            lis = max(lis, cnt+1)
        return lis