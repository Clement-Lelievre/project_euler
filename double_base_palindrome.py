"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def is_palindrome_base_10(num: int) -> int:
    reversed_num = 0
    init = num
    while num:
        # Extract the least significant digit
        digit = num % 10
        # Add the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the least significant digit
        num //= 10
    return reversed_num == init


def is_palindrome_base_2(num: int) -> int:
    # would have liked to do the bit manipulaiton:
    # num = 0b100101
    # bits = num.bit_length()
    # reversed_num = ~num & ((1 << bits) - 1)
    b = bin(num)[2:]
    return b == b[::-1]


def solve(thresh: int = 1_000_000) -> int:
    ans = 0
    for nb in range(thresh):
        if is_palindrome_base_10(nb) and is_palindrome_base_2(nb):
            ans += nb
    print(ans)
    return ans


if __name__ == "__main__":
    solve()
