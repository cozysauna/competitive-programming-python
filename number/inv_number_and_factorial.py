def inv_number_and_factorial(N, MOD):
    inv_number = [0, 1]
    inv_fact = [1, 1]
    for i in range(2, N + 1):
        inv_number.append(-inv_number[MOD % i] * (MOD // i) % MOD)
        inv_fact.append((inv_fact[-1] * inv_number[-1]) % MOD)
    return inv_number, inv_fact
