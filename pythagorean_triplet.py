"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from itertools import combinations


def solve(n: int = 1_000):
    triplets = (elem for elem in combinations(range(999), 3) if sum(elem) == n)
    for triplet in triplets:
        m1, m2, m3 = sorted(triplet)
        if m3**2 == m1**2 + m2**2:
            break
    else:
        raise Exception("No solution")
    ans = m1 * m2 * m3
    print(ans)
    return ans


if __name__ == "__main__":
    solve()
