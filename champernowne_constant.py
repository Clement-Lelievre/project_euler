"""https://projecteuler.net/problem=40"""
import time
from functools import reduce


def solve_naive(max_pow: int = 6) -> None:
    starttime = time.time()
    s = "".join(map(str, range(1, 10**max_pow + 1)))
    print(
        f"Naive solution: {reduce(lambda x, y: int(x) * int(y), map(s.__getitem__, (10**i-1 for i in range(max_pow+1))))} in {time.time() - starttime} seconds"
    )


def get_char(n: int) -> int:
    """The core algo.

    Args:
        n (int): the index of the digit to return. 0-based (ie takes into account the 0 before the dot in the constant)

    Returns:
        int: the digit at index n in Champernowne's constant
    """
    if n <= 9:
        return n
    consumed_indices = 10
    width = 2
    while (
        True
    ):  # a 'batch' means a group of numbers of the same width (e.g. 100 through 999 included is a batch)
        if (
            consumed_indices
            + (next_batch_nb_of_indices := width * 9 * 10 ** (width - 1))
            < n
        ):
            consumed_indices += next_batch_nb_of_indices
            width += 1
        else:
            break
    nb_ind_diff = (
        n - consumed_indices + 1
    )  # how many indices separate n from the first index of the latest batch
    nb_full_numbers, remainder = divmod(nb_ind_diff, width)
    return int(
        str(10 ** (width - 1) + nb_full_numbers - (0 if remainder else 1))[
            remainder - 1
        ]
    )


def solve_smarter(max_pow: int = 6) -> None:
    """A much better algorithm than the naive one.

    Args:
        max_pow (int, optional): the max power used in the computations (e.g. d100000). Defaults to 6 which corresponds to the text of the problem.
    """
    starttime = time.time()
    print(
        f"Smarter solution: {reduce(lambda x, y: x * y, map(get_char, (10**i for i in range(max_pow+1))))} in {time.time() - starttime} seconds"
    )


if __name__ == "__main__":
    for i in range(10):
        assert get_char(i) == i
    assert get_char(12) == 1 and get_char(13) == 1 and get_char(14) == 1
    assert (
        get_char(15) == 2
        and get_char(16) == 1
        and get_char(17) == 3
        and get_char(18) == 1
    )
    solve_naive()
    solve_smarter()
