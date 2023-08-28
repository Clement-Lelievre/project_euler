"""https://projecteuler.net/problem=348"""


class PalindromeFinder:
    def __init__(self) -> None:
        self.squares: set[int] = {
            k**2 for k in range(2, 50_000)
        }  # need a set for O(1) lookup
        self.cubes: list[int] = [
            k**3 for k in range(2, 10_000)
        ]  # need an ordered array

    def palindrome_generator(self):
        num = 13
        while True:
            if str(num) == str(num)[::-1]:  # Check if the number is a palindrome
                yield num
            num += 2

    def is_valid(
        self,
        pal: int,
    ) -> bool:
        """Returns whether a palindrome integer meets the conditions

        Args:
            pal (int): the palindrome integer

        Returns:
            bool: the validity
        """
        nb_ways = 0
        for cube in self.cubes:
            if cube >= pal or nb_ways > 4:
                break
            if pal - cube in self.squares:
                nb_ways += 1
                # print(f"{pal} is {pal-cube} + {cube}")
        return nb_ways == 4

    def solve(self) -> None:
        """Main code"""
        ans = 0
        nb_found = 0
        palindromes = self.palindrome_generator()
        while nb_found < 5:
            pal = next(palindromes)
            if self.is_valid(pal):
                print(pal)
                ans += pal
                nb_found += 1
        print(ans)


if __name__ == "__main__":
    PF = PalindromeFinder()
    assert PF.is_valid(5_229_225)
    PF.solve()
