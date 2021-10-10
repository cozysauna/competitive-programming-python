def partial_sum_cases(arr, K, MOD=998244353):
    if K < 0: return 0
    dp = [0] * (K+1)
    dp[0] = 1
    for a in arr:
        for j in range(K, -1, -1):
            if j+a <= K:
                dp[j+a] += dp[j]
                dp[j+a] %= MOD
    return dp[K]