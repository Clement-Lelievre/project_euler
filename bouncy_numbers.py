"""https://projecteuler.net/problem=112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""


def is_bouncy(nb: int) -> bool:
    nb = str(nb)
    can_be_increasing = can_be_decreasing = True
    for i in range(1, len(nb)):
        if nb[i] > nb[i - 1]:
            can_be_decreasing = False
        elif nb[i] < nb[i - 1]:
            can_be_increasing = False
        if (not can_be_increasing) and (not can_be_decreasing):
            return True
    return False


def iterate_till_ratio_reaches(ratio: float) -> int:
    nb = 100  # start at 100 (see text)
    nb_bouncing = 0
    while nb_bouncing / nb < ratio:
        nb_bouncing += is_bouncy(nb)
        nb += 1
    return nb


def iterate_till_ratio_equals(ratio: float) -> int:
    nb = 100  # start at 100 (see text)
    nb_bouncing = 0
    while True:
        nb_bouncing += is_bouncy(nb)
        if nb_bouncing / nb == ratio:
            return nb
        nb += 1


if __name__ == "__main__":
    for i in range(100):
        assert not is_bouncy(i)
    assert is_bouncy(155349)
    assert sum(map(is_bouncy, range(100, 1_000))) == 525
    print(iterate_till_ratio_equals(0.99))
