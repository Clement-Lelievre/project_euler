"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_largest_prime_factor(nb: int) -> int:
    temp = factor = 1
    left = nb
    while temp != nb:
        factor += 1
        while left % factor == 0:
            temp *= factor
            left /= factor
    return factor


# could be optimize by checing the factor 2 then going to 3 and doing factor += 2, as
# the only even prime is 2
# also, using the sqrt of the number to limit the search

if __name__ == "__main__":
    assert get_largest_prime_factor(13195) == 29
    print(get_largest_prime_factor(600_851_475_143))
