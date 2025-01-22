"""https://projecteuler.net/problem=719"""

from math import sqrt
from typing import Generator
from tqdm import tqdm

# I need to iterate on square numbers less than or equal to 10**12, so I'll iterate over range(10**6) and square the numbers
# I don't see any maths property that'd help express a number as the sum of parts like explained in the text, so I'll go for a full programmatic approach
# I'll come up with criteria to early exit the generator


def is_s_number(num: int) -> bool:
    sqrt_ = sqrt(num)

    for digit_split in split_digits(
        remaining_num=str(num), done=[], maxlen=len(str(num)), nb_to_make=sqrt_
    ):
        if sum(digit_split) == sqrt_:
            return True
    return False


def split_digits(
    remaining_num: str, done: list[int], maxlen: int, nb_to_make: float
) -> Generator[list[int], None, None]:
    if not remaining_num:
        yield done
        return
    if sum(done) > nb_to_make or (
        sum(done) + int(remaining_num) < nb_to_make
    ):  # early exit, essential to scale with N=10**12
        return
    for i in range(min(maxlen, len(remaining_num)), 0, -1):
        yield from split_digits(
            remaining_num[i:],
            done + [int(remaining_num[:i])],
            maxlen=maxlen,
            nb_to_make=nb_to_make,
        )


def t(n: int) -> int:
    ans = sum(
        nb**2 for nb in tqdm(range(4, round(sqrt(n)) + 1)) if is_s_number(nb**2)
    )  # start at 4 because the nb needs to be split into at least 2 numbers: 3² has one digit, 4² has two
    print(ans)
    return ans


if __name__ == "__main__":
    assert (s := sorted(split_digits("123", [], 1, 15))) == [], s
    assert (s := sorted(split_digits("123", [], 2, 15))) == sorted(
        [[1, 23], [12, 3]]
    ), s
    assert (s := sorted(split_digits("123", [], 3, 15))) == sorted(
        [
            [1, 23],
            [12, 3],
            [123],
        ]
    ), s
    for test_value in [81, 6724, 8281, 9801]:
        assert is_s_number(test_value)
    assert t(10**4) == 41_333
    t(10**12)  # 128088830547982 in 3'45''
