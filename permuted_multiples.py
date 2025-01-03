"""https://projecteuler.net/problem=52"""

# It is unclear to me from the text whether the number obtained by 2x, 3x, 4x,5x or 6x must have the
# same number of digits as the original number, or can contain more digits as long as the unique set of digits is identical

# I'll assume the total number of digits should remain the same. Therefore, let n be the original number,
# I observe that if 6*n contains the exact same digits, then n must be above the next decimal power / 6
# example: assume n is in [1000, 10000[ then n cannot be > 10000/6 otherwise 6*n would have more than 4 digits.
# that's a huge gain, dividing by 6 the number of iterations required

# there are other observations one can make such as the fact that x2 implies there is at least one of {0,2,4,6,8} in the number I'm looking for
# This helps discard more numbers, but I'll use these only if I need to optimize my algo


def same_digits(nb: int) -> bool:
    digits = set(str(nb))
    return all(set(str(nb * k)) == digits for k in range(2, 7))


def solve():
    i = 1
    while True:
        for nb in range(10**i, 10 ** (i + 1) // 6):
            if same_digits(nb):
                print(nb)
                return nb
        i += 1


if __name__ == "__main__":
    solve()
