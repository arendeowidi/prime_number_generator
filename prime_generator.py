
from math import sqrt

def isprimes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        number = isprimes(int(sqrt(n)))
        non_primes = {j for i in number for j in xrange(i * 2, n + 1, i)}
        primes = {x for x in xrange(2, n + 1) if x not in non_primes}

    return number
