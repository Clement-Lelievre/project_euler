"""https://projecteuler.net/problem=97
The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form 2^6972593−1; it contains exactly 2,098,960 digits.
Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.
Find the last ten digits of this prime number.
"""

# I think I can just track the last ten digits


def solve() -> None:
    """Using the trick that we can just care about the last ten digits at each iteration"""
    BIG = 10**10
    nb = 1
    for _ in range(7_830_457):
        nb = (nb * 2) % BIG
    print((nb * 28_433 + 1) % BIG)


if __name__ == "__main__":
    solve()
