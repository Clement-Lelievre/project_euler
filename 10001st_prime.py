"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from summation_of_primes import is_prime


def get_primes():
    i = 0
    while True:
        if is_prime(i):
            yield i
        i += 1


def solve(target: int = 10_001) -> int:
    primes = get_primes()
    for _ in range(target):
        next(primes)
    ans = next(primes)
    print(ans)
    return ans


if __name__ == "__main__":
    assert solve(target=6) == 13
    solve()
