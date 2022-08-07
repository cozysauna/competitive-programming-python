def factorial(N, MOD):
    fact = [1]
    for i in range(1, N + 1): fact.append(fact[-1] * i % MOD)
    return fact
