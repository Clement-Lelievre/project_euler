"""https://projecteuler.net/problem=6
Straightforward when you know the formulae
"""


def solve(n: int) -> int:
    return n * (n + 1) * (6 * n * (n + 1) - 8 * n - 4) / 24


if __name__ == "__main__":
    assert solve(10) == 2640
    print(solve(100))
