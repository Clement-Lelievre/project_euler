"""https://projecteuler.net/problem=41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n to exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

from itertools import permutations


def is_prime(n: int) -> bool:
    """Says if a number is prime or not.

    Args:
        n (int): the number to test

    Returns: whether the number is prime or not
    """
    if n == 2:
        return True
    if n % 2 == 0 or any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2)):
        return False
    return True


def solve():
    for i in range(9, 2, -1):
        for perm in permutations(map(str, (range(i, 0, -1)))):
            nb = int("".join(perm))
            if is_prime(nb):
                print(nb)
                return
    raise Exception("Not found")


if __name__ == "__main__":
    solve()
