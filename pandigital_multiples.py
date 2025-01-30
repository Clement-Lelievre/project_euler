"""https://projecteuler.net/problem=38"""


def is_pandigital(nb: int) -> bool:
    return sorted(str(nb)) == [str(i) for i in range(1, 10)]


def solve():
    nb = 1
    best = 0
    while nb < 10_000:  # a simple upper bound is 10000
        concat = ""
        for k in range(1, 10):
            concat += str(nb * k)
            if int(concat) > 987654321:
                break
            if k > 1 and is_pandigital(int(concat)) and int(concat) > best:
                best = int(concat)
                print(
                    f"{nb=}: 1 to {k} ({int(concat)})"
                )  # note: 192 from the text will not be printed here because it is already beaten by 9 at the time it appears
                break
        nb += 1


if __name__ == "__main__":
    assert is_pandigital(123564897)
    solve()
