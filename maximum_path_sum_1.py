"""https://projecteuler.net/problem=18"""

from pprint import pprint

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

TEST_TRIANGLE = """
   3
  7 4
 2 4 6
8 5 9 3"""


def solve(input_: str, debug: bool = False):
    best_scores = (
        {}
    )  # stores (x,y)location:score -> the max scores achievable starting from location downwards
    pyramid = [
        list(map(int, row.split())) for row in input_.splitlines() if row.strip()
    ]
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
    answer = best_scores[(0, 0)]
    if debug:
        pprint(best_scores)
    print(answer)
    return answer


if __name__ == "__main__":
    assert solve(TEST_TRIANGLE) == 23
    solve(TRIANGLE)
