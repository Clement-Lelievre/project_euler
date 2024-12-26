"""https://projecteuler.net/problem=918"""
# first I telescoped both series on pen and paper, ans saw that a0 = 4, so that all that was left to compute was
# 4 - a(10**12/2)
# I then wrote the below recursive function to get the result
# no recursion limit raise nor memoization was necessary to get the result instantly

def f(n: int) -> int:
    if n<=0:
        raise ValueError(f"found {n=}")
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n % 2==0:
        return 2 * f(n // 2)
    k = (n - 1) // 2
    return f(k) - 3 * f(k + 1)

print(4 - f(10**12 // 2))



