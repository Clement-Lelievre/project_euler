"""https://projecteuler.net/problem=40"""
from functools import reduce


def solve_naive() -> None:
    s = ""
    for i in range(1, 1_000_001):
        s += str(i)
    assert s[11] == "1"
    s = tuple(map(int, s))
    print(
        f"Naive solution: {reduce(lambda x, y: x * y, map(s.__getitem__, (10**i-1 for i in range(7))))}"
    )


def get_char(ind: int) -> int:
    # needs checking, currently wrong, should be quite close though
    if ind == 0:
        return 1
    n = 0
    i = 1
    while n < ind:
        n += i * 9 * 10 ** (i - 1)
        i += 1
    i -= 1
    low = n - i * 9 * 10 ** (i - 1)
    integer_part, remainder = divmod(ind - low + 1, i + 1)
    return (
        int(str(10**i + integer_part - 1)[remainder - 1])
        if remainder == 0
        else int(str(10**i + integer_part)[remainder])
    )


def solve_smarter() -> None:
    print(
        f"Smarter solution: {reduce(lambda x, y: x * y, map(get_char, (10**i - 1 for i in range(7))))}"
    )


if __name__ == "__main__":
    solve_naive()
    solve_smarter()
