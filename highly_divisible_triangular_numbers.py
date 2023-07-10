"""https://projecteuler.net/problem=12"""

import math


def nb_divisors(n: int) -> int:
    large_divisors = []
    nb_divisors = 0
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            nb_divisors += 1
            if i * i != n:
                large_divisors.append(n / i)
    nb_divisors += len(large_divisors)
    return nb_divisors


def solve(nb_div: int) -> None:
    n = 1
    s = n
    while nb_divisors(s) < nb_div:
        n += 1
        s += n
    print(s)
    return s


if __name__ == "__main__":
    assert solve(5) == 28
    solve(500)
