"""https://projecteuler.net/problem=79
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible
secret passcode of unknown length.
"""
import re

DATA = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716
"""


def solve() -> None:
    # extract data
    data = sorted(elem for elem in set(DATA.split()) if elem.strip())
    # build REGEX pattern for each item in data
    patterns = [re.compile(".*" + ".*".join(list(item)) + ".*") for item in data]
    # iterate over increasing integers, checking if each pattern matches,
    # and stop at the first that matches all
    nb = int("".join(sorted("".join(set("".join(data))))))
    while True:
        print(nb)
        s_repr = str(nb)
        if all(pat.match(s_repr) for pat in patterns):
            print(nb)
            break
        nb += 1


if __name__ == "__main__":
    solve()
