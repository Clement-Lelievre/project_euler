"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""
from functools import reduce

# a path is a placement of 20 "Rs" (for 'Right') among 40 spots (then the remaining 20 spots will be filled with "Ds" for down)


def factorial(n: int) -> int:
    return 1 if n in {0, 1} else factorial(n - 1) * n


def k_among_n(k: int, n: int) -> int:
    assert 0 <= k <= n
    return reduce(lambda x, y: x * y, range(n - k + 1, n + 1)) // factorial(k)


if __name__ == "__main__":
    print(k_among_n(20, 40))
