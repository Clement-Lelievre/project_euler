"""https://projecteuler.net/problem=45"""

from math import sqrt


def next_triangle_number(start: int) -> float:
    n = start
    while True:
        triangular = n * (n + 1) / 2
        pentagonal = (1 / 2 + sqrt(1 / 4 + 6 * triangular)) / 3 # solve the order 2 equation
        if pentagonal != int(pentagonal):
            n += 1
            continue
        hexagonal = (1 + sqrt(1 + 8 * triangular)) / 4 # solve the order 2 equation
        if hexagonal != int(hexagonal):
            n += 1
            continue
        print(triangular)
        return triangular


if __name__ == "__main__":
    assert next_triangle_number(start=2) == 285 * 286 / 2
    next_triangle_number(start=286)
