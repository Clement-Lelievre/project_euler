"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing
one thousand lines with a base/exponent pair on each line, determine which line number has
the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
# using the log, which is increasing on R*+, and in O(n)
from math import log


def solve(filepath: str = "p099_base_exp.txt") -> int:
    with open(filepath, "r") as f:
        numbers = [list(map(int, line.strip().split(","))) for line in f.readlines()]
    best_val = 0
    best_line = 0
    for i in range(len(numbers)):
        base, exp = numbers[i]
        if (res := exp * log(base)) > best_val:
            best_line = i
            best_val = res
    print(best_line + 1)
    return best_line + 1


if __name__ == "__main__":
    solve()
