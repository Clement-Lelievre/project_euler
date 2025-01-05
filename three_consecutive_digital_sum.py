"""https://projecteuler.net/problem=164"""

from collections import defaultdict


def solve_slow(nb_digits: int = 20) -> int:
    # recursion; does not scale to the input size
    ans = 0

    def recurse(nbs: list[int]) -> None:
        nonlocal ans
        if len(nbs) == nb_digits:
            ans += 1
            return
        for i in range(9 - sum(nbs[-2:]) + 1):
            recurse(nbs + [i])

    for k in range(1, 10):
        recurse([k])
    print(ans)
    return ans


def solve_faster(nb_digits: int = 20) -> int:
    # way faster than recursion, instant solution
    LAST_TWO = [
        (i, j) for i in range(10) for j in range(9 - i + 1)
    ]  # all combinations of last two digits summing up to 9 max
    d = {
        i: defaultdict(int) for i in range(2, nb_digits + 1)
    }  # tracks {total_nb_digits: {(last_but_one_digit, last_digit): nb_occurences}, ...}

    # populate d[2] manually
    for elem in LAST_TWO:
        if elem[0] == 0:
            continue  # no leading zero permitted
        d[2][elem] = 1
    # populate the dict gradually, in DP fashion
    for curr_nb_digits in range(3, nb_digits + 1):
        for i, j in LAST_TWO:
            d[curr_nb_digits][i, j] = sum(
                {
                    k: v
                    for k, v in d[curr_nb_digits - 1].items()
                    if k[1] == i and sum(k) + j <= 9
                }.values()
            )

    ans = sum(d[nb_digits].values())
    print(ans)
    return ans


if __name__ == "__main__":
    assert solve_faster(nb_digits=2) == sum(range(10))
    assert solve_faster(3) == 165
    solve_faster(20)  # 378158756814587
