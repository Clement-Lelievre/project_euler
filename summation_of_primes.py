"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


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


def solve(thresh: int = 2_000_000) -> int:
    return sum(nb for nb in range(2, thresh) if is_prime(nb))


if __name__ == "__main__":
    assert solve(thresh=10) == 17
    print(solve())
