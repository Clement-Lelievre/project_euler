"""https://projecteuler.net/problem=893"""

from tqdm import tqdm
from math import sqrt

DIGIT_COSTS = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
}
BASE_NUMBER_COSTS = {
    nb: sum(DIGIT_COSTS[digit] for digit in str(nb)) for nb in range(1, 10**6)
}
KNOWN_COSTS_ONLY_MUL = [0] * 10**6
for digit, points in DIGIT_COSTS.items():
    KNOWN_COSTS_ONLY_MUL[int(digit)] = points

KNOWN_COSTS_ONLY_ADD = [0] * 10**6
for digit, points in DIGIT_COSTS.items():
    KNOWN_COSTS_ONLY_ADD[int(digit)] = points


def express_number_only_mul(nb: int) -> int:
    """Find the minimum of matches needed to represent `nb`, using only x

    Args:
        nb (int): _description_

    Returns:
        int: the minimum nb of points needed to express `nb` only with multiplications
    """
    if KNOWN_COSTS_ONLY_MUL[nb] > 0:
        return KNOWN_COSTS_ONLY_MUL[nb]
    current_best = BASE_NUMBER_COSTS[nb]
    for i in range(2, int(sqrt(nb)) + 1):
        x, remainder = divmod(nb, i)
        if remainder == 0:  # nb == i * x
            if (
                new := express_number_only_mul(x) + 2 + express_number_only_mul(i)
            ) < current_best:
                current_best = new
    KNOWN_COSTS_ONLY_MUL[nb] = current_best
    return current_best


def express_number_only_add(nb: int) -> int:
    """Find the minimum of matches needed to represent `nb`, using only +

    Args:
        nb (int): _description_

    Returns:
        int: the minimum nb of points needed to express `nb` only with additions
    """
    if KNOWN_COSTS_ONLY_ADD[nb] > 0:
        return KNOWN_COSTS_ONLY_ADD[nb]
    current_best = BASE_NUMBER_COSTS[nb]
    for i in range(1, nb // 2 + 1):
        if (
            new := express_number_only_add(i) + 2 + express_number_only_add(nb - i)
        ) < current_best:
            current_best = new
    KNOWN_COSTS_ONLY_ADD[nb] = current_best
    return current_best


if __name__ == "__main__":
    assert express_number_only_mul(343) == 13  # 7 x 7 x 7
    assert express_number_only_add(88) == 12 # 77 + 11
    assert express_number_only_mul(88) == 13 # 8 x 11
    print(sum(express_number_only_mul(k) for k in range(1, 101)))
    print(sum(express_number_only_add(k) for k in range(1, 101)))
