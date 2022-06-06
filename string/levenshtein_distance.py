def levenshtein_distance(A, B): #Edit Distance
    AL = len(A)
    BL = len(B)
    dp = [[10 ** 18] * (BL + 1) for _ in range(AL + 1)]
    dp[0][0] = 0
    for i in range(AL + 1):
        for j in range(BL + 1):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + (A[i - 1] != B[j - 1]))
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    return dp[AL][BL]