"""https://projecteuler.net/problem=104"""

from math import log10

# at first I had issues because I attempted casting b to a str which
# fails due to b being too large (which is good since otherwise this challenge would be far less interesting)
# I thought this meant b was also too big as an int so started looking in the wrong diection, but no only the str type was an issue


def solve() -> int:
    a, b = 1, 1
    index = 2
    DIGITS = set(map(str, range(1, 10)))
    while True:
        a, b = b, a + b
        index += 1
        if (
            set(str(b % (10**9))) == DIGITS
        ):  # do second calc only if the trailing digits condition is met
            nb_digits = int(log10(b))  # started on pen and paper from: 10^n >= b
            first_nine = b // (10 ** (nb_digits - 9))
            if set(str(first_nine)) == DIGITS:
                print(index)
                break


if __name__ == "__main__":
    solve()
