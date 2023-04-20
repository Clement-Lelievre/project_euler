"""
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from itertools import combinations
from math import sqrt

CEIL = 10_000
PROPER_DIVISORS_SUM: dict[int, int] = {
    n: 1
    + sum(
        nb + res[0]
        for nb in range(2, int(sqrt(n)) + 1)
        if (res := divmod(n, nb))[1] == 0
    )
    for n in range(2, CEIL)
}


def are_amicable(a: int, b: int) -> int:
    return a + b if PROPER_DIVISORS_SUM[a] == b and PROPER_DIVISORS_SUM[b] == a else 0


def solve(ceil: int):
    ans = sum(are_amicable(a, b) for a, b in combinations(range(2, ceil), 2))
    print(ans)
    return ans


if __name__ == "__main__":
    solve(CEIL)
