"""https://projecteuler.net/problem=63
The 5-digit number 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number,134217728 = 8^9
, is a ninth power.

How many n-digit positive integers exist which are also an n-th power?"""


#  I observe that for any integer n, 10**n has (n+1) digits, therefore I can limit the search to k**n where 1 <= k <= 9
# Let's consider an n-digit number x. The minimum n-digit number is 10^(n-1), and the maximum n-digit number is (10^n) - 1.
# 10^(1 - 1/n) ≤ k ≤ (10 - 1/n)^(1/n)

n = 1
ans = set()
while True:
    low = 10 ** (1 - 1 / n)
    low = int(low) if low == int(low) else int(low) + 1
    print(f"{n=} {low=}")
    if low >= 10:
        break
    for c in range(low, 10):
        ans.add(c**n)
    n += 1

print(len(ans))
