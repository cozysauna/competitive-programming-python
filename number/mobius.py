# mobius(x) = 1  if x is a squeare-free positive integer with an EVEN number of prime factors
# mobius(x) = -1 if x is a squeare-free positive integer with an ODD number of prime factors
# mobius(x) = 0  if x has a squared prime factor
def mobius(N):
    is_prime = [1] * (N + 1)
    is_prime[0] = is_prime[1] = 0
    mobius = [0] * (N + 1)
    mobius[1] = 1
    d = [1] * (N + 1)
    for i in range(2, N + 1):
        if d[i] > 1:
            if not i % (d[i] ** 2): mobius[i] = 0
            else: mobius[i] = - mobius[i // d[i]]
        if not is_prime[i]: continue
        mobius[i] = -1
        for j in range(i ** 2, N + 1, i):
            is_prime[j] = 0
            d[j] = i
    return mobius