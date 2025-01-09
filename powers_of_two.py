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
    for ind in range(nth - nb_times_pattern_found):
        for j, (candidate_power_space, value) in enumerate(
            RELEVANT_POWERS_SPACES.items()
        ):
            cand = v * value
            if (
                j < 2
            ):  # if we're checking the last one, it must be the one so no need to compute the leading digits
                cand_len = int(log10(cand)) + 1
                cand_leading_digits = cand // 10 ** (cand_len - pattern_len)
            if j == 2 or cand_leading_digits == pattern:
                power += candidate_power_space
                v = cand // (
                    10**32
                )  # hack: keep only the leading 32 digits to avoid getting intractable integers
                if ind % 1000 == 0 and ind:
                    print(f"found {ind} more valid powers of 2 (target: {nth})")
                break

    print(f"Ans: {power}")
    return power


# my solution above is correct but does not scale well
# I need something like the below, taken from the PE thread:


def p(prefix, num):
    v = 1.0
    j = 0
    while num > 0:
        v *= 2
        j += 1
        if v > 1000:
            v /= 10
        if int(v) == prefix:
            num -= 1
            if num % 1000 == 0:
                print(num)
    return j


if __name__ == "__main__":
    assert solve(123, 45) == 12710
    solve(123, 678910)
