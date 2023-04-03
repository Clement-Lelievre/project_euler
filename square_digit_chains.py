"""A number chain is created by continuously adding the square of the digits in a number to form a
new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
# I'll cache results in a mapping table, then iterate over it
known = {nb: sum(int(digit) ** 2 for digit in str(nb)) for nb in range(10_000_000)}


def arrives_at_eighty_nine(nb: int) -> bool:
    while True:
        if nb == 89:
            return True
        if nb == 1:
            return False
        nb = known[nb]


if __name__ == "__main__":
    assert arrives_at_eighty_nine(44) is False
    assert arrives_at_eighty_nine(85) is True
    print(sum(map(arrives_at_eighty_nine, range(1, 10_000_000))))
