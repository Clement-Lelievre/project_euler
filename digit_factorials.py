"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums, they are not included.
"""
import logging
from itertools import chain, product

logging.basicConfig(level=logging.INFO)

# I'll find the upper bound, above which it is useless to search because the smallest integer is already
# larger than the max one can do with only 9s
# I'll start building every possible combination of digits, compute the sum
# of its element-wise factorial, then checking which number based on the digits equals that sum


def find_upper_bound() -> int:
    """Narrows the search space by finding the upper bound of the number of digits

    Returns:
        int: the upper bound of the number of digits
    """
    n = 1
    while 10**n - 1 <= n * 362_880:  # 9!, because 9 is the biggest possible digit
        n += 1
    logging.info(f"Search space: up to {n-1}-digit numbers")
    return n - 1


def solve() -> None:
    """Generates combinations of digits up to the upper bound, computes the sum of their factorial,
    and checks if the sum is equal to the number based on the digits
    """
    cached_fact = {}
    upper_bound = find_upper_bound()

    def factorial(n: int) -> int:
        if n in cached_fact:
            return cached_fact[n]
        res = 1 if n in {0, 1} else n * factorial(n - 1)
        cached_fact[n] = res
        return res

    valid = set()
    for comb in chain(
        *(product(*(range(10) for _ in range(i))) for i in range(2, upper_bound + 1))
    ):
        if "".join(map(str, sorted(comb))) == "".join(
            sorted(str((val := sum(map(factorial, comb)))))
        ):
            valid.add(val)

    answer = sum(valid)
    logging.info(f"{answer=}")


if __name__ == "__main__":
    solve()
