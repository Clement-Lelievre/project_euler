"""https://projecteuler.net/problem=455"""

# notes/ideas:
# it's clearly unfeasible to iterate over 1 billion elements, 1 million times. So there must be a BIG shortcut/trick
# iterating downwards from 1 billion may help, as whenever we find a solution, we can early exit the loop
# however, this does not help for numbers for which the solution (f(n)) is relatively small (eg 743757 in the text) as we'd still need to make close to 10**9 iterations => this can't be the solution
# maybe I only need to compute the prime numbers powers, then adjust for their factors (not sure)
# if I need to compute these big powers, I'll need to it modulo 10**9 to retain only the last 9 digits so as to avoid memory errors and speed up

# still, the above ideas will not solve it

# OK, after checking some values manually I found that there are cycles of the last  digits I need to track
from tqdm import tqdm


def f(n: int) -> int:  # CURRENTLY f(3) is a problem as the cycle is huge
    for i in range(7):
        if n == 10**i:
            return 0
    b = n
    seen = {}
    for power in range(2, 20_000_001):
        if power >= 20_000_000:
            raise Exception(
                "cycle is already 20 million members big, this won't scale, there must be a more efficient way"
            )
        b = (b * n) % (10**9)  # keep it short
        if (
            power == b
        ):  # found during the first cycle, so no need to find the full cycle
            #     print(f"in first cycle {n=} {power=} {b=}")
            return power
        if (
            b in seen
        ):  # end of cycle; no need to iterate further, retain the max and add cycle length
            cycle_len = power - seen[b]
            print(f"{power=} {cycle_len=} {n=}")
            return max(
                (k for k, v in seen.items() if (v - k) % cycle_len == 0), default=0
            )
        seen[b] = power
    return 0


def sum_f(from_: int, to: int) -> int:
    """sum f(n) for n from `from_` to `to` included"""
    s = sum(f(n) for n in tqdm(range(from_, to + 1)))
    print(s)
    return s


if __name__ == "__main__":
    # assert f(4) == 411_728_896
    # assert f(10) == 0, f(10)
    # assert f(157) == 743_757
    f(3)  # is a problem: big cycle
    # for _ in range(2,20):print(_);f(_)
    # assert sum_f(2, 10**3) == 442_530_011_399
    # sum_f(2, 10**6)
