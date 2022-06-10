def gcd(x, y):
    while y: x, y = y, x % y 
    return x 

def is_terminate_decimal(numerator, denominator):
    div = gcd(numerator, denominator)
    denominator //= div 
    while denominator % 2 == 0: denominator //= 2 
    while denominator % 5 == 0: denominator //= 5 
    return denominator == 1

def recurring_decimal(numerator, denominator):
    # not terminate decimal
    assert not is_terminate_decimal(numerator, denominator)

    integer, numerator = divmod(numerator, denominator)
    decimal = []
    idx = 0
    checked = {}
    quotient, remainder = divmod(numerator * 10, denominator)
    while (quotient, remainder) not in checked:
        checked[(quotient, remainder)] = idx 
        decimal.append(quotient)
        numerator = remainder
        idx += 1
        quotient, remainder = divmod(numerator * 10, denominator)

    repeat = decimal[checked[(quotient, remainder)]:]
    ans = str(integer) + '.' + ''.join(map(str, decimal))
    print(ans)
    print(f"Repeat:{repeat}")
