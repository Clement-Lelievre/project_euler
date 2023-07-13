"""https://projecteuler.net/problem=37"""
from itertools import chain, product


def solve() -> None:
    BIG = 10**100  # arbitrary big number
    primes_set = set()
    not_primes_set = {
        1,
    }

    def is_prime(n: int) -> bool:
        """Check if `n` is prime"""
        if n in primes_set:
            return True
        if n in not_primes_set:
            return False
        if all(n % i for i in range(2, int(n**0.5 + 1))):
            primes_set.add(n)
            return True
        not_primes_set.add(n)
        return False

    def all_primes_left_to_right(n: int, nb_digits: int) -> bool:
        for i in range(nb_digits - 1, 0, -1):
            n %= 10**i
            if not is_prime(n):
                return False
        return True

    def all_primes_right_to_left(n: int, nb_digits: int) -> bool:
        for _ in range(nb_digits - 1):
            n //= 10
            if not is_prime(n):
                return False
        return True

    truncatable_found = []
    nb_truncatable_found = 0
    candidates = chain(
        *[product({"1", "3", "7", "9", "5", "2"}, repeat=k) for k in range(2, BIG)]
    )  # excludes 2,3,5,7 as requested
    # candidates necessarily have all their digits only among 1,3,7 or 9
    while nb_truncatable_found < 11:
        try:
            str_nb = "".join(next(candidates))
        except StopIteration:
            print("error: not found")
            break
        if (
            str_nb.startswith(("1", "9"))
            or str_nb.endswith(("1", "9", "5", "2"))
            or any(seq in str_nb for seq in ("33", "55", "77", "99"))
        ):
            continue
        current_candidate = int(str_nb)
        if not is_prime(current_candidate):
            continue
        nb_digits = len(str(current_candidate))
        if all_primes_left_to_right(
            current_candidate, nb_digits
        ) and all_primes_right_to_left(current_candidate, nb_digits):
            nb_truncatable_found += 1
            truncatable_found.append(current_candidate)
            print(f"{current_candidate} is truncatable both ways")
    else:
        print(f"{sum(truncatable_found)}, {nb_truncatable_found=}")


if __name__ == "__main__":
    solve()
