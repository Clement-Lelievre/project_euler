"""https://projecteuler.net/problem=67

Brute-forcing is clearly not an option here (2^99 possible paths).
I'll use `dynamic programming` to solve this problem, starting from the bottom of the pyramid
and making my way up to the top.
"""

from pprint import pprint


def solve(path: str, debug: bool = False, start_square: tuple[int] = (0, 0)):
    best_scores = (
        {}
    )  # stores (x,y)location:score -> the max scores achievable starting from location downwards
    with open(path, "r") as f:
        pyramid = [list(map(int, row.split())) for row in f.readlines() if row.strip()]
    for row_nb in range(len(pyramid) - 1, -1, -1):
        if row_nb == len(pyramid) - 1:
            for col_nb in range(len(pyramid[row_nb])):
                best_scores[(row_nb, col_nb)] = pyramid[row_nb][col_nb]
        else:
            for col_nb in range(len(pyramid[row_nb])):
                best_scores[(row_nb, col_nb)] = pyramid[row_nb][col_nb] + max(
                    best_scores[(row_nb + 1, col_nb)],
                    best_scores[(row_nb + 1, col_nb + 1)],
                )
    answer = best_scores[start_square]
    if debug:
        pprint(best_scores)
    print(answer)
    return answer


if __name__ == "__main__":
    solve("p067_triangle.txt")
