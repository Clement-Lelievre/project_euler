"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def solve(nb_digits: int = 3) -> str:
    nb = int("9" * nb_digits)
    palindromes = []
    for nb1 in range(nb, int("9" * (nb_digits - 1)), -1):
        for nb2 in range(nb1, int("9" * (nb_digits - 1)), -1):
            if (snb := str(nb1 * nb2)) == snb[::-1]:
                palindromes.append(snb)
    answer = max(map(int, palindromes), default="No solution")
    print(f"{answer=}")
    return str(answer)


if __name__ == "__main__":
    assert solve(nb_digits=2) == "9009"
    solve(nb_digits=3)
