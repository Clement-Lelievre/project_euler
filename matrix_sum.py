"""https://projecteuler.net/problem=345 
We define the Matrix Sum of a matrix as the maximum possible sum of matrix elements such that none of the selected elements share the same row or column.

For example, the Matrix Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303

Find the Matrix Sum of MATRIX"""
import logging
import time
from collections import deque

import numpy as np

# from pprint import pprint # used for debugging


logging.basicConfig(level=logging.INFO)

MATRIX = """
  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805
"""

TEST_MATRIX = """ 
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303
"""

# I tried to solve this using dynamic programming but couldn't make it work
# so I'll switch to a graph problem approach, which I'm more familiar with


def get_matrix(matrix: str) -> np.ndarray:
    # use Numpy to benefit from the handy getitem notation
    return np.array(
        [
            list(map(int, rs.split()))
            for row in matrix.splitlines()
            if (rs := row.strip())
        ]
    )


def traverse_graph(matrix: np.ndarray) -> int:
    """Returns the max path sum after traversing (and pruning) the tree

    Args:
        matrix (np.array): _description_

    Returns:
        int: the max path sum found along the way
    """
    starttime = time.time()
    queue: deque = deque()
    NB_ROWS, NB_COLS = matrix.shape
    COL_NB_SET = set(range(NB_COLS))
    for start_col in range(NB_COLS):
        remaining_cols = frozenset(COL_NB_SET - {start_col})
        path_sum = matrix[0, start_col]
        queue.append(((0, start_col), remaining_cols, path_sum))
    seen: dict[tuple, int] = {}
    current_best = 0
    while queue:
        pos, rem_cols, path_sum = queue.pop()  # way faster than .popleft() -> DFS beats BFS here due to faster getting seen states, I think
        x = pos[0]
        if seen.get((x, rem_cols), -1) >= path_sum:
            continue
        seen[(x, rem_cols)] = path_sum
        if path_sum > current_best:
            current_best = path_sum
        if x == NB_ROWS - 1:
            continue  # reached the bottom of the grid
        for next_col in rem_cols:
            queue.append(
                (
                    (x + 1, next_col),
                    rem_cols - {next_col},
                    path_sum + matrix[x + 1, next_col],
                )
            )
    logging.info(f"{current_best=} in {time.time() - starttime}s")
    return current_best


def dp_solution(multiline_string_matrix: str):
    """Submitted by user MrDrake from Australia on Project Euler,
    on Sept 4th 2011. This solution leverages dynamic programming
    and is way, way faster than mine (180 times, or about 2 orders of magnitude!)
    while being also more compact, using less dependencies and probably less memory!
    Hats off to you, MrDrake!"""
    starttime = time.time()
    matrix = [
        list(map(int, rs.split()))
        for row in multiline_string_matrix.splitlines()
        if (rs := row.strip())
    ]  # this is my version of pre-processing the input
    MINUS_INF = -float("inf")
    n = len(matrix)
    dp = {0: 0}
    # key is a bitmask representing the set of columns already visited,
    # value is the max sum of the path
    for row in range(n):
        z = {}
        for column in range(n):
            x = 1 << column
            # set the bit of the current column to 1, all other remain 0
            for d in dp:
                if x & d:
                    # if in this mask, column `column` is visited, skip
                    continue
                y = matrix[row][column] + dp[d]
                # path sum = current cell weight + previous path sum
                if z.get(x | d, MINUS_INF) < y:
                    z[x | d] = y  # update the max path sum
        dp = z
    logging.info(f"{dp[(1<<n)-1]} in {time.time() - starttime}sec")
    return dp[(1 << n) - 1]  # (1 << n) - 1 is the mask with all bits set to 1,
    # meaning we want the max path sum for all columns


if __name__ == "__main__":
    assert traverse_graph(get_matrix(TEST_MATRIX)) == 3_315
    traverse_graph(get_matrix(MATRIX))
    # assert dp_solution(TEST_MATRIX) == 3315
    # dp_solution(MATRIX)
