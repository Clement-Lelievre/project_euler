"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from string import ascii_uppercase as alphabet


def solve() -> None:
    with open("p022_names.txt", "r") as f:
        names = sorted(f.read().replace('"', "").split(","))
        assert names.index("COLIN") == 937
        assert sum(map(lambda x: alphabet.index(x) + 1, names[937])) == 53
        print(
            sum(
                i * sum(map(lambda x: alphabet.index(x) + 1, names[i - 1]))
                for i in range(1, len(names) + 1)
            )
        )


if __name__ == "__main__":
    solve()
