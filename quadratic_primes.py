"""https://projecteuler.net/problem=27"""


def is_prime(n: int) -> bool:
    """Says if a number is prime or not.

    Args:
        n (int): the number to test

    Returns: whether the number is prime or not
    """
    if n < 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0 or any(n % i == 0 for i in range(3, int(n**0.5) + 1, 2)):
        return False
    return True


def polynom(n: int, a: int, b: int) -> int:
    return n**2 + a * n + b


def solve() -> None:
    best = 0
    best_a, best_b = None, None
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            k = 0
            while is_prime(polynom(k, a, b)):
                k += 1
            if k > best:
                best = k
                best_a = a
                best_b = b

    print(best_a * best_b)


if __name__ == "__main__":
    solve()
