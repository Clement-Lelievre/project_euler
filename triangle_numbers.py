"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values 
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common 
English words, how many are triangle words?
"""
from string import ascii_uppercase as alphabet


def solve(filepath: str) -> int:
    MAX_WORD_VALUE = 26**2  # large enough, theoretical value
    with open(filepath, "r") as f:
        words = [word.replace('"', "") for word in f.read().split(",")]
    triangle_values = []
    n = 0
    while (val := n * (n + 1) // 2) <= MAX_WORD_VALUE:
        triangle_values.append(val)
        n += 1
    ans = len(
        [
            word
            for word in words
            if sum(map(lambda x: alphabet.index(x) + 1, word)) in triangle_values
        ]
    )
    print(ans)
    return ans


if __name__ == "__main__":
    solve("p042_words.txt")
