"""https://projecteuler.net/problem=85"""

from math import sqrt

# I solved by hand the double summation and found that the general solution
# for l lines and c columns is: l*(l+1)*c*(c+1)/4
# with l=2 and c=3 as in the example, I do find 18


def solve() -> None:
    closest = float("inf")
    for l in range(
        int(sqrt(2 * 10**6) + 1)
    ):  # not the tightest bound, just one good enough for the program to be instantaneous
        for c in range(int(sqrt(2 * 10**6)) + 1):
            curr = l * (l + 1) * c * (c + 1) / 4
            if (new := abs(curr - 2 * 10**6)) < closest:
                best = l * c
                closest = new
            if curr > 2 * 10**6:
                break
    print(best)


if __name__ == "__main__":
    solve()
