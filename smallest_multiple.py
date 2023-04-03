"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# the below implements the "naïve" approach slightly improved, which is to simply iterate over all numbers
# and check if they are divisible by the number, except there is a step equal to the number itself
# given a larger upper bound, I'd need to implement a more efficient algorithm
def solve(top: int) -> int:
    """Iteratively finds the smallest positive number that is evenly divisible by all of the numbers from 1 to `top`

    Args:
        top (int): The upper bound of the range of numbers to check

    Returns:
        int: The smallest positive number that is evenly divisible by all of the numbers from 1 to `top`
    """
    nb = top
    while not all(nb % i == 0 for i in range(2, top)):
        nb += top
    print(nb)
    return nb


if __name__ == "__main__":
    assert solve(10) == 2_520
    solve(20)
