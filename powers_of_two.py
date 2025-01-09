"""https://projecteuler.net/problem=686"""

from math import log10


def explore(pattern: int, nth: int) -> int:
    # this function allowed me to see that there is a clear pattern in the space between consecutive exponents that produce
    # the starting sequence '123': they are either 196, 289 or 485 (eg 2^k then 2^(k+289))
    # this observation will allow me to iterate way faster, checking only the relevant candidate powers of 2
    v = 1
    powers = []
    deltas = []
    pattern_len = int(log10(pattern)) + 1
    nb_times_pattern_found = 0
    power = 1
    while True:
        v *= 2
        v_len = int(log10(v)) + 1
        v_leading_digits = v // 10 ** (v_len - pattern_len)
        if v_leading_digits == pattern:
            nb_times_pattern_found += 1
            if powers:
                deltas.append(power - powers[-1])
                print(f"delta: {power-powers[-1]}")
            powers.append(power)
            if nb_times_pattern_found == nth:
                print(f"Ans: {power}")
                break
        power += 1
    return power


def solve(pattern: int, nth: int) -> int:
    v = 1
    pattern_len = int(log10(pattern)) + 1
    nb_times_pattern_found = 0
    power = 1
    RELEVANT_POWERS_SPACES = {k: 2**k for k in [196, 289, 485]}  # 485 is 196 + 289
    # this is obtained in explore() above, by looking at the interval between the exponents of valid powers of 2

    while nb_times_pattern_found == 0:
        # step 1: get to the first power of 2 producing a leading '123'
        v *= 2
        v_len = int(log10(v)) + 1
        v_leading_digits = v // 10 ** (v_len - pattern_len)
        if v_leading_digits == pattern:
            nb_times_pattern_found += 1
            print(f"The first power producing a leading {pattern} is {power}")
            if nb_times_pattern_found == nth:
                print(f"Ans: {power}")
                return power
            break
        power += 1
    # step 2: iterate using a step of 196, 289, or 485 forward in the exponent
    for _ in range(nth - nb_times_pattern_found):
        for candidate_power_space, value in RELEVANT_POWERS_SPACES.items():
            cand = str(v * value)
            if int(cand[: len(str(pattern))]) == pattern:
                power += candidate_power_space
                v = int(
                    cand[:14]
                )  # hack: keep only the 14 leading digits to speed up. The precision will still be OK for this input
                break

    print(f"Ans: {power}")
    return power


# just for the fun of it, implementing the solution at https://projecteuler.net/thread=686#342794
def log_analysis(n: int) -> int:
    # start from 1.23*10^k < 2^n < 1.24*10^k and apply log to all sides, getting:
    # nlog(2) - log(1.24) < k < nlog(2) - log(1.23)
    # now look if an integer k could fit into this for all n, and record them
    c = 0
    power = 1
    a, b, log2 = log10(1.24), log10(1.23), log10(2)
    while True:
        if int(power * log2 - a) != int(power * log2 - b):
            c += 1
            if c == n:
                print(power)
                return power
        power += 1
    # it turns out to be way slower than solve()


if __name__ == "__main__":
    assert solve(123, 45) == 12710
    solve(123, 678910)
    assert log_analysis(45) == 12710
    log_analysis(678910)
