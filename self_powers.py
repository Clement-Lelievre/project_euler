def naive_solution(up_to: int, n_digits: int = 10) -> str:
    # does not scale for big enough numbers
    # but unfortunately it still scales for the input, which makes the problem brute-forceable
    ans = str(sum(k**k for k in range(1, up_to + 1)))[-n_digits:].zfill(n_digits)
    print(ans)
    return ans


def smarter_solution(up_to: int, n_digits: int = 10) -> str:
    """Returns the last `n_digits` of the series 1¹ + 2² + 3³ + ... + up_to^up_to"""
    ans = 0
    for k in range(1, up_to + 1):
        modular = k
        for _ in range(k - 1):
            modular = (modular * k) % (10**n_digits)
        ans += modular
    ans = str(ans)[-n_digits:].zfill(n_digits)
    print(ans)
    return ans


assert naive_solution(up_to=3) == "0000000032"
assert smarter_solution(up_to=3) == "0000000032"

assert naive_solution(up_to=10) == "0405071317"
assert smarter_solution(up_to=10) == "0405071317"

assert naive_solution(up_to=1000) == smarter_solution(up_to=1000)

smarter_solution(up_to=1371)
try:
    naive_solution(
        up_to=1371
    )  # 1371 is the first integer such that the naive solution no longer scales => ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
except ValueError:
    print("naive solution does not scale starting from up_to=1371")
    # I wanted to get the exact value on wolfram to compare my modular solution, but didn't get the exact result: https://www.wolframalpha.com/input?i=sum%28k%5Ek%2C+k%3D1+to+1371%29
