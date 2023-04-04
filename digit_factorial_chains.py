"""https://projecteuler.net/problem=74
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a
starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""


def solve() -> None:
    # cache factorials up to 9!
    factorials = {"0": 1}
    for i in range(1, 10):
        factorials[str(i)] = factorials[str(i - 1)] * i

    def is_longest(number: int, chain_length: int = 60) -> bool:
        nb_iter = 0
        seen = set()
        while number not in seen:
            seen.add(number)
            number = sum(factorials[char] for char in str(number))
            nb_iter += 1
        return nb_iter == chain_length

    print(sum(map(is_longest, range(1_000_000))))


if __name__ == "__main__":
    solve()
