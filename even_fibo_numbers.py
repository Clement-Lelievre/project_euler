"""By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms."""


def solve(lim: int = 4_000_000) -> None:
    s = 0
    a, b = 1, 2
    while b <= lim:
        if b % 2 == 0:
            s += b
        a, b = b, b + a
    print(s)


if __name__ == "__main__":
    solve()
