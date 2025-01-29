"""https://projecteuler.net/problem=100"""

# I see two things that will help me find the value:
# 1) at the limit, when numbers are infinite, we have the equation:
# (1/p)² = 1/2 => 1/p = 1/sqrt(2)
# because when numbers are big enough, removing one disc has no effect on the ratio
# 2) The ratio value should be monotonic (I think), so I can stop whenever I cross the 0.5 value
# 3) (I got help for this observation:) observe that the ratio of solutions converges to ~ 5.8284..., I can then use that fact to fast forward to the solution

from math import sqrt


def solve_but_precision_error(start_total: int) -> int:
    """This is my original attempt; Correct logic except it (silently) suffers from
    float precision error, leading to an incorrect result"""
    total = start_total
    while 1:
        blue = int(total / sqrt(2)) - 1
        while blue / total * (blue - 1) / (total - 1) <= 1 / 2:
            blue += 1
            proba = blue / total * (blue - 1) / (total - 1)
            if (
                proba == 1 / 2
            ):  # this criteria is correct on paper, but fails due to precision issues
                print(f"Ans (precision error): {total=} {blue=} red={total-blue}")
                return blue
        total += 1


def solve_from(start_total: int) -> int:
    """Same as above, except it uses integer arithmetic to avoid precision errors"""
    total = start_total
    while 1:
        blue = int(total / sqrt(2)) - 1
        while total * (total - 1) - 2 * blue * (blue - 1) >= 0:
            blue += 1
            diff = total * (total - 1) - 2 * blue * (blue - 1)
            if diff == 0:
                print(f"Ans: {total=} {blue=} red={total-blue}")
                return blue
        total += 1


def solve() -> None:
    """Util function to get the solutions for the first 9 values, and then use that to find the solution for the 10^12 value.
    It's used to get an approx. of the ratio of consecutive solutions, which is then used to fast forward to the solution
    """
    total = 4
    totals, blues, reds = [], [], []
    while len(totals) < 9:
        blue = int(total / sqrt(2)) - 1
        while True:
            diff = total * (total - 1) - 2 * blue * (blue - 1)
            if diff == 0:
                print(f"{total=} {blue=} red={total-blue}")
                totals.append(total)
                blues.append(blue)
                reds.append(total - blue)
                break
            if diff < 0:
                break
            blue += 1
        total += 1

    print(
        "Ratios observed:",
        [totals[i + 1] / totals[i] for i in range(len(totals) - 1)],
        [blues[i + 1] / blues[i] for i in range(len(blues) - 1)],
        [reds[i + 1] / reds[i] for i in range(len(reds) - 1)],
        sep="\n",
        end="\n\n",
    )

    ratio = min(totals[-1] / totals[-2], blues[-1] / blues[-2], reds[-1] / reds[-2])
    ans_total = totals[-1]
    while ans_total < 10**12:
        ans_total *= ratio
    solve_from(start_total=int(ans_total))


if __name__ == "__main__":
    assert solve_from(start_total=10) == 15
    assert solve_from(start_total=22) == 85
    solve()
